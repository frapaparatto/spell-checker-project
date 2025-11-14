import re
import os
from collections import Counter
from typing import Dict


def load_file(filepath: str) -> str:
    if not filepath or not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")

    with open(filepath, "r") as file:
        return file.read()


def create_dictionary(text: str) -> Dict[str, int]:
    """Create a dictionary of word with their frequencies from a text file."""
    words = re.findall(r"\w+", text.lower())  # list of words

    # return a dictionary with the count of all occurrences of each word
    return Counter(words)
