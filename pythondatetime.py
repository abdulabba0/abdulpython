from datetime import datetime, timedelta
from transactionModel import dummyDate
""" 
Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""
# Getting the current date and time
# today = datetime.now()
# print(f"Year : {today.year}")
# print(f"Month : {today.month}")
# print(f"day : {today.day}")
# print(f"hour : {today.hour}")
# print(f"minute : {today.minute}")
# print(f"seconds : {today.second}")
# print(f"miroseconds : {today.microsecond}")

# #Creating a date object
# # 2024:10:3
# # 2024/10/3
# # 2024-10-3
# # January 10 2004
# # Jan 10 2004
# date_obj = datetime(2022, 1, 1, 20, 34, 10)

# today = datetime.now()

# # getting the day of the week
# print(today.strftime("%a"))
# print(today.strftime("%A"))
# print(today.strftime("%w"))

# # getting the day of the month
# print(today.strftime("%d"))

# # getting the month name

# print(today.strftime("%b"))
# print(today.strftime("%B"))
# print(today.strftime("%m"))

# # getting the year
# print(today.strftime("%y"))
# print(today.strftime("%Y"))

# # getting the hour
# print(today.strftime("%H"))
# # Sunday November 2024
# print(today.strftime("%A %B %Y"))
# # Sunday Nov 24 20:10:10
# print(today.strftime("%A %b %y %H:%M:%S"))

# # Finding the difference between two date
# old_date = datetime(2020, 1, 1)
# new_date = datetime(2024, 1, 1)

# res = new_date - old_date
# print(res.days)

# # using timedelta
previous_date = datetime.now()
# we want to check date of the last hundred days
last_hundred_days = previous_date - timedelta(days=100)
print(last_hundred_days)
# generate a dummy transaction database, generate dummy date and dummy transaction ammount

dates = dummyDate((2023, 1, 1), (2024, 11, 1), 100)
print(dates[0])