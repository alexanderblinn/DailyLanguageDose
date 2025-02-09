import csv
import random


class FileIsEmptyError(Exception):
    pass


class NumberOfColumnsError(Exception):
    pass


def get_random_entry(file_path: str) -> tuple[str, str, str, str, str]:
    """Reads a semicolon-separated CSV file and prints a random entry."""
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=";")
            rows = list(csv_reader)

            # Check if the file is empty
            if not rows:
                raise FileIsEmptyError("File is empty or doesn't contain data rows.")

            # Select a random row
            random_entry = random.choice(rows)

            # Validate the row structure
            if len(random_entry) != 5:
                raise NumberOfColumnsError(
                    "Selected row does not have the correct number of columns."
                )

            # Unpack and return the cleaned entry
            en, en_pron, de, en_phrase, de_phrase = map(str.strip, random_entry)
            return en, en_pron, de, en_phrase, de_phrase

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
