import json
from utils import load_file, create_dictionary


def main():
    with open("config.json", "r") as file:
        config = json.load(file)

    english_dictionary = create_dictionary(
        load_file(config["dictionary"]["english_path"])
    )

    business_dictionary = create_dictionary(
        load_file(config["dictionary"]["business_path"])
    )

    dictionary = english_dictionary | business_dictionary






if __name__ == "__main__":
    main()
