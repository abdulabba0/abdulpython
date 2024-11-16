from datetime import datetime, timedelta
import random

def dummyDate(trans_start_date: tuple, trans_end_date:tuple, num_of_date:int) :
    """
    Generate some random dates

    Args:
        trans_start_date (tuple): the beginning date of the dummy transaction
        trans_end_date (tuple): the ending date of the dummy transaction
        num_of_date (int): how many dates to generate
    """
    # check if the provided number of dates is valid
    if num_of_date <= 0 :
        print("Invalid number of dates. Please enter a positive integer.")
        return
    else :
        # calculate the range of days between the start and end dates
        start_date = datetime(trans_start_date[0], trans_start_date[1], trans_start_date[2])
        end_date = datetime(trans_end_date[0], trans_end_date[1], trans_end_date[2])
        
        difference = end_date - start_date
        num_of_days = timedelta(days=int(difference.days))
        random_days = [random.randint(0, int(difference.days)) for x in range(num_of_date)]
        all_dates = [(start_date + timedelta(days=x)) for x in random_days]
        return all_dates
        
        
        