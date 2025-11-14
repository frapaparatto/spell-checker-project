from typing import Dict, List

def query_tokenizer(query: str) -> List[str]:
    """Function for handling multi-word queries"""
    ...

def calculate_probability(word: str, words: Dict[str, int]) -> float:
    """Function for calculating the probability of each word"""
    ...

def suggest_correction(query: str, dictionary: Dict[str, int]) -> str:
    """Function for correcting the user query"""
    ...



