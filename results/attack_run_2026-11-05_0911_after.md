# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 09:11
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `31651c82-9741-4204-a283-4ec15be6c2b9` | human | 0.536 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8f866cbc-36c7-4300-83fe-51646a8f1753` | human | 0.494 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `afade792-361d-44da-b847-84cac87dde46` | unsure | 0.277 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `38df1888-7420-445a-9fca-2b69ce2cf84d` | unsure | 0.186 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9ac14d94-ba43-4c4c-b4a7-78aedce1dc96` | human | 0.627 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `244ec1e9-3aaf-4764-9372-a6ad11154433` | human | 0.423 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e7975dd3-d8e8-4220-8239-ad92280059ca` | unsure | 0.133 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `ce57239f-c2dd-4460-9a98-1c87daf04e04` | human | 0.544 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3d01b170-f1d2-49c7-a799-a8177731b2dd` | unsure | 0.253 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3a902021-ec74-4572-9087-9ccdc5cfcf4b` | ai | 0.659 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `2ee4d7da-6b02-4353-8c40-64273c8b2746` | unsure | 0.225 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `b4746ca4-634a-4323-9c19-067ae92d81ad` | unsure | 0.034 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `d03cae6d-3726-4454-b614-c50475276043` | unsure | 0.024 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `32c20c5b-11f0-4d8d-a240-816f540c2ab6` | unsure | 0.094 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ffa8371e-70b5-4b82-8d05-127b2435834a` | unsure | 0.099 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `7fec9360-bec1-4a49-ad2b-b5daa0f7ea89` | unsure | 0.065 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `bb109102-fe7b-429e-8ad5-ceff1e95a828` | unsure | 0.078 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `cd16ee88-f158-495d-9214-eeb205288fa3` | human | 0.577 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c1ee9b76-4d8e-41e9-a039-4f3901527a44` | human | 0.518 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `28474be0-d0ac-4a33-a54f-c01943df7793` | human | 0.749 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ef745282-bfa7-4669-a064-3b33c0bf8f7a` | unsure | 0.273 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c38855ef-e466-4cdf-9a2d-3511aec8c1d9` | human | 0.419 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `83bbd0ad-6069-4216-91d6-6d2595a75d90` | human | 0.340 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `10f0399b-7dc1-4c15-be94-c83632c29f69` | unsure | 0.266 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `068a7449-c30c-4fef-9ef6-b777ef155524` | human | 0.640 |  |
| MF04 | malformed | text is only punctuation | 200 | `288e9b03-1029-4c1c-a54b-989cdf7fc3c8` | unsure | 0.191 |  |
| MF05 | malformed | text is a very long single word | 200 | `fcaeab06-2f20-4087-9f1a-7f6c154b781c` | unsure | 0.238 |  |
| MF06 | malformed | text is emoji only | 200 | `bd4b55b0-38af-4889-b09b-69b634801208` | ai | 0.598 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ba05ad77-6531-4b4d-bf5b-00a722c900a2` | ai | 0.525 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b8bdf0d1-6085-4738-b5fd-2ffd1db5be89` | human | 0.567 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2ec0316c-1fa3-4d56-a3cd-1397f0eef674` | human | 0.567 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b1204dc0-97ff-47f0-89df-1782d1f255c2` | human | 0.567 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3094a76a-340d-4d82-80c1-4b8b7d9ab135` | human | 0.567 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `afed5bbf-8bc5-4a9e-a02a-4f6fde14c078` | human | 0.567 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a4b20fe-83a4-4c64-84c8-8a9f482322b1` | human | 0.567 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `237e8f54-41d7-4695-9c16-f9f546bf9647` | human | 0.567 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d59d8e7f-0484-4395-9298-270c05dc5703` | human | 0.567 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d78b2fae-0089-49e0-be46-f0e24e3bd076` | human | 0.567 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `209f6bbe-93c4-4518-bfdb-1e59a17e5204` | human | 0.567 |  |
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
  "content_id": "31651c82-9741-4204-a283-4ec15be6c2b9",
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
  "content_id": "8f866cbc-36c7-4300-83fe-51646a8f1753",
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
  "content_id": "afade792-361d-44da-b847-84cac87dde46",
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
  "content_id": "38df1888-7420-445a-9fca-2b69ce2cf84d",
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
  "content_id": "9ac14d94-ba43-4c4c-b4a7-78aedce1dc96",
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
  "content_id": "244ec1e9-3aaf-4764-9372-a6ad11154433",
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
  "content_id": "e7975dd3-d8e8-4220-8239-ad92280059ca",
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
  "content_id": "ce57239f-c2dd-4460-9a98-1c87daf04e04",
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
  "content_id": "3d01b170-f1d2-49c7-a799-a8177731b2dd",
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
  "content_id": "3a902021-ec74-4572-9087-9ccdc5cfcf4b",
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
  "content_id": "2ee4d7da-6b02-4353-8c40-64273c8b2746",
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
  "content_id": "b4746ca4-634a-4323-9c19-067ae92d81ad",
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
  "content_id": "d03cae6d-3726-4454-b614-c50475276043",
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
  "content_id": "32c20c5b-11f0-4d8d-a240-816f540c2ab6",
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
  "content_id": "ffa8371e-70b5-4b82-8d05-127b2435834a",
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
  "content_id": "7fec9360-bec1-4a49-ad2b-b5daa0f7ea89",
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
  "content_id": "bb109102-fe7b-429e-8ad5-ceff1e95a828",
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
  "content_id": "cd16ee88-f158-495d-9214-eeb205288fa3",
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
  "content_id": "c1ee9b76-4d8e-41e9-a039-4f3901527a44",
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
  "content_id": "28474be0-d0ac-4a33-a54f-c01943df7793",
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
  "content_id": "ef745282-bfa7-4669-a064-3b33c0bf8f7a",
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
  "content_id": "c38855ef-e466-4cdf-9a2d-3511aec8c1d9",
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
  "content_id": "83bbd0ad-6069-4216-91d6-6d2595a75d90",
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
  "content_id": "10f0399b-7dc1-4c15-be94-c83632c29f69",
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
  "content_id": "068a7449-c30c-4fef-9ef6-b777ef155524",
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
  "content_id": "288e9b03-1029-4c1c-a54b-989cdf7fc3c8",
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
  "content_id": "fcaeab06-2f20-4087-9f1a-7f6c154b781c",
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
  "content_id": "bd4b55b0-38af-4889-b09b-69b634801208",
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
  "content_id": "ba05ad77-6531-4b4d-bf5b-00a722c900a2",
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
  "content_id": "b8bdf0d1-6085-4738-b5fd-2ffd1db5be89",
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
  "content_id": "2ec0316c-1fa3-4d56-a3cd-1397f0eef674",
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
  "content_id": "b1204dc0-97ff-47f0-89df-1782d1f255c2",
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
  "content_id": "3094a76a-340d-4d82-80c1-4b8b7d9ab135",
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
  "content_id": "afed5bbf-8bc5-4a9e-a02a-4f6fde14c078",
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
  "content_id": "2a4b20fe-83a4-4c64-84c8-8a9f482322b1",
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
  "content_id": "237e8f54-41d7-4695-9c16-f9f546bf9647",
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
  "content_id": "d59d8e7f-0484-4395-9298-270c05dc5703",
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
  "content_id": "d78b2fae-0089-49e0-be46-f0e24e3bd076",
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
  "content_id": "209f6bbe-93c4-4518-bfdb-1e59a17e5204",
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
