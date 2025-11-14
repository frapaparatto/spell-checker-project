import json
import cProfile
import pstats
from utils import load_file, create_dictionary
from corrector import suggest_correction, query_tokenizer


def main():
    # TODO: evaluate to create an helper function also for getting config files in order to handle JsonDecodeError
    with open("config.json", "r") as file:
        config = json.load(file)

    with cProfile.Profile() as profile:
        try:
            english_dictionary = create_dictionary(
                load_file(config["dictionary"]["english_path"])
            )

            business_dictionary = create_dictionary(
                load_file(config["dictionary"]["business_path"])
            )
        except FileNotFoundError as e:
            print(e)

        else:
            dictionary = english_dictionary | business_dictionary
            research_query = input("Search: ").strip().lower()

            suggestions = [
                suggest_correction(query, dictionary, max_distance=2)
                for query in query_tokenizer(research_query)
                if query
            ]

            print(" ".join(suggestions))

    stats = pstats.Stats(profile).sort_stats(pstats.SortKey.TIME)
    stats.print_stats("corrector|utils|algorithms|main")


if __name__ == "__main__":
    main()
