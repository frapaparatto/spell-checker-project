from typing import Dict, List
from algorithms.damerau_levenshtein import damerau_levenshtein_distance


def query_tokenizer(query: str) -> List[str]:
    """Tokenize multi-word queries in single-word tokens.
    Separator: space.
    """
    return query.split()


def calculate_probability(word: str, words: Dict[str, int]) -> float:
    """Calculate the probability of each single word in the dictionary."""

    return words[word] / sum(words.values())


def suggest_correction(
    query: str, dictionary: Dict[str, int], max_distance: int
) -> str:
    """Main correction function."""

    if query in dictionary:
        return query

    candidates = []
    for word in dictionary:
        if abs(len(word) - len(query)) > max_distance:
            continue

        distance = damerau_levenshtein_distance(query, word)
        if distance <= max_distance:
            candidates.append((word, distance))

    if not candidates:
        return query

    min_distance = min(distance for _, distance in candidates)
    best_candidates = [
        word for word, distance in candidates if distance == min_distance
    ]

    return max(best_candidates, key=lambda x: calculate_probability(x, dictionary))
