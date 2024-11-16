import random
"""
A function is use to group code together, we use it
for code rusability
"""

"defining the function"
# def add_number(a, b):
#     print(a + b)
    
# "calling the function"

# add_number(10, 5)
# print("=====" * 20)
# print(" ")
# def say_hello() :
#     print("Hello world!")
    
# say_hello()
# print("=====" * 20)
# print(" ")

"calculate the mean of student score"
# student_score = [79, 55, 78, 85, 70, 88, 65, 70]
# student_name = "Ahmmed Balablu"

# mean = sum(student_score) / len(student_score)
# print(f"Name : {student_name}. Score : {mean}")
# print("=====" * 20)
# print(" ")

"Using a function to solve the problem above"

# def calculate_mean(student_score, student_name):
#     mean = sum(student_score) / len(student_score)
#     print(f"Name : {student_name}. Score : {mean}")

# student_score = [79, 55, 78, 85, 70, 88, 65, 70]
# student_name = "Ahmmed Balablu"

# calculate_mean(student_score, student_name)
# say_hello()
# print("=====" * 20)
# print(" ")

# def print_family(*args) :
#     for name in args:
#         print(name)

# def print_family(*abc) :
#     for name in abc:
#         print(name)
        
# print_family("Ahmmed", "Blam", "Man")

"Key word Argument"
# def all_names(first_child, second_child) :
#     print(f"First child : {first_child}. Second child : {second_child}")
    
# all_names(second_child="Blam", first_child="Ahmmed")

# def calc_mean(list_of_scores):
#     return sum(list_of_scores) / len(list_of_scores)

"Arbitrary Keyword Argument"
# def student_result(**kwargs) :
#     if "Math" in kwargs :
#         math_mean = calc_mean(kwargs["Math"])
#         print(f"Math mean : {math_mean}")
#     if "English" in kwargs :
#         english_mean = calc_mean(kwargs["English"])
#         print(f"English mean : {english_mean}")
        
# student_result(Math=[80, 90, 75], science=[95, 85, 78], English=[85, 90, 92])

"Function with default parameters"

# def add(num1, num2 = 4) :
#     print(num1 + num2)

# add(10, 2) # values can be change here

# def mean(num, type = "normal") :
#     if type == "normal" :
#         print(sum(num) / len(num))
#     elif type == "weighted" :
#         weights = [1/len(num)] * len(num)
#         print(sum(num[i] * weights[i] for i in range(len(num))))

# mean([1, 2, 3, 4, 5], type="weighted")

"adding datatypes"

# def mean(num:list, type:str = "normal") :
#     if type == "normal" :
#         print(sum(num) / len(num))
#     elif type == "weighted" :
#         weights = [1/len(num)] * len(num)
#         print(sum(num[i] * weights[i] for i in range(len(num))))

# mean([1, 2, 3, 4, 5], type="weighted")

# "pass"
# def wait():
#     pass

# "Return"
# def mean2(num) :
#     return sum(num) / len(num)

# res = mean2 =([1, 2, 3, 4, 5])
# print(res)
# print(mean2([1, 2, 3, 4, 5]))

# def standard_dev(num) :
#     mean_val = mean2(num)
#     variance = sum((x - mean_val) ** 2 for x in num) / len(num)
#     print(variance ** 0.5)

# standard_dev([1, 2, 3, 4, 5])


"Using positional Argument alone"
# def divide_me(a, b, /) : # for only positional arguments
#     return a / b

# divide_me = divide_me(2, 4)
# print(divide_me)

"Using Keyword argument alone"
# def divide_us(*, a, b) :
#     return a / b

# print(divide_us(a=10, b=2))

"""Lambda function : a lambda function is a one line function.
it can take as many parameters as possible but it can only take a single expression
"""

# def lambda_func(x) :
#     return (x ** 2 / (x+x)) 

# lambda_func = lambda x, : (x ** 2 / (x+x))
# print(lambda_func(5))

# print([random.randint(1, 20) for x in range(20)])

"""
Q1. Write a function sum_of_elements(lst) that takes a list of numbers as input and returns the sum of all the elements.
Q2. Create a function find_maximum(lst) that returns the maximum value in a given list of numbers.
Q3. Write a function unique_elements(lst) that takes a list of numbers and returns a new list with only the unique elements, preserving the original order.
"""
# Q1 
def sum_of_elements(x:list):
    return(sum(x))

print([1, 2, 3, 3])

# Q2
def find_maximum(x:list):
    return(max(x))

print(find_maximum([1, 2, 3, 3, 4, 5]))

# Q3
def unique_elements(x:list):
    return(set(x))

print(unique_elements([1, 2, 3, 3, 4, 5]))