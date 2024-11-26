import random 
"""
General Questions
•	Write a Python program that takes a list of numbers and returns a list containing only the even numbers.
•	Write a Python program that takes two numbers from the user and prints their sum, difference, product, and quotient.
•	Write a Python program that checks if a given string is a palindrome (reads the same backward as forward).
•	Write a Python program that prints the first 10 Fibonacci numbers.
•	Write a Python program that takes a list of numbers and returns the largest number using a loop.
"""
# Q1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_num = [x for x in a if x % 2 == 0] 
# print(even_num)

# even_list = []
# for x in a :
#     if x % 2 == 0 and x != 0 :
#         even_list.append(x)

# print(f"even list : {even_list}")

# #Q2
# b = 1
# c = 3
# print(b + c)
# print(b - c)
# print(b * c)
# print(b / c)
      
#Q3
# strings = "level"

# if strings == strings[::-1] :
#     print(f"{strings} is a pallindrome")
# else :
#     print(f"{strings} is not a pallindrome")

#Q4
"""
Fibonacci numbers are number in which addition of the last two numbers is the next
1, 2, 3, 5, 8, 13, 21, 21, 34, 55
"""
# fib_list = [1, 2]

# for x in range(2, 12) :
#     first_prev = fib_list[x - 1]
#     second_prev = fib_list[x - 2]
#     next = first_prev + second_prev
#     fib_list.append(next)

# print(fib_list)


# # Q5
# numbers = [3, 6, 8, 1, 2, 9, 4, 5, 7, 1]
# big_num = numbers[1]
# for x in numbers:
#     if x > big_num:
#         big_num = x
# print(x)

"""
•	Write a Python program that takes a list of numbers and returns a list containing only the even numbers.
•	Write a Python program that takes two numbers from the user and prints their sum, difference, product, and quotient.
•	Write a Python program that checks if a given string is a palindrome (reads the same backward as forward).
•	Write a Python program that prints the first 10 Fibonacci numbers.
•	Write a Python program that takes a list of numbers and returns the largest number using a loop.
"""

"Q1"
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_num = [x for x in a if x % 2 == 0] 
# print(even_num)

"Q2"
# a = 1
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a % b)
# print(a / b)
# print(a // b)

"Q3"
# string = "bob"
# if string == string[::-1] :
#     print("This is a palindrome")

"Q4"
# a = [3, 5, 2, 7, 9, 3, 6, 7]
# b = "THIS IS THE WOLRD"
# print(b.lower())

"""
Question 1: Sum of Array Elements
Write a program to calculate the sum of all elements in an array using a for loop.
Input:
Array: [1, 2, 3, 4, 5]
Output:
Sum: 15

Question 2:
Here are three algorithm questions for working with for loops suitable for beginners:
Question 1: Sum of Array Elements
Write a program to calculate the sum of all elements in an array using a for loop.
Input:
Array: [1, 2, 3, 4, 5]
Output:
Sum: 15
Question 3: Find the Maximum Value
Write a program to find the maximum value in an array using a for loop.
Input:
Array: [10, 25, 3, 45, 12]
Output:
Maximum Value: 45
"""

# Q1
# array = [1, 2, 3, 4, 5]

# sum = 0
# for num in array :
#     sum += num

# print("sum:", {sum})

# Q2
# array = [10, 25, 3, 45, 12]
# max_value = [0]

# for num in array :
#     if num > max_value[0] :
#         max_value[0] = num

# print(max_value)

"""
1.	Use the following string method and print out the result
islower()       Returns True if all characters in the string are lower case
isnumeric()     Returns True if all characters in the string are numeric
isprintable()   Returns True if all characters in the string are printable
isspace()       Returns True if all characters in the string are whitespaces
istitle()       Returns True if the string follows the rules of a title
isupper()       Returns True if all characters in the string are upper case
join()          Joins the elements of an iterable to the end of the string
lower()         Converts a string into lower case
replace()       Returns a string where a specified value is replaced with a specified value
splitlines()    Splits the string at line breaks and returns a list
startswith()    Returns true if the string starts with the specified value
strip()         Returns a trimmed version of the string
swapcase()      Swaps cases, lower case becomes upper case and vice versa
title()         Converts the first character of each word to upper case
upper()         Converts a string into upper case

2.	You are been hired by a company to help them reformat some phone number that was wrongly inserted into their database, the format of these phone number is this: 720-376-4918, create a list containing 2 0f this number, then use string method to reformat them to something like this +2347203764918

3.	20 student register their interest to participate in the school annual excursion, only 4 student can go, write a program to select 4 students from a list of 20 student
"""
# Q1
# a = "student"
# print(a.islower())

# b = "23"
# print(b.isnumeric())

# c = "student"
# print(c.isprintable())

# d = "     "
# print(d.isspace())

# e = "Student"
# print(e.istitle())

# f = "STUDENT"
# print(f.isupper())

# g = "file"
# o = ["1", "2", "3", "4"]
# print(g.join(o))

# r = "STUDENT"
# print(r.lower())

# h = "student"
# y = "sign"
# print(h.replace(y))

# i = "student"
# print(i.splitlines())

# j = "student"
# print(j.startswith("stu"))

# k = "student"
# print(k.strip("st"))

# l = "STudENt"
# print(l.swapcase())

# q = "student"
# print(q.title())

# w = "student"
# print(w.upper())

# Q2
# let's create the number
# wrongly_formatted_num = []

# for _ in range(30) :
#     num_append1 = [str(x) for x in random.choices([1,2,3,4,5,6,7,8,9,0], k=3)]
#     num_append2 = [str(x) for x in random.choices([1,2,3,4,5,6,7,8,9,0], k=3)]
#     num_append3 = [str(x) for x in random.choices([1,2,3,4,5,6,7,8,9,0], k=3)]
   
#     num1 = "".join(num_append1) + "-" + "".join(num_append2) + "-" + "".join(num_append3)
#     wrongly_formatted_num.append(num1)
    
# # reformat the numbers
# formatted_nums = []
# for x in wrongly_formatted_num:
#     pres_string = "+234"
#     for i in x :
#         if i != "-":
#             pres_string += i
#     formatted_nums.append(pres_string)

# print(formatted_nums)

# Q3
# students = random.choices(["sani", "musa", "racheal", "abdul", "rach", "tear", "buba", "isah"], k =4)

# print(students)

"""
1.	Remove duplicate item from this list [4, 5, 6, 3, 5, 6, 7, 8, 4, 5, 6, 7, 7, 6, 7]
2.	Create an empty list multiply all even number in the list by 4 and add them including the odd number inside the empty list
3.	Given set a = {5, 3, 4, 9, 12, 45, 15, 45, 78, 89} set b = {3, 4, 6, 7, 9, 12, 34, 45, 90, 10} and set c = {23, 56, 12, 4, 5, 6, 4, 7}
a.	Find the intersect of set a and b (a | b)
b.	Find the union of set a, b and c (a & b & c)
c.	Find the union of set a and c (a & c)
d.	Find the intersect of set a, b and c (a | b | c)
e.	Find the difference of set a and b (a - b)
f.	Find the difference of set a, b and c (a - b - c)
4.	Given this dictionary below
a.	Sum up all the first Test
b.	Calculate the mean score of the Total
 C = { "firstTest" : (12, 15, 15, 15, 15, 15, 12, 12, 12, 11, 12, 12, 11, 12, 15, 12, 15, 11, 12),
"practical" : [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
"exam" :  (65, 65, 55, 65, 70, 70, 60, 43, 46, 36, 48, 39, 65, 30, 65, 41, 55, 70, 45),
"Total" :  [92, 95, 85, 95, 100, 100, 87, 70, 73, 62, 75, 66, 91, 57, 95, 68, 85, 96, 72], } 
"""
# Q1
# a = [{4, 5, 6, 3, 5, 6, 7, 8, 4, 5, 6, 7, 7, 6, 7}]
# print(a)

# # Q2
# numbers = [1, 2, 3, 4, 5]
# empty_list = []

# for x in numbers:
#     if x % 2 == 0 :
#         empty_list.append(x * 4)
#     else :
#         empty_list.append(x)
# print(empty_list)

# Q3
# a = {5, 3, 4, 9, 12, 45, 15, 45, 78, 89}
# b = {3, 4, 6, 7, 9, 12, 34, 45, 90, 10}
# c = {23, 56, 12, 4, 5, 6, 4, 7}
# print(a | b)
# print(a & b & c)
# print(a & c)
# print(a | b | c)
# print(a - b)
# print(a - b - c)

# Q4
# dict = { "firstTest" : (12, 15, 15, 15, 15, 15, 12, 12, 12, 11, 12, 12, 11, 12, 15, 12, 15, 11, 12),
# "practical" : [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
# "exam" :  (65, 65, 55, 65, 70, 70, 60, 43, 46, 36, 48, 39, 65, 30, 65, 41, 55, 70, 45),
# "Total" :  [92, 95, 85, 95, 100, 100, 87, 70, 73, 62, 75, 66, 91, 57, 95, 68, 85, 96, 72], } 
# print(sum(dict["firstTest"]))
# print(sum(dict["Total"]) / len(dict["Total"]))

"""
Questions requiring if-else statements:

1. Write a program to check if a number entered by the user is even or odd.
2. Create a program that asks the user for their age and then tells them if they are eligible to vote or not.
3. Write a program that takes two numbers as input and prints the greater number.
4. Develop a program that asks the user to input their grade and then prints if they passed or failed (assuming passing grade is 60 or above).
5. Create a program that prompts the user to input their name and then checks if their name is longer than 5 characters or not.
"""
# Q1

# number =int(input("Enter a number :")) 
# if number % 2 == 0 :
#     print(f"{number} is an even number")
# else :
#     print(f"{number} is an odd number")
    
# # Q2
# age = ()
# eligible_age = int(input("Enter your age: "))
# if eligible_age >= 18 :
#     print("This is an eligible age to vote)")
# else :
#     print("This is not eligible to vote")

# # Q3
# a = 3
# b = 5
# if a > b :
#     print("Yes, it is greater")
# else :
#     print("No, it is not greater")

# # Q4
# grade = 67
# if grade >= 60 :
#     print(f"{grade} is a pass mark")
# else :
#     print(f"{grade} is not a pass mark")
    
# # Q5
# name = "abdul"
# if len(name) > 5 :
#     print(f"{name} is longer than 5 characters")
# else :
#     print(f"{name} is not up to 5 characters")

"""
Questions requiring while loops:
-Write a program to count from 1 to 10 using a while loop.
-Create a program that continuously prompts the user to guess a secret number (e.g., 7) until they guess correctly.
-Write a program that prompts the user to enter a number and keeps prompting until the user enters a number greater than 10.
-Develop a program that asks the user to input a password and keeps asking until they enter the correct password ('password123').
-Create a program that asks the user for a number and then prints all the numbers from that number down to 1.
"""
# Q1
# num = 1

# while num <= 10:
#     print(num)
#     num += 1  

# Q2
# secret_number = 7
# while True:
#     guess = int(input("Guess the secret number: "))
    
#     if guess == secret_number:
#         print("Congratulations! You guessed the secret number.")
#         break  
#     else:
#         print("Wrong guess! Try again.")

# Q3
# while True:
#     number = int(input("Enter a number: "))
    
#     if number > 10:
#         print("You entered a number greater than 10!")
#         break  
#     else:
#         print("The number is not greater than 10, try again.")

# Q4
# correct_password = "password123"

# while True:
#     user_input = input("Enter the password: ")
#     if user_input == correct_password:
#         print("Access granted!")
#         break  
#     else:
#         print("Incorrect password. Please try again.")

# Q5
# number = int(input("Enter a number: "))

# while number >= 1:
#     print(number)
#     number -= 1 

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

# Q4 
# a = 3
# if a == 0:
#     print("It's a zero")
# elif a %2 == 0 :
#     print("its an even number")
# elif a %2 != 0:
#     print("It's an odd number")

# Q

"""
Write a Python function safe_divide that takes two numbers as input and returns their division result. The function should handle the following cases:

Raise an error if the inputs are not numbers.
Handle division by zero by returning "Cannot divide by zero.".
Catch any unexpected errors and display an appropriate message.
Sample Input:

python
Copy code
safe_divide(10, 2)  # Should return 5.0
safe_divide(10, 0)  # Should return "Cannot divide by zero."
safe_divide(10, "a")  # Should raise a TypeError with a custom message
"""
def safe_divide(num1, num2):
    
    try:
        if num1 / num2 == 0:
            raise TypeError("Both inputs must be numbers.")
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError as e:
        return f"TypeError: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

print(safe_divide(10, 2)) 
print(safe_divide(10, 0))   
print(safe_divide(10, "a")) 

