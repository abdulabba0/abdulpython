"""
Error Handling:
We may not be able to handle all errors

try :
    run code
except TypeError error
"""
import sys
# a = 4
# b = "7"

# print(a + b) # error

# try :
#     print(a + b)
# except :
#     print("Error: Both inputs should be numbers")

# def dividenumber(a, b) :
#     try : 
#         result = a / b
#     except ZeroDivisionError :
#         print("Error: Division by zero is not allowed")
#     except TypeError as e:
#         print(f"TypeError: {e}")
#     except ValueError as e:
#         print(f"ValueError: {e}")
#     finally :
#         return result 

# try :   
#     dividenumber(a, "s", "u")
# except TypeError as e:
#     print(f"TypeError: {e}")

# stock_price = [23, 34, 54, 65]
# percentage_increase = []

"Throwing an error"
# class insuffientPrice(Exception):
#     pass

# try :
#     if len(stock_price) <2 :
#         raise insuffientPrice("stock price must not be less than 2 days")
#     for i in len(stock_price) <= 2 :
#        percentage_increase.append((i - stock_price[i]) / stock_price[i-1] * 100)
# except :
#     insuffientPrice("error calculating percentage")

# def cost(a, b):
#     return a * b
# print(cost(a, b))


# "Using Base Exception class"
# try:
#     raise SystemExit("Exiting the code")
# except BaseException as e:
#     print(f"BaseException: {e}")

# class stockError(BaseException):
#     def __init__(self, message):
#         super().__init__(message)

# "StockError"
# try:
#     raise stockError("Insufficient stock")
# except BaseException as e:
#     print(f"BaseException: {e}")

# "sys.exit"
# try:
#     raise sys.exit("insufficient stock")
# except sys.exit as e:
#     print(f"sys.exit: {e}")

# "KeyboardInterrupt"
# try :
#     while True: 
#         print("Waiting for")
# except KeyboardInterrupt as e:
#     print("KeyboardInterrupt: {e}")

# "ZeroDivisionError"
# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print(f"ZeroDivisionError")   

# "OverflowError"
# try :
#     x = 10.0 ** 1000000
# except OverflowError as e:
#     print(f"OverflowError: {e}")

# "floating point error"
# np.seterr(all='raise')

# try:
#     result = np.divide(1.0, 0.0)
#     print(result)
# except FloatingPointError as e:
#     print(f"FloatingPointError: {e}")

# "LookupError"
# a = [1, 2, 3, 4, 6]

# try:
#     print(a[5])
# except IndexError as e:
#     print("Index out of range")

# "KeyError"
# a = {"name": "John", "age": 23}
# try:
#     print(a["c"])
# except KeyError as e:
#     print(f"Key not found {e}")

# "TypeError"
# try:
#     a = 4
#     b = "7"
#     print(a + b)
# except TypeError as e:
#     print(f"TypeError: {e}")

# "ValueError"
# try:
#     a = 4
#     b = "s"
#     print(a + int(b))
# except ValueError as e:
#     print(f"ValueError: {e}")

"Delegating exceptions"
def div(a):
    return a / 0

def dicmod(a):
    try:
        res = div(a)
        return res
    except ZeroDivisionError as e:
        return("Cannot divide by zero")
        
print(dicmod(5))

"Delegating exceptions in a class"

"""
1.	Write a Python program that raises and catches a ValueError when trying to convert an invalid string to an integer.
2.	Demonstrate how a ZeroDivisionError can be caught using a try-except block.
3.	Create a function that uses try-except to handle a KeyError when accessing a non-existent key in a dictionary.
4.	Write a Python script to catch IndexError when trying to access an out-of-range index in a list.
5.	Use the KeyboardInterrupt exception to gracefully terminate a program running in an infinite loop.
________________________________________
Intermediate Questions
6.	Explain and demonstrate the difference between catching Exception and BaseException. Why is catching BaseException generally discouraged?
7.	Create a Python program that catches multiple exceptions (e.g., ValueError and TypeError) in a single try block. Show how to use multiple except branches.
8.	Write a function that propagates exceptions. For example, if a KeyError occurs inside the function, let it propagate to the calling code.
9.	Write a program that demonstrates the ordering of except branches. Place the general Exception handler before a specific exception (e.g., KeyError) and explain the result.
10.	Write a script that raises a SystemExit using sys.exit() but handles it in an except block to perform cleanup tasks before exiting.
________________________________________
Advanced Questions
11.	Create a custom function that generates a TypeError by passing the wrong argument type. Catch the exception and print a user-friendly error message.
12.	Write a program that demonstrates how to use the else block in a try-except-else structure. Include a situation where no exception occurs.
13.	Demonstrate the use of the finally block for cleanup actions (e.g., closing a file or database connection) after handling exceptions.
14.	Simulate a program where an exception propagates through multiple function calls before being caught in the main function. Use a ValueError for this exercise.
15.	Write a program that handles abstract exceptions like ArithmeticError to catch all arithmetic-related errors (ZeroDivisionError, OverflowError, etc.) in one block.
________________________________________
Complex Questions
16.	Create a custom logging mechanism that catches and logs exceptions (e.g., KeyError, IndexError, etc.) to a file while letting the program continue executing.
17.	Implement a custom retry mechanism using try-except for a function that raises a ValueError. Retry the function three times before raising the exception again.
18.	Write a Python script that uses try-except inside a for loop. Simulate a situation where an exception occurs during some iterations but not others.
19.	Write a program where:
•	The try block raises multiple exceptions (KeyError, TypeError).
•	The except block handles them in an ordered way.
•	Propagates one of the exceptions to an outer try-except.
20.	Build a small CLI program that:
•	Uses KeyboardInterrupt to gracefully exit the program.
•	Handles ValueError when the user enters invalid input.
•	Uses finally to display a goodbye message regardless of how the program ends.
________________________________________
Challenge Question
21.	Implement a program that demonstrates exception delegation in a nested function structure:
•	A top-level function calls a helper function.
•	The helper function raises an ArithmeticError.
•	The top-level function catches and handles it with a specific message.
"""

'Q20'
def register():
    try:
        while True:
            try:
                age  = int(input("Enter your age: "))
                print(f"Your age is {age}")
                return
            except ValueError as e:
                print(f"ValueError: {e}")
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: Exiting the program") 
    finally:
        print("Goodbye!")  

register()