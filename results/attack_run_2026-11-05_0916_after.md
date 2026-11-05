# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 09:16
- Auto-marked BROKE (5xx, crash, no response): **0**
- Manual verdicts: **1 BROKE, 55 HELD**

Manual verdicts use each attack's stated target and observed response.
Whether an evasion worked depends on the threshold; here, only a `human`
label counted as a successful bypass, while `unsure` did not.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f8dce57f-3d95-4d7b-ab1a-e454a40e644c` | unsure | 0.536 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4a2de405-0250-48b8-85fc-1030f6f2d2f7` | unsure | 0.494 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3bd25690-e13e-4480-8d9c-c9bba4191348` | unsure | 0.277 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e9203599-1290-4f0e-b370-8fc73bdf4c7f` | unsure | 0.186 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3f08046f-826d-4e91-ba73-7d3fc89debe2` | unsure | 0.627 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `a06823cd-e238-4aea-a697-7aa1f219b278` | unsure | 0.423 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0497c3e3-3b5f-462f-a139-978bb5dbf4ec` | unsure | 0.133 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `3ed0f94a-e32e-4b06-bc23-e25c5407b445` | unsure | 0.544 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `86a3bd15-9368-4e33-8e98-916639a92f63` | unsure | 0.253 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7a02c555-622f-4261-84d1-2ed635a65122` | ai | 0.659 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a311c56d-081f-4077-b34b-8169c7196bf6` | unsure | 0.225 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `8889571a-6810-4760-9d41-3a317c449406` | unsure | 0.034 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `48be21ad-9048-4804-a3ff-2e87ac2afadf` | unsure | 0.024 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5e34fef7-0536-4dcd-b97c-75111234b287` | unsure | 0.094 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `9c9b9cdc-4ff8-4125-9be9-251240d53fba` | unsure | 0.099 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `1424f4ac-8197-4b28-8b0d-1228870b0eeb` | unsure | 0.065 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `90de2dc2-a25c-4978-8b88-95e157dee09c` | unsure | 0.078 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `d670fca8-07bf-41cf-bdba-134a3df95bb6` | unsure | 0.577 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c069d04f-1d7c-4263-b044-9a9897d5786b` | unsure | 0.518 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `367d0974-7c95-414b-9aa4-2d06c1eccc2e` | human | 0.749 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `41fb3f70-0d1d-4503-a38e-d7278d03903b` | unsure | 0.273 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `75ecbfd7-1ed9-4159-9ea7-a2f68325319c` | unsure | 0.419 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8ce5cdb5-0d83-4f99-955b-3d231ac24dc6` | unsure | 0.340 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `7dc83580-60cd-4655-80aa-c71a7b52173a` | unsure | 0.266 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `d6ccc9a4-16dc-445b-9fe1-a745b47d3f8c` | human | 0.640 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `113901b0-2312-4fea-8ae0-da829ab28439` | unsure | 0.191 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `36fc09ba-dfa9-4cab-9ef9-60a943ec995a` | unsure | 0.238 | HELD |
| MF06 | malformed | text is emoji only | 200 | `d3117ff2-969b-44fa-82c1-9dd635f266ad` | ai | 0.598 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `f7053e1d-edc6-479a-8570-51f670489f48` | ai | 0.525 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6833380b-5e39-461f-b8cb-dadbb56fb379` | unsure | 0.567 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `135fb331-b75d-476d-87ae-bb104a820e72` | unsure | 0.567 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f316c7c0-90b9-4cde-a5ae-806f97386541` | unsure | 0.567 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cc340202-cdc3-4022-9198-d1b5860687be` | unsure | 0.567 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `429bf5b4-e10e-475e-b81f-efc440216ef8` | unsure | 0.567 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cd90f0db-485c-4403-b201-770ea48d0aec` | unsure | 0.567 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9c92e474-156b-45fa-a728-898e850689e9` | unsure | 0.567 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ef111a0-e1e0-4062-9921-35b0ba10ab77` | unsure | 0.567 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b7fd18a3-0671-4c0d-888f-e95bd073b88e` | unsure | 0.567 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d9e59b0-2517-4cbf-b427-a74f47f540d1` | unsure | 0.567 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | BROKE | HELD |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 1 | 5 |

Manual totals: **1 BROKE, 55 HELD**. PI02 was the only broken attack.

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f8dce57f-3d95-4d7b-ab1a-e454a40e644c",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.536,
  "model_score": 0.1635,
  "style_score": 0.4165,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "4a2de405-0250-48b8-85fc-1030f6f2d2f7",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4944,
  "model_score": 0.5943,
  "style_score": 0.0377,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "3bd25690-e13e-4480-8d9c-c9bba4191348",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.2768,
  "model_score": 0.6662,
  "style_score": 0.2377,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e9203599-1290-4f0e-b370-8fc73bdf4c7f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.1864,
  "model_score": 0.6114,
  "style_score": 0.4056,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3f08046f-826d-4e91-ba73-7d3fc89debe2",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.6272,
  "model_score": 0.3212,
  "style_score": 0.1449,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "a06823cd-e238-4aea-a697-7aa1f219b278",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4228,
  "model_score": 0.5727,
  "style_score": 0.121,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "0497c3e3-3b5f-462f-a139-978bb5dbf4ec",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.1328,
  "model_score": 0.5862,
  "style_score": 0.4978,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "3ed0f94a-e32e-4b06-bc23-e25c5407b445",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.5444,
  "model_score": 0.2452,
  "style_score": 0.3243,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "86a3bd15-9368-4e33-8e98-916639a92f63",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.2526,
  "model_score": 0.7042,
  "style_score": 0.23,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "7a02c555-622f-4261-84d1-2ed635a65122",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.659,
  "model_score": 0.9792,
  "style_score": 0.7656,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "a311c56d-081f-4077-b34b-8169c7196bf6",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.2248,
  "model_score": 0.6175,
  "style_score": 0.3516,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "8889571a-6810-4760-9d41-3a317c449406",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.0336,
  "model_score": 0.7387,
  "style_score": 0.4692,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "48be21ad-9048-4804-a3ff-2e87ac2afadf",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0244,
  "model_score": 0.8051,
  "style_score": 0.4144,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5e34fef7-0536-4dcd-b97c-75111234b287",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.094,
  "model_score": 0.8329,
  "style_score": 0.2996,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "9c9b9cdc-4ff8-4125-9be9-251240d53fba",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.0988,
  "model_score": 0.8005,
  "style_score": 0.5657,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "1424f4ac-8197-4b28-8b0d-1228870b0eeb",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.0652,
  "model_score": 0.8814,
  "style_score": 0.2871,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "90de2dc2-a25c-4978-8b88-95e157dee09c",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.0776,
  "model_score": 0.8816,
  "style_score": 0.4304,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d670fca8-07bf-41cf-bdba-134a3df95bb6",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.577,
  "model_score": 0.3223,
  "style_score": 0.2064,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c069d04f-1d7c-4263-b044-9a9897d5786b",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5178,
  "model_score": 0.4625,
  "style_score": 0.1402,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "367d0974-7c95-414b-9aa4-2d06c1eccc2e",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.749,
  "model_score": 0.2044,
  "style_score": 0.1093,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "41fb3f70-0d1d-4503-a38e-d7278d03903b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.2728,
  "model_score": 0.5943,
  "style_score": 0.3146,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "75ecbfd7-1ed9-4159-9ea7-a2f68325319c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4186,
  "model_score": 0.4998,
  "style_score": 0.2269,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8ce5cdb5-0d83-4f99-955b-3d231ac24dc6",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.34,
  "model_score": 0.6401,
  "style_score": 0.1848,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "7dc83580-60cd-4655-80aa-c71a7b52173a",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.2662,
  "model_score": 0.5583,
  "style_score": 0.359,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "d6ccc9a4-16dc-445b-9fe1-a745b47d3f8c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.64,
  "model_score": 0.0,
  "style_score": 0.45,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "113901b0-2312-4fea-8ae0-da829ab28439",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.191,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "36fc09ba-dfa9-4cab-9ef9-60a943ec995a",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.238,
  "model_score": 0.9976,
  "style_score": 0.55,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "d3117ff2-969b-44fa-82c1-9dd635f266ad",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.5976,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "f7053e1d-edc6-479a-8570-51f670489f48",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.5252,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "6833380b-5e39-461f-b8cb-dadbb56fb379",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "135fb331-b75d-476d-87ae-bb104a820e72",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "f316c7c0-90b9-4cde-a5ae-806f97386541",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "cc340202-cdc3-4022-9198-d1b5860687be",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "429bf5b4-e10e-475e-b81f-efc440216ef8",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "cd90f0db-485c-4403-b201-770ea48d0aec",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "9c92e474-156b-45fa-a728-898e850689e9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "1ef111a0-e1e0-4062-9921-35b0ba10ab77",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "b7fd18a3-0671-4c0d-888f-e95bd073b88e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "3d9e59b0-2517-4cbf-b427-a74f47f540d1",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We can't tell confidently who wrote this. If you wrote it yourself, you can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
