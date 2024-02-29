"""Cleaning functions to clean data."""

import re


def clean_phone_number(chunk: dict[str, str]) -> dict[str, str]:
    """Remove extensions and standardise phone numbers.

    Args:
        chunk (dict[str, str]): The row that needs altering.

    Returns:
        dict[str, str]: Cleaned row.
    """
    cleaned_number = chunk["Phone"]
    # Handle extension (x followed by five digits) at the end
    match_extension = re.search(r"x(\d{1,5})$", cleaned_number)
    if match_extension:
        cleaned_number = cleaned_number[: match_extension.start()]

    if cleaned_number.startswith("+1"):
        cleaned_number = cleaned_number[2:]

    # Remove non-numeric characters
    cleaned_number = re.sub(r"\D", "", cleaned_number)

    # Handle country code "001" at the beginning
    if cleaned_number.startswith("001") and len(cleaned_number) == 13:
        cleaned_number = cleaned_number[3:]

    # Remove country code if present (assuming 10-digit US numbers)
    if len(cleaned_number) == 11 and cleaned_number.startswith("1"):
        cleaned_number = cleaned_number[1:]

    chunk["Phone"] = cleaned_number

    return chunk
