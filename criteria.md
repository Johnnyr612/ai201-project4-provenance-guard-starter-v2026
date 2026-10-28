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
