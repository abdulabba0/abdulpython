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
# even_num = [x for x in a if x % 2 == 0 and x != 0] 
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
# numbers = [3, 6, 8, 1, 2, 9, 4, 5, 7]
# big_num = numbers[0]
# for x in numbers:
#     if x > big_num:
#         big_num = x
# print(x)

