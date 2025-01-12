"""
Variables, Data Types, and Basic Operations
1.	Write a program to swap two variables without using a third variable.
2.	Create a function that returns the count of each vowel in a given string.
3.	Write a program to determine if a given integer is even or odd without using the modulus operator.
4.	Implement a program that checks if a number is positive, negative, or zero.
5.	Write a function to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
6.	Write a program that calculates the compound interest.
7.	Create a function that takes a list of numbers and returns the largest even number.
8.	Write a program that finds the largest and smallest elements in a list without using built-in functions.
9.	Write a function to check if two given strings are anagrams.
10.	Create a program to convert a string containing a floating-point number into an integer without using built-in conversion functions.
"""

# "Q1"
# a = 5
# b = 10

# a = a + b  
# b = a - b 
# a = a - b  

# print("After swapping:")
# print("a =", a)  
# print("b =", b)  

# "Q2"

# "Q3"
# def check_even_odd(number):
#     if number & 1 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = 13
# result = check_even_odd(num)
# print(f"The number {num} is {result}.") 
# num = 8
# result = check_even_odd(num)
# print(f"The number {num} is {result}.")

# "Q4"
# def check_number(number):
#     if number > 0:
#         return "The number is positive."
#     elif number < 0:
#         return "The number is negative."
#     else:
#         return "The number is zero."

# num = float(input("Enter a number: "))
# result = check_number(num)
# print(result)

# "Q5"
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# celsius_temp = 25
# fahrenheit_temp = 77

# result_fahrenheit = celsius_to_fahrenheit(celsius_temp)
# print(f"{celsius_temp}°C is equal to {result_fahrenheit}°F")

# result_celsius = fahrenheit_to_celsius(fahrenheit_temp)
# print(f"{fahrenheit_temp}°F is equal to {result_celsius}°C")

# "Q6"

# "Q7"
# def largest_even_number(numbers):
#     even_numbers = [num for num in numbers if num % 2 == 0]

#     if even_numbers:
#         return max(even_numbers)
#     else:
#         return None

# numbers_list = [3, 7, 8, 12, 19, 22]
# result = largest_even_number(numbers_list)

# if result is not None:
#     print(f"The largest even number is: {result}")
# else:
#     print("There are no even numbers in the list.")

# "Q8"
# def find_largest_and_smallest(numbers):
    
#     largest = numbers[0]
#     smallest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num

#     return smallest, largest

# numbers_list = [5, 1, 9, -3, 7, 8]
# smallest, largest = find_largest_and_smallest(numbers_list)

# print(f"The smallest element is: {smallest}")
# print(f"The largest element is: {largest}")

# "Q9"
# def are_anagrams(str1, str2):

#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     if sorted(str1) == sorted(str2):
#         return True
#     else:
#         return False

# string1 = "Listen"
# string2 = "Silent"
# result = are_anagrams(string1, string2)

# if result:
#     print(f'"{string1}" and "{string2}" are anagrams.')
# else:
#     print(f'"{string1}" and "{string2}" are not anagrams.')

"Q10"

"""
Control Flow
11.	Implement a function to find the factorial of a number using recursion.
12.	Write a function that finds the nth Fibonacci number using both recursion and iteration.
13.	Create a program to simulate a simple calculator using conditional statements.
14.	Write a function that takes an integer and returns whether the number is prime.
15.	Create a program that finds all prime numbers within a given range.
16.	Write a function to check if a given year is a leap year.
17.	Create a function that checks if a string is a palindrome.
18.	Write a program that simulates the “FizzBuzz” challenge.
19.	Implement a program to print a multiplication table up to a given number.
"""
"Q11"
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# number = int(input("Enter a number: "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

"Q12"

"Q13"

"Q14"

"Q15"

"Q16"
# def is_leap_year(year):
   
#     if (year % 4 == 0 and year % 100 != 0) :
#         return True
#     else:
#         return False

# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

"Q17. Create a function that checks if a string is a palindrome."
# string = "level"
# if string == string[:-1] :
#     print(f"{string} is a palindrome")

"Q18. Write a program that simulates the “FizzBuzz” challenge."

"Q19. Implement a program to print a multiplication table up to a given number."

"20. Create a function that sorts a list of tuples based on the second element in each tuple."

"""Loops
21.	Write a program that reverses a given integer.
22.	Implement a program to count the number of digits in an integer.
23.	Write a function that takes a list and prints each element that appears more than once.
24.	Create a function that finds the missing number in a list of consecutive integers.
25.	Write a program to generate a random password of a given length.
26.	Create a program to print the first n terms of the harmonic series.
27.	Write a function that checks if all elements in a list are unique.
28.	Implement a function to find the frequency of elements in a list without using a dictionary.
29.	Create a program to generate a list of unique random integers within a specified range.
30.	Write a function that finds all the divisors of a given number.
"""
"Q21"
# number = 12345  

# is_negative = number < 0

# reversed_number = int(str(abs(number))[::-1])

# if is_negative:
#     reversed_number *= -1

# print(f"Reversed integer: {reversed_number}")

"Q22"

# number = 123456789

"""
Tuples
81.	Write a function that sorts a list of tuples by the second element.
82.	Create a function to reverse a tuple.
83.	Write a function to find the index of an element in a tuple.
84.	Implement a function to concatenate two tuples.
85.	Write a function to count the number of times an item appears in a tuple.
86.	Create a function to find the largest and smallest elements in a tuple.
87.	Write a function that returns a list of tuples containing the index and value of each element in a tuple.
88.	Implement a function to check if an element exists in a tuple.
89.	Write a function to convert a tuple to a string.
90.	Create a function to multiply all elements in a tuple.
"""
# 81
def sort_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
print(sort_second_element([(1, 3), (3, 2), (2, 1)]))

# 82
def reverse_tuple(tup):
    return tup[::-1]
print(reverse_tuple((1, 2, 3)))

#83
def find_index(tup, element):
    return tup.index(element)
print(find_index((1, 2, 3), 2))


# 84
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2
print(concatenate_tuples((1, 2), (3, 4)))

# 85
def count_item(tup, item):
    return tup.count(item)
print(count_item((1, 2, 2, 3), 2))

# 86
def largest_and_smallest(tup):
    return max(tup), min(tup)
print(largest_and_smallest((1, 2, 3)))

# 87
# def index_value_pairs(tup):
#     return list((tup))

# 88 
def element_exists(tup, element):
    return element in tup
print(element_exists((1, 2, 3), 2))

# 89 Write a function to convert a tuple to a string
def tuple_to_string(tup):
    return ''.join(map(str, tup))
print(tuple_to_string((1, 2, 3)))

# 90 Create a function to multiply all elements in a tuple
def multiply_elements(tup):
    result = 0
    for element in tup:
        result *= element
    return result
print(multiply_elements((1, 2, 3)))