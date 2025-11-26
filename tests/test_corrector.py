import unittest
from typing import List

from corrector import query_tokenizer, suggest_correction


class TestCorrector(unittest.TestCase):
    def setUp(self) -> None:
        self.dictionary = {
            "hello": 100,
            "world": 80,
            "hallo": 10,
            "help": 60,
            "held": 40,
            "sales": 150,
            "report": 200,
        }

    def test_tokenize_single_word_query(self):
        result = query_tokenizer("suggestion")

        self.assertIsInstance(result, List)

    def test_tokenize_multi_words_query(self):
        result = query_tokenizer("sales report")

        self.assertIsInstance(result, List)
        self.assertListEqual(result, ["sales", "report"])

    def test_correct_query_returns_same_word(self):
        result = suggest_correction("hello", self.dictionary, max_distance=2)

        self.assertEqual(result, "hello")

    def test_same_distance_chooses_higher_probability(self):
        result = suggest_correction("helo", self.dictionary, max_distance=2)

        self.assertEqual(result, "hello")


if __name__ == "__main__":
    unittest.main()
