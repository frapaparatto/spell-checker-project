import re
import os
from collections import Counter
from typing import Dict


def load_file(filepath: str) -> str:
    if not filepath or not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")

    with open(filepath, "r") as file:
        file = file.read()

    if not file:
        # TODO: understand if there are more appropriate exceptions class to handle that
        raise ValueError("The file is empty")

    return file


def create_dictionary(text: str) -> Dict[str, int]:
    """Create a dictionary of word with their frequencies from a text file."""
    words = re.findall(r"\w+", text.lower())  # list of words

    # return a dictionary with the count of all occurrences of each word
    return Counter(words)


def get_max_distance(len_query: int, config: Dict) -> int:
    """Use different values for the max edit distance based on the length of the word"""
    return (
        config["algorithm"]["max_distance_long"]
        if len_query >= 4 
        else config["algorithm"]["max_distance_short"]
    )
