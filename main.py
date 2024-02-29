"""Script to run the main loop."""

import cProfile
from os import listdir, makedirs

from src.calculations import find_age
from src.cleaning import clean_phone_number
from src.data import create_dataset
from src.generators import apply_functions_to_large_file


def main(num_rows: int, debug: bool = False) -> None:
    """Run main loop.

    Args:
        num_rows (int): Desired number of rows in the fake dataset.
        debug (bool): Activates debug mode. (Profiler and generate new dataset.)
    """
    makedirs("Data", exist_ok=True)
    if "fakeData.csv" not in listdir("Data") or debug:
        if not debug:
            create_dataset("fakeData", num_rows)
        else:
            cProfile.run(f"create_dataset('fakeData', {num_rows})", sort="cumulative")

    if not debug:
        apply_functions_to_large_file(
            "fakeData.csv",
            [clean_phone_number, find_age],
            "cleanedNumbers",
            num_rows,
        )
    else:
        cProfile.run(
            f"""apply_functions_to_large_file(
                'fakeData.csv',
                [clean_phone_number, find_age],
                'cleanedNumbers',
                {num_rows},
                )
                """,
            sort="cumulative",
        )


if __name__ == "__main__":
    main(num_rows=10**5)
