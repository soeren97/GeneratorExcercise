"""DAta generation script."""

import csv
from multiprocessing import Pool
from typing import Any, Generator

from tqdm import tqdm

from src.constants import fake


def create_fake_row(_: Any) -> dict[str, Any]:
    """Create a single fake row.

    Args:
        _ (Any): Variable used for imap.

    Returns:
        dict[str, Any]: Fake Row.
    """
    profile: dict[str, Any] = fake.profile()
    profile["Phone"] = fake.phone_number()
    return profile


def generate_fake_dataset(
    num_rows: int,
) -> Generator[dict[str, str], None, None]:
    """Create generator for making dataset.

    Args:
        num_rows (int): Number of desired row in dataset.

    Yields:
        Generator[list[str, str], None, None]: Fake row generator.
    """
    with Pool() as pool:
        rows = pool.imap_unordered(create_fake_row, range(num_rows))
        for row in rows:
            yield row


def save_dataset(
    iterator: Generator[dict[str, str], None, None],
    name: str,
    num_rows: int,
) -> None:
    """Save the dataset iterativly.

    Args:
        iterator (Generator[list[str, str], None, None]): Row generator.
        name (str): File name.
        num_rows (int): Desired number of rows.
    """
    fake_row = create_fake_row(None)
    with open(f"Data/{name}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(fake_row.keys())

        # Write rows
        for row in tqdm(iterator, total=num_rows, desc=f"Creating {name}.csv"):
            csv_writer.writerow(row.values())
