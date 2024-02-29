"""Functions for processing large datasets."""

import csv
from typing import Any, Callable, Generator

import pandas as pd
from tqdm import tqdm


def read_rows(name: str) -> Generator[pd.Series, None, None]:
    """Read rows of a large file iteratively.

    Args:
        name (str): Name of the large file.

    Yields:
        Generator[pd.Series, None, None]: A row from the large file.
    """
    with open(f"Data/{name}", "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)

        # Skip first row
        column_names = next(csv_reader)

        # Iterate over the remaining rows
        for row in csv_reader:
            yield pd.Series(row, index=column_names)


def apply_functions_to_large_file(
    filename: str,
    func_list: list[Callable[[dict[str, Any]], dict[str, Any]]],
    name: str,
    num_rows: int,
) -> None:
    """Apply a list of functions to a large file.

    Args:
        filename (str): Name of the file to be modified.
        func_list (list[Callable[[dict[str, str]], str]]): Functions.
        name (str): Name of save file.
        num_rows (int): Total number of rows in the large file.
    """
    generator = read_rows(filename)

    with open(f"Data/{name}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Process and write header
        header_written = False
        for row in tqdm(
            generator,
            total=num_rows,
            desc="Cleaning and processing data",
        ):
            if not header_written:
                csv_writer.writerow(row.index)
                header_written = True

            # Apply functions and write processed row
            for func in func_list:
                row = func(row)
            csv_writer.writerow(row.tolist())
