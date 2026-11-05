#!/usr/bin/env python3
"""
Run your five criteria three times each.  <- UNIT 8, MILESTONE 3

    python app.py                              # in one terminal
    python run_eval.py --label before          # in another
    python run_eval.py --label after

The attack set tests what staff thought to test. This tests what *you* thought
to test, and the two rarely overlap much. Both count.

Fill in `scenarios.py` first — that's where you say what each criterion needs
run against it. A criterion about false positives needs your own writing. One
about label coverage needs inputs across the score range.

An `appeals` scenario exercises a valid appeal and an unknown content ID,
including the resulting status and audit-log entries.

!! Three trials, and **your first signal runs a model, so identical input can
score differently twice.** That's exactly why repeats matter here.

This does the sending and the recording. It does not decide whether a trial
passed — that depends on the criterion you wrote, so the Verdict column comes
back blank.
"""

import argparse
import datetime as dt
import json
import statistics
import sys
import uuid
from pathlib import Path

import config

# Windows consoles often run a codepage that can't print every character in
# this file's help text. Without this, `--help` ends in a UnicodeEncodeError
# traceback instead of the help — which is a miserable first thing to hit.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):  # not a normal text stream
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def bodies_for(scenario, trial_number):
    """
    The request bodies one scenario sends.

    A "texts" scenario gets a creator_id made up for it. A "bodies" scenario
    keeps its request shape, while valid creator IDs get trial-specific suffixes
    so repeated bad-input checks don't collide with the rate limit.
    """
    if scenario.get("bodies"):
        bodies = []
        for i, original in enumerate(scenario["bodies"], 1):
            body = dict(original)
            creator_id = body.get("creator_id")
            if isinstance(creator_id, str):
                body["creator_id"] = f"{creator_id}_t{trial_number}_{i}"
            bodies.append(body)
        return bodies
    return [
        {"text": text, "creator_id": f"eval_{scenario['name'][:12]}_{i}"}
        for i, text in enumerate(scenario["texts"], 1)
    ]


def response_json(response):
    """Return decoded JSON, preserving a short note for a non-JSON response."""
    try:
        return response.json()
    except ValueError:
        return {"non_json": response.text[:300]}


def group_score_summary(scenario, results):
    """Summarize configured model-score groups from one text trial."""
    medians = {}
    for group, indexes in scenario["groups"].items():
        scores = [
            results[index].get("model_score")
            for index in indexes
            if index < len(results)
        ]
        if len(scores) != len(indexes) or not all(
            isinstance(score, (int, float)) for score in scores
        ):
            medians[group] = None
        else:
            medians[group] = round(statistics.median(scores), 4)

    values = list(medians.values())
    gap = (
        round(values[1] - values[0], 4)
        if len(values) == 2 and all(value is not None for value in values)
        else None
    )
    return {
        "check": "group model-score medians",
        "median_model_scores": medians,
        "second_group_minus_first_group": gap,
    }


def run_appeal_trial(requests, url, scenario, trial_number, timeout):
    """Exercise valid and unknown-content appeals and verify their log effects."""
    content_id = None
    creator_id = f"eval_appeal_{trial_number}_{uuid.uuid4().hex[:8]}"
    try:
        submission = requests.post(
            f"{url}/submit",
            json={"text": scenario["appeals"]["text"], "creator_id": creator_id},
            timeout=timeout,
        )
        submission_body = response_json(submission)
        if not isinstance(submission_body, dict):
            submission_body = {"response": submission_body}
        content_id = submission_body.get("content_id")
        if submission.status_code != 200 or not content_id:
            return [{
                "check": "valid appeal",
                "submission_status": submission.status_code,
                "submission_body": submission_body,
                "passed": False,
            }]

        appeal = requests.post(
            f"{url}/appeal",
            json={
                "content_id": content_id,
                "reasoning": scenario["appeals"]["reasoning"],
            },
            timeout=timeout,
        )
        appeal_body = response_json(appeal)
        if not isinstance(appeal_body, dict):
            appeal_body = {"response": appeal_body}
        current = requests.get(f"{url}/content/{content_id}", timeout=timeout)
        current_body = response_json(current)
        if not isinstance(current_body, dict):
            current_body = {"response": current_body}
        log_response = requests.get(f"{url}/log?limit=500", timeout=timeout)
        log_body = response_json(log_response)
        if not isinstance(log_body, dict):
            log_body = {}
        matching = [
            entry for entry in log_body.get("entries", [])
            if entry.get("content_id") == content_id
        ]
        decision_retained = any(entry.get("status") == "decided" for entry in matching)
        appeal_recorded = any(entry.get("event") == "appeal" for entry in matching)
        valid_passed = (
            appeal.status_code == 200
            and current.status_code == 200
            and current_body.get("status") == "under_review"
            and decision_retained
            and appeal_recorded
        )
        valid_result = {
            "check": "valid appeal",
            "content_id": content_id,
            "submission_status": submission.status_code,
            "appeal_status": appeal.status_code,
            "appeal_body": appeal_body,
            "content_status": current.status_code,
            "current_status": current_body.get("status"),
            "decision_retained": decision_retained,
            "appeal_recorded_in_log": appeal_recorded,
            "passed": valid_passed,
        }

        unknown_id = f"unknown-eval-{uuid.uuid4().hex}"
        unknown = requests.post(
            f"{url}/appeal",
            json={
                "content_id": unknown_id,
                "reasoning": scenario["appeals"]["reasoning"],
            },
            timeout=timeout,
        )
        unknown_body = response_json(unknown)
        if not isinstance(unknown_body, dict):
            unknown_body = {"response": unknown_body}
        unknown_log_response = requests.get(f"{url}/log?limit=500", timeout=timeout)
        unknown_log_body = response_json(unknown_log_response)
        if not isinstance(unknown_log_body, dict):
            unknown_log_body = {}
        unknown_recorded = any(
            entry.get("content_id") == unknown_id
            for entry in unknown_log_body.get("entries", [])
        )
        unknown_result = {
            "check": "unknown content appeal",
            "status": unknown.status_code,
            "body": unknown_body,
            "appeal_recorded_in_log": unknown_recorded,
            "passed": 400 <= unknown.status_code < 500 and not unknown_recorded,
        }
        return [valid_result, unknown_result]
    except Exception as exc:  # noqa: BLE001
        return [{
            "check": "appeal path",
            "content_id": content_id,
            "error": f"{type(exc).__name__}: {exc}",
            "passed": False,
        }]


def describe(body):
    """A short, readable note of what was sent — for the report."""
    if set(body) == {"text", "creator_id"} and isinstance(body.get("text"), str):
        text = body["text"]
        return text[:70] if text else "(empty text)"
    return json.dumps(body)[:120]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        print("The `requests` package isn't installed.\n"
              "Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)

    try:
        import scenarios
    except ImportError:
        print("No scenarios.py found. Milestone 3 starts by filling it in.",
              file=sys.stderr)
        sys.exit(1)

    problems = scenarios.validate()
    if problems:
        print("scenarios.py has problems:\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py",
              file=sys.stderr)
        sys.exit(1)

    if args.trials < 3:
        print(f"!! {args.trials} trial(s). The submission asks for three.\n")

    rows = []
    for scenario in scenarios.SCENARIOS:
        print(f"\n{scenario['name']}  (criterion {scenario.get('criterion') or '—'})")

        trials = []
        for trial in range(1, args.trials + 1):
            if scenario.get("appeals"):
                results = run_appeal_trial(
                    requests, args.url, scenario, trial, args.timeout
                )
                trials.append(results)
                passed = all(result.get("passed") for result in results)
                print(f"  trial {trial}: {'PASS' if passed else 'FAIL'}")
                continue

            results = []
            for i, body in enumerate(bodies_for(scenario, trial), 1):
                preview = describe(body)
                try:
                    response = requests.post(f"{args.url}/submit", json=body,
                                             timeout=args.timeout)
                    payload = response.json() if response.content else {}
                    results.append({
                        "status": response.status_code,
                        "guess": payload.get("guess"),
                        "confidence": payload.get("confidence"),
                        "model_score": payload.get("model_score"),
                        "style_score": payload.get("style_score"),
                        "label": payload.get("label"),
                        "sent": preview,
                    })
                except Exception as exc:  # noqa: BLE001
                    results.append({
                        "status": None,
                        "error": f"{type(exc).__name__}: {exc}",
                        "sent": preview,
                    })

            if scenario.get("groups"):
                results.append(group_score_summary(scenario, results))

            if scenario.get("health_check"):
                try:
                    health = requests.get(f"{args.url}/health", timeout=5)
                    health_body = response_json(health)
                    results.append({
                        "check": "health after invalid requests",
                        "status": health.status_code,
                        "ok": (
                            isinstance(health_body, dict)
                            and health_body.get("ok") is True
                        ),
                        "body": health_body,
                    })
                except Exception as exc:  # noqa: BLE001
                    results.append({
                        "check": "health after invalid requests",
                        "status": None,
                        "ok": False,
                        "error": f"{type(exc).__name__}: {exc}",
                    })

            trials.append(results)
            outcomes = [
                r.get("guess") or str(r.get("status") or "—")
                for r in results
                if r.get("check") != "group model-score medians"
            ]
            print(f"  trial {trial}: {', '.join(outcomes)}")

        rows.append({"scenario": scenario, "trials": trials})

    write_report(rows, args)


def write_report(rows, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"run_{stamp}{label}.md"

    n = args.trials
    headers = " | ".join(f"Run {i}" for i in range(1, n + 1))
    divider = "|".join(["---"] * n)

    lines = [
        f"# Run log{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_eval.py::main`",
        "- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`",
        f"- {n} trials per criterion · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Fill in Target from `criteria.md`, and Run and Verdict from the output",
        "underneath. Whether a trial passed depends on the criterion you wrote.",
        "",
        f"| Criterion | Target | {headers} | Verdict |",
        f"|---|---|{divider}|---|",
    ]

    for row in rows:
        scenario = row["scenario"]
        number = scenario.get("criterion")
        name = f"{number}. {scenario['name']}" if number else scenario["name"]
        target = scenario.get("target", "").replace("|", "\\|")
        lines.append(f"| {name} | {target} | {' | '.join([' '] * n)} |  |")

    lines += ["", "---", "", "## What actually came back", "",
              "Real output. Paste the relevant parts into your README — the rubric",
              "asks for the actual JSON, not a description of it.", ""]

    for row in rows:
        scenario = row["scenario"]
        lines += [f"### {scenario['name']}", ""]
        if scenario.get("source_note"):
            lines += [f"*Note:* {scenario['source_note']}", ""]
        for trial_number, results in enumerate(row["trials"], 1):
            lines += [f"**Trial {trial_number}**", "", "```json",
                      json.dumps(results, indent=2), "```", ""]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Commit it. It's the evidence the test actually happened.")


if __name__ == "__main__":
    main()
