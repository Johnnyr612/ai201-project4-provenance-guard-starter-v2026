"""
Inputs for the five Milestone 3 criteria.

Criterion 1 and Criterion 2's "own_writing" group must be the student's own
writing. They are left as "REPLACE ME" placeholders on purpose: `validate()`
rejects them, so the evaluation will not run until real personal writing is
pasted in. Anything an AI drafts there would not measure the false-positive
rate on human writing.

Criterion 2's "ai_written" group and Criterion 3's inputs were written by an
AI assistant (Claude) for this evaluation. Criterion 3's inputs were checked
locally against the pipeline before use (model / style / repetition -> score):
  0 casual human-style note   0.178 / 0.000 / 0.000 -> 0.071 human
  1 generic AI paragraph      0.943 / 0.409 / 0.000 -> 0.541 unsure
  2 repetitive AI paragraph   0.950 / 0.770 / 0.319 -> 0.751 ai
"""

SCENARIOS = [
    {
        "name": "own-writing false positives",
        "criterion": 1,
        "target": "No more than 1 of 10 labeled high-confidence AI",
        "source_note": "Ten original rough notes written by the student.",
        "texts": [
            "i needed money to pay rent so i got a job to pay the bills",
            "I like pizza because its cheap and fills me up.",
            "I don't like commuting to school when it's really busy outside",
            "I am learning how to finish hw assignments fast",
            "I like the spider-man movies because they show a lot of action.",
            "I have to wake up and go to work 5x a week, I wish I only worked 3 hours a day",
            "ai helps alot, and restrictions on ai annoy me becuase if ai can do a lot of our busy work, why don't we let it do it.",
            "I received a bonus at work that helped me pay for more bills",
            "i am working on a website that will hopefully generate me passive income in the future",
            "good work ethic translates to reaching goals better and resiliently",
        ],
    },
    {
        "name": "model-score separation",
        "criterion": 2,
        "target": "AI median at least 0.15 above own-writing median",
        "source_note": (
            "Indices 0-4: the student's own writing. "
            "Indices 5-9: AI-written by Claude for this evaluation."
        ),
        "groups": {
            "own_writing": [0, 1, 2, 3, 4],
            "ai_written": [5, 6, 7, 8, 9],
        },
        "texts": [
            "i needed money to pay rent so i got a job to pay the bills",
            "I like pizza because its cheap and fills me up.",
            "I don't like commuting to school when it's really busy outside",
            "I am learning how to finish hw assignments fast",
            "I like the spider-man movies because they show a lot of action.",
            'Effective communication is essential in any workplace. Clear communication helps teams share information, solve problems, and work toward common goals. When team members communicate well, they can avoid misunderstandings and build trust. Managers play an important role in creating a culture of open communication. By encouraging feedback and listening carefully, they can help their teams succeed. In conclusion, effective communication is a key factor in the success of any organization.',
            'Climate change is one of the most important issues facing the world today. Rising temperatures can affect weather patterns, food production, and human health. Many countries are working to reduce greenhouse gas emissions and invest in renewable energy. Individuals can also make a difference by reducing waste and using energy more efficiently. By working together, we can help protect the planet for future generations.',
            'Reading is an important skill that offers many benefits. It helps people learn new information, improve their vocabulary, and develop critical thinking skills. Reading can also reduce stress and provide a way to relax after a long day. For children, reading at an early age can support success in school. Overall, reading is a valuable habit that can improve many areas of life.',
            'Social media has changed the way people connect with each other. It allows users to share ideas, stay in touch with friends, and access news quickly. However, social media can also have negative effects, such as the spread of misinformation and increased feelings of anxiety. It is important for users to think carefully about how they use these platforms. By using social media in a balanced way, people can enjoy its benefits while reducing its risks.',
            'Healthy eating is an important part of a healthy lifestyle. A balanced diet includes fruits, vegetables, whole grains, and lean proteins. Eating a variety of foods helps the body get the nutrients it needs to function properly. It is also important to drink enough water and limit foods that are high in sugar and salt. By making small changes to their diet, people can improve their health and well-being.',
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "target": "All 3 labels in every trial",
        "source_note": (
            "Index 0 aims for human (informal, uneven sentences, heavy punctuation); "
            "index 1 for unsure (generic AI prose: high model score, mid style score); "
            "index 2 for ai (generic AI prose with repeated phrasing and even sentences)."
        ),
        "texts": [
            'ok so the 6:40 train?? cancelled. again. stood on platform 3 w/ about 200 other ppl, all of us glaring at the board like it owed us money -- which, tbh, it kinda does. Got a coffee (bad), a croissant (worse), then finally a 7:25 that crawled into town at 8:50. Missed standup. Boss: "no worries!" Me: dying inside.',
            'Healthy eating is an important part of a healthy lifestyle. A balanced diet includes fruits, vegetables, whole grains, and lean proteins. Eating a variety of foods helps the body get the nutrients it needs to function properly. It is also important to drink enough water and limit foods that are high in sugar and salt. By making small changes to their diet, people can improve their health and well-being.',
            'It is important to note that effective time management is important for students. It is important to set clear goals and it is important to plan each day. It is important to review progress and it is important to make changes when needed. When students manage their time well, they can reach their goals. When students manage their time well, they can reduce stress. When students manage their time well, they can improve their results. In the end, effective time management is important for students and it is important for their future success.',
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "target": "Valid appeal recorded; unknown appeal rejected and not logged",
        "appeals": {
            "text": "I am submitting this short sample to verify that an appeal is recorded without replacing the original decision.",
            "reasoning": "I would like a person to review this decision.",
        },
    },
    {
        "name": "invalid text and service availability",
        "criterion": 5,
        "target": "Four invalid requests return 4xx; health remains 200",
        "health_check": True,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "x" * 10_001, "creator_id": "eval_bad_long"},
        ],
    },
]


def validate() -> list[str]:
    """Complain about malformed scenarios before a long evaluation run."""
    problems = []
    seen_criteria = set()

    for i, scenario in enumerate(SCENARIOS, 1):
        name = scenario.get("name")
        if not name:
            problems.append(f"scenario {i} has no name")

        criterion = scenario.get("criterion")
        if criterion in seen_criteria:
            problems.append(f"criterion {criterion} is used more than once")
        if criterion is not None:
            seen_criteria.add(criterion)

        kinds = sum(bool(scenario.get(key)) for key in ("texts", "bodies", "appeals"))
        if kinds != 1:
            problems.append(
                f"scenario {i} ('{name}') must have exactly one of texts, bodies, or appeals"
            )
            continue

        if scenario.get("texts"):
            for j, text in enumerate(scenario["texts"], 1):
                if not isinstance(text, str) or not text.strip():
                    problems.append(f"scenario {i}, text {j} must be a non-empty string")
                elif text.startswith("REPLACE ME"):
                    problems.append(f"scenario {i}, text {j} is still a placeholder")

        if scenario.get("bodies"):
            for j, body in enumerate(scenario["bodies"], 1):
                if not isinstance(body, dict):
                    problems.append(f"scenario {i}, body {j} is not a dict")

        if scenario.get("appeals"):
            appeal = scenario["appeals"]
            if not isinstance(appeal.get("text"), str) or not appeal["text"].strip():
                problems.append(f"scenario {i} appeal text must be non-empty")
            if not isinstance(appeal.get("reasoning"), str) or not appeal["reasoning"].strip():
                problems.append(f"scenario {i} appeal reasoning must be non-empty")

    missing_criteria = sorted(set(range(1, 6)) - seen_criteria)
    if missing_criteria:
        problems.append(f"missing criteria: {', '.join(map(str, missing_criteria))}")
    return problems
