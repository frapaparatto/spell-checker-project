import cProfile
import sys
import json
import pstats
from utils import load_file, create_dictionary, get_max_distance, load_config
from corrector import suggest_correction, query_tokenizer


def main():
    try:
        config = load_config("./config.json")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)

        sys.exit()

    try:
        english_dictionary = create_dictionary(
            load_file(config["dictionary"]["english_path"])
        )
    except (ValueError, FileNotFoundError) as e:
        print(f"Error loading English dictionary: {e}")
        sys.exit()

    try:
        business_dictionary = create_dictionary(
            load_file(config["dictionary"]["business_path"])
        )
    except (ValueError, FileNotFoundError) as e:
        print(f"Error loading business dictionary: {e}")
        sys.exit()

    dictionary = english_dictionary | business_dictionary

    while True:
        research_query = input("Search (or 'quit' to exit): ").strip().lower()

        if research_query == "quit":
            print("Exiting")
            sys.exit()

        if research_query:
            break

        print("\nPlease, insert a search query.")

    with cProfile.Profile() as profile:
        suggestions = [
            # max_distance parameter will be 1 if the query contains less than 4 chars, else 2
            suggest_correction(
                query.strip(),
                dictionary,
                max_distance=get_max_distance(len(query), config),
            )
            for query in query_tokenizer(research_query)
            if query
        ]

        print(" ".join(suggestions))

    stats = pstats.Stats(profile).sort_stats(pstats.SortKey.TIME)
    # print stats only for modules that contains those name patterns
    stats.print_stats("corrector|utils|algorithms|main")


if __name__ == "__main__":
    main()
