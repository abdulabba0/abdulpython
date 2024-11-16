from datetime import datetime, timedelta
import random

def dummyDate(trans_start_date: tuple, trans_end_date: tuple, num_of_date: int):
    """
    Generate a list of random dates within a given date range.

    Args:
        trans_start_date (tuple): The beginning date of the dummy transaction.
        trans_end_date (tuple): The ending date of the dummy transaction.
        num_of_date (int): how many dates to generate.

    Returns:
        Tuple: A list of randomly generated date.
    """

    if num_of_date <= 0:
        print("Invalid number of dates. Please enter a positive integer.")
        return
    start_date = datetime(trans_start_date[0], trans_start_date[1], trans_start_date[2])
    end_date = datetime(trans_end_date[0], trans_end_date[1], trans_end_date[2])
    if start_date > end_date:
        print("Start date must be earlier than end date.")
        return

    difference = (end_date - start_date).days
    random_dates = [(start_date + timedelta(days=random.randint(0, difference))).strftime("%Y-%m-%d") for _ in range(num_of_date)]
    return random_dates

trans_start_date = (2024, 1, 1)
trans_end_date = (2024, 12, 31)
num_of_date = 100  

random_dates_list = dummyDate(trans_start_date, trans_end_date, num_of_date)
print("Generated random dates list:")
print(random_dates_list)
