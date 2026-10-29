"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three surface-text measures are combined into a 0–1 score. Their scales and
weights are simple heuristics, not validated authorship probabilities.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      punctuation marks per word

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── Surface-text measures ────────────────────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, relative to the mean sentence length.

    Returns the sample standard deviation divided by mean word count.
    Fewer than two non-empty sentences returns 0.0.
    """
    lengths = [len(words(sentence)) for sentence in sentences(text)]
    lengths = [length for length in lengths if length > 0]
    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)
    if mean_length == 0:
        return 0.0
    return round(statistics.stdev(lengths) / mean_length, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    return round(len(set(tokens)) / len(tokens), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to the number of words.

    Returns:
        A float. All non-alphanumeric, non-whitespace characters count as
        punctuation, including sentence-ending marks.
    """
    token_count = len(words(text))
    if token_count == 0:
        return 0.0
    punctuation_count = sum(
        1 for char in text if not char.isalnum() and not char.isspace()
    )
    return round(punctuation_count / token_count, 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Low sentence-length variation, lower vocabulary variety, and lower
         punctuation density each contribute toward an AI-like score.
      2. Each measure is normalized to 0–1 before averaging. These simple
         cutoffs are heuristic, not validated authorship probabilities.

    Test it on clearly AI, clearly human, formal human, and lightly edited AI
    examples before you trust it. These scores remain surface-text heuristics.
    """
    spread = sentence_length_spread(text)
    vocabulary_variety = type_token_ratio(text)
    punctuation = punctuation_density(text)

    spread_score = 1.0 - min(spread / 0.8, 1.0)
    vocabulary_score = 1.0 - min(
        max((vocabulary_variety - 0.35) / 0.45, 0.0),
        1.0,
    )
    punctuation_score = 1.0 - min(punctuation / 0.3, 1.0)

    return round(
        0.45 * spread_score
        + 0.45 * vocabulary_score
        + 0.10 * punctuation_score,
        4,
    )


def repetition_signal(text: str) -> float:
    """Score repeated three-word phrases from 0 (few) to 1 (many)."""
    tokens = words(text)
    if len(tokens) < 3:
        return 0.0

    trigrams = [
        tuple(tokens[index:index + 3])
        for index in range(len(tokens) - 2)
    ]
    repeated_fraction = (len(trigrams) - len(set(trigrams))) / len(trigrams)
    return round(repeated_fraction, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print(f"repetition_signal        {repetition_signal(text)}   (higher = more repeated phrases)")
    print("\nThese are surface-text heuristics, not proof of authorship.")
