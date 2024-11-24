"""
-Recursion is a function that it call itself.
-There must be a base where the function stops and recurse.

factorial of a number
4 : 4 * 3 * 2 * 1

1 : Initial call Factorial(4)
    n : 4 is not equal to zero, the else block run
    return 4 * factorial(4 - 1)

2 : Second call Factorial(3)
    n : 3 is not equal to zero, the else block run
    return 3 * factorial(3 - 1)

3 : Initial call Factorial(2)
    n : 2 is not equal to zero, the else block run
    return 2 * factorial(2 - 1)

3 : Initial call Factorial(1)
    n : 1 is not equal to zero, the else block run
    return 1 * factorial(1 - 1)

4 : Initial call Factorial(0)
    return 1                    
                                    
1 * 1
2 * 1
3 * 2
4 * 6
"""

# def factorial(n) :
#     print(n)
#     if n == 0 :
#         return 1
#     else :
#         return n * factorial(n-1)
    
# print(factorial(4))

"""
Calculate n fibonacci numbers
1, 2, 3, 5, 8, 13, 21, 34, 55, 89

1 : return fibonacci(4) + fibonacci(3)
2 : return fibonacci(3) + fibonacci(1)
3 : return fibonacci(2) + fibonacci(0)
4 : return fibonacci(1) + fibonacci(0)
5 : return fibonacci(0) + fibonacci(0)
6 : return 0 + 0
"""
# def fibonacci(n) :
#     print(n)
#     if n <= 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     else :
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# print(fibonacci(5))

"""
- Calculate standard deviation
- Write a fuction to calculate mean
"""

# def mean(num_list) :
#     return sum(num_list) / len(num_list)

# def standard_deviation(num_list) :
#     mean_val =  mean(num_list)
#     variance = sum((x - mean_val) ** 2 for x in num_list) / len(num_list)
#     return variance ** 0.5

# print(standard_deviation([4, 5, 6, 7, 8, 9, 10, 11]))