"""
Language detection starter.
"""

from pathlib import Path


if __name__ == "__main__":
    PATH_TO_LAB_FOLDER_ASSETS = Path(__file__).parent / "assets"
    PATH_TO_PROFILES_FOLDER = PATH_TO_LAB_FOLDER_ASSETS / "profiles"
    PATH_TO_DATASET_FOLDER = PATH_TO_LAB_FOLDER_ASSETS / "dataset"

    with open(PATH_TO_PROFILES_FOLDER / "eng.txt", "r", encoding="utf-8") as file_to_read:
        en_text = file_to_read.read()

    with open(PATH_TO_PROFILES_FOLDER / "de.txt", "r", encoding="utf-8") as file_to_read:
        de_text = file_to_read.read()

    with open(PATH_TO_PROFILES_FOLDER / "lat.txt", "r", encoding="utf-8") as file_to_read:
        lat_text = file_to_read.read()

    with open(
        PATH_TO_DATASET_FOLDER / "known_samples_de.txt", "r", encoding="utf-8"
    ) as file_to_read:
        de_samples = file_to_read.read().split("[TEXT]")[1:]

    with open(
        PATH_TO_DATASET_FOLDER / "known_samples_eng.txt", "r", encoding="utf-8"
    ) as file_to_read:
        eng_samples = file_to_read.read().split("[TEXT]")[1:]

    with open(
        PATH_TO_DATASET_FOLDER / "known_samples_lat.txt", "r", encoding="utf-8"
    ) as file_to_read:
        lat_samples = file_to_read.read().split("[TEXT]")[1:]

    with open(
        PATH_TO_DATASET_FOLDER / "unknown_samples.txt", "r", encoding="utf-8"
    ) as file_to_read:
        unknown_samples = file_to_read.read().split("[TEXT]")[1:]

    result = None
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert result, "Detection not working"
