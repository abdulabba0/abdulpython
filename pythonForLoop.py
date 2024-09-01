"""
General Questions
•	Write a Python program that takes a list of numbers and returns a list containing only the even numbers.
•	Write a Python program that takes two numbers from the user and prints their sum, difference, product, and quotient.
•	Write a Python program that checks if a given string is a palindrome (reads the same backward as forward).
•	Write a Python program that prints the first 10 Fibonacci numbers.
•	Write a Python program that takes a list of numbers and returns the largest number using a loop.
"""
#Q1
a = [4, 5, 6, 7, 8, 9, 0, 5, 3, 1, 7, 9]
even =[x for x in a if x % 2 == 0 and x != 0]
print(even)

even_list = []
for x in a :
    if x % 2 == 0 and x != 0 :
        even_list.append(x)

print(f"even list : {even_list}")

#Q2
# checking if a string is pallindrome
strings = "level"

if strings == strings[::-1] :
    print(f"{strings} is a pallindrome")
else :
    print(f"{strings} is not a pallindrome")
    
#Q3
# Fibonnaci numbers
""" 
Fibonacci numbers are numbers in which the addition of the last two
number is the next
1, 2, 3, 5, 8, 13, 21, 34, 55
"""
fib_list = [1, 2]

for x in range(2, 12) :
    first_prev = fib_list[x - 1]
    second_prev = fib_list[x - 2]
    next = first_prev + second_prev
    fib_list.append(next)
    
print(fib_list)


# print out the largest number using a loop
big_list = [3, 5, 6, 3, 4, 5, 7, 55, 34, 23, 67]
big_number = big_list[0]

for x in big_list:
    if x > big_number :
        big_number = x

print(f"The biggest number in the list is {big_number}")
    
    


    
    
# # for x in a :
# #     print(x)

# for x in range(len(a)):
#     print(a[x])
    
# check 