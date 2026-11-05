# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 17:08
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

Manual verdicts below use the attack's stated target and observed response.
For evasion, a human label counts as a successful bypass; unsure does not.
For false-positive cases, only an AI label counts as a false accusation.
Malformed inputs are held when rejected or handled without a server error;
this is an availability judgment, not a claim that every accepted text is
meaningful. Flood requests are held when the configured quota is enforced.

Manual totals: **7 BROKE, 49 HELD**.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `52000f22-399b-46b6-ac41-e9eeef252972` | human | 0.536 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4be0fdc7-a009-47de-9d29-0129f4c43bcd` | human | 0.494 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f183804a-156e-42f1-9d2a-3e88973a790d` | unsure | 0.277 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d858ed2a-88ff-4440-8650-d89ebe657759` | unsure | 0.186 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `20e2dc6e-70b1-403b-a08b-1f5b8f6681cd` | human | 0.627 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9707a1c4-3b83-4ee9-96e8-3165ff2c83d5` | human | 0.423 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0a6a8f71-3ada-40d3-9bdd-ebd47da389a7` | unsure | 0.133 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `60a1f6ef-873f-4313-9306-9e34378ef232` | human | 0.544 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f17dc3da-4c8f-4195-b8ca-6e995a0d0908` | unsure | 0.253 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e95f26b8-1add-488c-984e-628ddb18afe1` | ai | 0.659 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `e51d7640-abbb-4469-a49a-538499b39952` | unsure | 0.225 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c4273d0e-9471-4203-8c53-acf8f8534c73` | unsure | 0.034 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `db4a784f-ce1d-4cbb-be85-cebeb4855feb` | unsure | 0.024 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `97c09223-559f-459e-ab86-11ea9a748a0f` | unsure | 0.094 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `5151dce3-ec52-4e91-8503-594d382d2727` | unsure | 0.099 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `34d70721-55b6-4709-89ea-1c8607e326c7` | unsure | 0.065 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `2d438df5-c876-4393-b9fd-50cdbec69a9b` | unsure | 0.078 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `4b932b58-4406-4dc3-b87f-b409ea89ee05` | human | 0.577 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e5c25e85-1c98-4741-b39f-0deebbfc5e6b` | human | 0.518 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7eaa7a0c-0653-4472-9410-0afedeb8fa10` | human | 0.749 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `47997c5e-a389-4aa9-8cc8-ff5f6eeea6ff` | unsure | 0.273 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0fc6381f-e561-4d3e-8b13-7351cd077813` | human | 0.419 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `3b9820b9-d782-4c54-b509-66360f96c195` | human | 0.340 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4f823b1d-af4e-4de3-aff9-dd6efe6ef867` | unsure | 0.266 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `893edb8e-7e25-443c-ab08-6ef91a214d61` | human | 0.640 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `1e09e26d-8ae3-4e42-b423-88ad2c931ac6` | unsure | 0.191 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `71239105-1ed1-464b-adb9-50f34a49c3d9` | unsure | 0.238 | HELD |
| MF06 | malformed | text is emoji only | 200 | `737b8353-1fac-46ec-bb90-61d7e49e79de` | ai | 0.598 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `ee57e7d7-9b14-48bd-a91d-231fedf2c297` | ai | 0.525 | HELD |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `db076041-2599-409f-9c7e-c0e210d13074` | human | 0.567 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3b7ca620-2a1a-431b-b9b3-3d9ac23a42e5` | human | 0.567 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8416cc5d-edd2-41bd-b827-c1bce2d2a051` | human | 0.567 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3716ded7-2789-4eec-9791-8f2e8ba02ca9` | human | 0.567 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a3694341-ef4d-40be-b5d9-1fec8f03aee7` | human | 0.567 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8e5926fc-0193-4f60-abaf-40b3a5b6d387` | human | 0.567 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4ab7a746-378d-4bf3-b454-5b969d06ab56` | human | 0.567 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d3167140-1602-49b7-a2ec-b545e0bdc13a` | human | 0.567 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47fa4a06-4b85-453f-8922-c59204800524` | human | 0.567 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `01b64f38-07ec-4bed-bcbf-bc2889b6459a` | human | 0.567 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

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
  "content_id": "52000f22-399b-46b6-ac41-e9eeef252972",
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
  "content_id": "4be0fdc7-a009-47de-9d29-0129f4c43bcd",
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
  "content_id": "f183804a-156e-42f1-9d2a-3e88973a790d",
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
  "content_id": "d858ed2a-88ff-4440-8650-d89ebe657759",
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
  "content_id": "20e2dc6e-70b1-403b-a08b-1f5b8f6681cd",
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
  "content_id": "9707a1c4-3b83-4ee9-96e8-3165ff2c83d5",
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
  "content_id": "0a6a8f71-3ada-40d3-9bdd-ebd47da389a7",
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
  "content_id": "60a1f6ef-873f-4313-9306-9e34378ef232",
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
  "content_id": "f17dc3da-4c8f-4195-b8ca-6e995a0d0908",
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
  "content_id": "e95f26b8-1add-488c-984e-628ddb18afe1",
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
  "content_id": "e51d7640-abbb-4469-a49a-538499b39952",
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
  "content_id": "c4273d0e-9471-4203-8c53-acf8f8534c73",
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
  "content_id": "db4a784f-ce1d-4cbb-be85-cebeb4855feb",
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
  "content_id": "97c09223-559f-459e-ab86-11ea9a748a0f",
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
  "content_id": "5151dce3-ec52-4e91-8503-594d382d2727",
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
  "content_id": "34d70721-55b6-4709-89ea-1c8607e326c7",
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
  "content_id": "2d438df5-c876-4393-b9fd-50cdbec69a9b",
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
  "content_id": "4b932b58-4406-4dc3-b87f-b409ea89ee05",
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
  "content_id": "e5c25e85-1c98-4741-b39f-0deebbfc5e6b",
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
  "content_id": "7eaa7a0c-0653-4472-9410-0afedeb8fa10",
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
  "content_id": "47997c5e-a389-4aa9-8cc8-ff5f6eeea6ff",
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
  "content_id": "0fc6381f-e561-4d3e-8b13-7351cd077813",
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
  "content_id": "3b9820b9-d782-4c54-b509-66360f96c195",
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
  "content_id": "4f823b1d-af4e-4de3-aff9-dd6efe6ef867",
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
  "content_id": "893edb8e-7e25-443c-ab08-6ef91a214d61",
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
  "content_id": "1e09e26d-8ae3-4e42-b423-88ad2c931ac6",
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
  "content_id": "71239105-1ed1-464b-adb9-50f34a49c3d9",
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
  "content_id": "737b8353-1fac-46ec-bb90-61d7e49e79de",
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
  "content_id": "ee57e7d7-9b14-48bd-a91d-231fedf2c297",
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
  "content_id": "db076041-2599-409f-9c7e-c0e210d13074",
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
  "content_id": "3b7ca620-2a1a-431b-b9b3-3d9ac23a42e5",
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
  "content_id": "8416cc5d-edd2-41bd-b827-c1bce2d2a051",
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
  "content_id": "3716ded7-2789-4eec-9791-8f2e8ba02ca9",
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
  "content_id": "a3694341-ef4d-40be-b5d9-1fec8f03aee7",
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
  "content_id": "8e5926fc-0193-4f60-abaf-40b3a5b6d387",
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
  "content_id": "4ab7a746-378d-4bf3-b454-5b969d06ab56",
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
  "content_id": "d3167140-1602-49b7-a2ec-b545e0bdc13a",
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
  "content_id": "47fa4a06-4b85-453f-8922-c59204800524",
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
  "content_id": "01b64f38-07ec-4bed-bcbf-bc2889b6459a",
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
