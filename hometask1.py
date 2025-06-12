from datetime import datetime
from typing import Optional


def get_days_from_today(date: str) -> Optional[int]:
    """
    Function return  the number of days from today to a given date.

    Args:
        date (str): Date in 'YYYY-MM-DD' forma.
    Returns:
        Optional[int]: The difference in days between the current date and the set date (date)
            - Positive if date is in the past,
            - Negative if in the future,
            - None if date is not a valid 'YYYY-MM-DD'.
    """
    try:
        # Parse the input date string into a datetime object
        date_input = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError , TypeError):
        # Parameter data must be a string in the format YYYY-MM-DD")
        return None
    # Get today date
    date_today = datetime.today().date()
    return (date_today - date_input).days    

