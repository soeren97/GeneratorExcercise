"""Script to run the main loop."""

from os import listdir, makedirs

from calculations import find_age
from src.cleaning import clean_phone_number
from src.data import generate_fake_dataset, save_dataset
from src.generators import apply_functions_to_large_file


def main(num_rows: int) -> None:
    """Run main loop.

    Args:
        num_rows (int): Desired number of rows in the fake dataset.
    """
    makedirs("Data", exist_ok=True)
    if "fakeData.csv" not in listdir("Data") or True:
        generator = generate_fake_dataset(num_rows)

        save_dataset(generator, "fakeData", num_rows)

    apply_functions_to_large_file(
        "fakeData.csv",
        [clean_phone_number, find_age],
        "cleanedNumbers",
        num_rows,
    )


if __name__ == "__main__":
    main(num_rows=10**5)
