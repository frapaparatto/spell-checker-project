from typing import Dict, List

def query_tokenizer(query: str) -> List[str]:
    """Tokenize multi-word queries in single-word tokens."""
    ...

def calculate_probability(word: str, words: Dict[str, int]) -> float:
    """Calculate the probability of each single word in the dictionary."""
    ...

def suggest_correction(query: str, dictionary: Dict[str, int]) -> str:
    """Main correction function."""
    ...



