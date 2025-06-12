import random


def get_numbers_ticket(min:int, max:int, quantity:int)-> list[int]:
    """
    Function retern list of random numbers from range [min, max] with quantity elements

    Args:
        min (int): Minimum value of the range, must be at least 1.
        max (int): Maximum value of the range, must not exceed 1000.
        quantity (int): Number of elements in the list, must be at least 1 and not more than (max - min).
    Returns:
        list[int]: A sorted list of unique random numbers if input parameters are valid, otherwise an empty list.
    """   
    if not all(isinstance(arg, int) for arg in [min, max, quantity]):
        return []
    if min < 1 or max > 1000 or 1 <= quantity  > (max - min ):
        # Invalid input parameters. Please ensure 1 <= min < max <= 1000 and quantity is within the range.
        return []
    else:
        # Generate a sorted list of unique random numbers
        return sorted(random.sample(range(min, max + 1), quantity))

