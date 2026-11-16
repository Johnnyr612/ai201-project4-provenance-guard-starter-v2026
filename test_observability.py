import json
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

import app
import config


class RuntimeLoggingTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        log_dir = Path(self.temp_dir.name)
        self.runtime_log = log_dir / "runtime.jsonl"
        self.audit_log = log_dir / "audit.jsonl"
        self.config_patch = patch.multiple(
            config,
            LOG_DIR=log_dir,
            RUNTIME_LOG=self.runtime_log,
            AUDIT_LOG=self.audit_log,
        )
        self.config_patch.start()
        self.addCleanup(self.config_patch.stop)

        self.client = app.app.test_client()

    def read_events(self):
        return [
            json.loads(line)
            for line in self.runtime_log.read_text(encoding="utf-8").splitlines()
        ]

    def test_ping_response_is_unchanged_and_request_values_are_not_logged(self):
        message = "private sample text"
        response = self.client.post("/ping", json={"message": message})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "ok": True,
            "you_sent": message,
            "service": "provenance-guard",
        })

        event = self.read_events()[0]
        self.assertEqual(event["event"], "http_request")
        self.assertEqual(event["route"], "/ping")
        self.assertEqual(event["input"]["message_characters"], len(message))
        self.assertEqual(event["output"]["status_code"], 200)
        self.assertIn("you_sent", event["output"]["json_fields"])
        self.assertIsInstance(event["duration_ms"], (int, float))
        self.assertGreaterEqual(event["duration_ms"], 0)
        self.assertNotIn(message, self.runtime_log.read_text(encoding="utf-8"))

    def test_submit_runtime_event_correlates_with_audit_decision(self):
        text = "A controlled sample for checking runtime and audit correlation."
        creator_id = "private-correlation-test-writer"
        with (
            patch("detector.model_signal", return_value=0.4),
            patch("stylometry.style_signal", return_value=0.4),
            patch("stylometry.repetition_signal", return_value=0.0),
        ):
            response = self.client.post(
                "/submit",
                json={"text": text, "creator_id": creator_id},
            )

        self.assertEqual(response.status_code, 200)
        content_id = response.get_json()["content_id"]
        event = self.read_events()[0]
        self.assertEqual(event["output"]["content_id"], content_id)

        audit_entries = [
            json.loads(line)
            for line in self.audit_log.read_text(encoding="utf-8").splitlines()
        ]
        self.assertTrue(
            any(entry.get("content_id") == content_id for entry in audit_entries)
        )

        runtime_text = self.runtime_log.read_text(encoding="utf-8")
        self.assertNotIn(text, runtime_text)
        self.assertNotIn(creator_id, runtime_text)

    def test_unknown_content_response_is_logged(self):
        response = self.client.get(f"/content/{uuid.uuid4()}")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["error"], "not_found")

        event = self.read_events()[0]
        self.assertEqual(event["route"], "/content/<content_id>")
        self.assertEqual(event["output"]["status_code"], 404)
        self.assertEqual(event["output"]["error"], "not_found")


if __name__ == "__main__":
    unittest.main()
