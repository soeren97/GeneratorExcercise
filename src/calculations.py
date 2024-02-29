"""Calculations made on data to find new values."""

from typing import Any

from dateutil.parser import parse  # type: ignore[import-untyped]

from src.constants import NOW


def find_age(chunk: dict[str, Any]) -> dict[str, Any]:
    """Find the age of a person based on birth date.

    Args:
        chunk (dict[str, str]): The row that needs altering.

    Returns:
        dict[str, Any]: Altered row.
    """
    birth_date = chunk["birthdate"]
    birth_date = parse(birth_date)
    age = NOW - birth_date
    age_years = int(age.days / 365.25)

    chunk["Age"] = age_years

    return chunk
