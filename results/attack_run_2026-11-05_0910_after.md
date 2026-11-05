# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 09:10
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `742d656d-e199-4967-85fd-953e7b3ff926` | human | 0.536 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9e3e5191-aed1-42a0-a379-91ed95c104fe` | human | 0.494 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6b247af2-8910-4906-b94b-a0718f9d89ac` | unsure | 0.277 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ed08f497-c85d-4db6-ab50-8956f8ee4c66` | unsure | 0.186 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0b25c3fe-b4d4-4198-b04b-313c1af2b33c` | human | 0.627 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `80073374-08c9-4af1-a3b6-828310c27f23` | human | 0.423 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `02b237fd-e352-44ab-a44d-3e52180aa9c3` | unsure | 0.133 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `b7b3014b-18fd-4924-a30e-ba06fe2b807c` | human | 0.544 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `53025428-e682-416c-8b71-b22dc4b158d1` | unsure | 0.253 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `4c32b5ef-cfab-47d3-9ee6-d722aa62f20d` | ai | 0.659 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `41dea3c9-980b-457e-a73f-632c8f0651f2` | unsure | 0.225 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `aa31ec7f-e8cc-4b96-9f0a-c837d7617df8` | unsure | 0.034 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ba4e69fe-61fa-4080-96ce-9d8993cc204d` | unsure | 0.024 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ea9e72bf-2f78-48f7-81e0-d8ca68dd041e` | unsure | 0.094 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `349d5040-08d2-4223-8e12-ef07527b1b2e` | unsure | 0.099 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `3576b70f-514d-4a30-aabc-456f6f035710` | unsure | 0.065 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `238340fc-b037-4b48-b67d-3ba6b9242928` | unsure | 0.078 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `7de9c7a0-ea23-41cb-bbf4-2ef40ea37a63` | human | 0.577 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f2e9d558-4edc-4dcd-9f50-aa7797cfc789` | human | 0.518 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7e677fbf-1826-418e-973e-23ab653c5b5d` | human | 0.749 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `a01f5429-efa3-461d-8bd3-a45d817ce6e2` | unsure | 0.273 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a1033b9d-c458-46c9-a011-6e66916e3b7e` | human | 0.419 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a69396ed-9279-4c87-a972-3c7e3a3948be` | human | 0.340 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bc4dfd8b-f0f2-4912-912d-51c3a16143f4` | unsure | 0.266 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `5771f302-4565-4541-a96d-8cb307ffa131` | human | 0.640 |  |
| MF04 | malformed | text is only punctuation | 200 | `aa510a8c-ce80-479c-aaf8-0448a4d9b46f` | unsure | 0.191 |  |
| MF05 | malformed | text is a very long single word | 200 | `d6a7f81e-5933-47c2-8a39-9c7e6457d6f5` | unsure | 0.238 |  |
| MF06 | malformed | text is emoji only | 200 | `647926aa-f097-4b4d-a765-5ebdaf147f36` | ai | 0.598 |  |
| MF07 | malformed | text is right-to-left script | 200 | `835d54be-0722-4c61-8bc1-0b28ab5ebbec` | ai | 0.525 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f3473100-ea44-4852-aac0-8f886e474170` | human | 0.567 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fb042fea-f142-470f-8e8c-cf81ebcad26a` | human | 0.567 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `840839cd-4c76-4371-8194-893cac2c13c4` | human | 0.567 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4b086d8b-7b41-4fa3-bb1d-c66af0e45dac` | human | 0.567 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fdf56ee5-269e-4012-b2f8-606e4aca9a04` | human | 0.567 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `687d4625-028c-4b87-8799-382994e13308` | human | 0.567 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `afc5d535-1e2e-4a04-aab1-7030caba96c1` | human | 0.567 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a623b89d-5944-442d-bb92-70ea0405a67b` | human | 0.567 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `349a3b60-a4be-4a9e-b934-69abed0d74ec` | human | 0.567 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `039a5651-6d6f-41f8-b78a-ead0c4c36bfa` | human | 0.567 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

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
  "content_id": "742d656d-e199-4967-85fd-953e7b3ff926",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.536,
  "model_score": 0.1635,
  "style_score": 0.4165,
  "label": "We think this was probably written by a person.",
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
  "content_id": "9e3e5191-aed1-42a0-a379-91ed95c104fe",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.4944,
  "model_score": 0.5943,
  "style_score": 0.0377,
  "label": "We think this was probably written by a person.",
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
  "content_id": "6b247af2-8910-4906-b94b-a0718f9d89ac",
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
  "content_id": "ed08f497-c85d-4db6-ab50-8956f8ee4c66",
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
  "content_id": "0b25c3fe-b4d4-4198-b04b-313c1af2b33c",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6272,
  "model_score": 0.3212,
  "style_score": 0.1449,
  "label": "We think this was probably written by a person.",
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
  "content_id": "80073374-08c9-4af1-a3b6-828310c27f23",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.4228,
  "model_score": 0.5727,
  "style_score": 0.121,
  "label": "We think this was probably written by a person.",
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
  "content_id": "02b237fd-e352-44ab-a44d-3e52180aa9c3",
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
  "content_id": "b7b3014b-18fd-4924-a30e-ba06fe2b807c",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.5444,
  "model_score": 0.2452,
  "style_score": 0.3243,
  "label": "We think this was probably written by a person.",
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
  "content_id": "53025428-e682-416c-8b71-b22dc4b158d1",
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
  "content_id": "4c32b5ef-cfab-47d3-9ee6-d722aa62f20d",
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
  "content_id": "41dea3c9-980b-457e-a73f-632c8f0651f2",
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
  "content_id": "aa31ec7f-e8cc-4b96-9f0a-c837d7617df8",
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
  "content_id": "ba4e69fe-61fa-4080-96ce-9d8993cc204d",
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
  "content_id": "ea9e72bf-2f78-48f7-81e0-d8ca68dd041e",
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
  "content_id": "349d5040-08d2-4223-8e12-ef07527b1b2e",
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
  "content_id": "3576b70f-514d-4a30-aabc-456f6f035710",
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
  "content_id": "238340fc-b037-4b48-b67d-3ba6b9242928",
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
  "content_id": "7de9c7a0-ea23-41cb-bbf4-2ef40ea37a63",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.577,
  "model_score": 0.3223,
  "style_score": 0.2064,
  "label": "We think this was probably written by a person.",
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
  "content_id": "f2e9d558-4edc-4dcd-9f50-aa7797cfc789",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.5178,
  "model_score": 0.4625,
  "style_score": 0.1402,
  "label": "We think this was probably written by a person.",
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
  "content_id": "7e677fbf-1826-418e-973e-23ab653c5b5d",
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
  "content_id": "a01f5429-efa3-461d-8bd3-a45d817ce6e2",
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
  "content_id": "a1033b9d-c458-46c9-a011-6e66916e3b7e",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.4186,
  "model_score": 0.4998,
  "style_score": 0.2269,
  "label": "We think this was probably written by a person.",
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
  "content_id": "a69396ed-9279-4c87-a972-3c7e3a3948be",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.34,
  "model_score": 0.6401,
  "style_score": 0.1848,
  "label": "We think this was probably written by a person.",
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
  "content_id": "bc4dfd8b-f0f2-4912-912d-51c3a16143f4",
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
  "content_id": "5771f302-4565-4541-a96d-8cb307ffa131",
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
  "content_id": "aa510a8c-ce80-479c-aaf8-0448a4d9b46f",
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
  "content_id": "d6a7f81e-5933-47c2-8a39-9c7e6457d6f5",
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
  "content_id": "647926aa-f097-4b4d-a765-5ebdaf147f36",
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
  "content_id": "835d54be-0722-4c61-8bc1-0b28ab5ebbec",
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
  "content_id": "f3473100-ea44-4852-aac0-8f886e474170",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "fb042fea-f142-470f-8e8c-cf81ebcad26a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "840839cd-4c76-4371-8194-893cac2c13c4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "4b086d8b-7b41-4fa3-bb1d-c66af0e45dac",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "fdf56ee5-269e-4012-b2f8-606e4aca9a04",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "687d4625-028c-4b87-8799-382994e13308",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "afc5d535-1e2e-4a04-aab1-7030caba96c1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "a623b89d-5944-442d-bb92-70ea0405a67b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "349a3b60-a4be-4a9e-b934-69abed0d74ec",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
  "content_id": "039a5651-6d6f-41f8-b78a-ead0c4c36bfa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5666,
  "model_score": 0.0287,
  "style_score": 0.513,
  "label": "We think this was probably written by a person.",
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
