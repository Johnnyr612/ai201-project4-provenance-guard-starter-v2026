# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

For each of three evaluation trials, no more than 1 of 10 pieces I wrote
myself will receive the high-confidence AI label.



**Why this target:**

I would rather let some AI-written text pass than wrongly accuse a real writer.
One false accusation in ten is already a serious warning, so I want to keep
that number low and check it against writing I actually wrote.

---

## 2.

In each of three trials, the median `model_score` for five texts I identify as
clearly AI-written will be at least 0.15 higher than the median `model_score`
for five texts I wrote myself.



**Why this target:**

The model signal should show a measurable difference between these two groups,
but I do not expect it to identify authorship perfectly. I chose a gap of 0.15
as a meaningful separation to check, rather than expecting the scores never
to overlap.

---

## 3.

In each of three trials, my evaluation set will produce at least one
high-confidence human label, one unsure label, and one high-confidence AI
label.



**Why this target:**

All three labels need to be reachable or the service cannot express the
difference between a low score, an ambiguous score, and a high score. I will
use examples I expect to span those cases and check the returned labels.

---

## 4.

For a valid appeal, the service must return a success response and add an
`under_review` appeal entry to `/log` for the same `content_id`, while keeping
the original decision entry. For an unknown `content_id`, it must return a
4xx response and must not record an appeal.



**Why this target:**

An appeal should give the writer a clear confirmation and leave an auditable
record without erasing the original decision. Rejecting an unknown ID avoids
making it look as though a nonexistent decision was successfully appealed.
I will check this manually by submitting once, appealing that returned ID,
and then checking `/log`.

---

## 5.

Requests with missing, empty, or `null` text, and requests with more than
10,000 characters of text, must each receive a JSON 4xx response rather than
a 500 error. After those requests, `GET /health` must still return 200.



**Why this target:**

These inputs are invalid or beyond the text size I chose to support, so the
service should reject them clearly instead of crashing or trying to score
them. Checking health afterwards makes sure handling bad input did not take
down the service.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 9 — Capstone acceptance criteria

These are the five criteria for the Shape A operational extension: local run
path, per-request runtime logging, privacy of log contents, failure recording,
and measured request cost. The Unit 3 run is a baseline for choosing a
defensible timing target; it is not counted as a trial against these criteria.
Each criterion will be checked in three separate trials before and after the
capstone improvement.

## 1. Runtime records cover completed requests

In each of three trials, I will send ten HTTP requests: one `POST /ping`,
eight valid `POST /submit` requests with unique creator IDs, and one empty-text
`POST /submit`. The runtime log must gain exactly ten parseable JSONL entries,
one for each response. Every entry must contain `timestamp`, `method`, `route`,
`input`, `output.status_code`, and a finite, non-negative `duration_ms`; its
status code must match the HTTP response.

**Why this target:** A missing or malformed record prevents me from diagnosing
what happened after a run. Ten requests meets the capstone's minimum log
evidence without spending extra time and model calls on a larger sample; three
trials can show whether logging is consistent rather than a one-time success.

## 2. Runtime records do not expose submitted values

In each trial, none of the new runtime entries may contain the literal test
text, ping message, or any submitted `creator_id` value. Field names and text
character counts may appear; the original values may not.

**Why this target:** Submitted writing can be private, and creator IDs can
identify a writer. The service can still be diagnosed from route, field names,
lengths, status, and timing, so retaining the raw values is unnecessary.
Zero exposed test values is the privacy boundary; allowing even one raw value
would expose data without adding diagnostic value.

## 3. Empty-text failures are returned and recorded

In each trial, an empty-text `POST /submit` must return JSON HTTP 400 with
`error: "invalid_text"`. The corresponding runtime entry must record status
400 and that error, the audit log must contain the rejection, and a following
`GET /health` must return HTTP 200.

**Why this target:** A rejected request is still an event worth diagnosing.
The empty-text case is a known invalid input and the route's contract returns
400 for it. Requiring both logs and a healthy follow-up distinguishes a clear
client rejection from a crash or a failure that disappears from the record.

## 4. Ten-request compute time stays within budget

In each of three trials, I will start a fresh service process with the model
already downloaded, then submit this same controlled text ten times, using a
unique creator ID for each request: “This is controlled fictional text for
measuring local processing duration. It contains no personal writing. I am
recording repeated requests to observe the service runtime.” The arithmetic
mean of all ten `duration_ms` values, including the first request that loads
the model into memory, must be no more than 2,000 ms.

**Why this target:** The Unit 3 baseline averaged 970.911 ms, including a
9,213.277 ms first request and nine warm requests averaging 55.092 ms. A
2,000 ms mean leaves room for local timing variation while still detecting a
substantial slowdown; excluding the first request would hide a delay a user
actually experiences after a service restart.

## 5. The documented local run path preserves the control routes

In each of three trials, starting the service with the documented
`python app.py` command must allow `GET /health` and `POST /ping` to return
HTTP 200 within 10 seconds of startup.

**Why this target:** The local run path is the deployment for this project.
The model loads on the first scoring request rather than at server startup, so
ten seconds allows for Windows process startup while still catching a missing
dependency, incorrect command, or service that never binds; waiting a minute
would hide a startup failure. `/ping` is the existing control route and helps
distinguish a service-startup problem from a scoring problem.
