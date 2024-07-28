"""
variable is like a container that stores data vaule
"""

x = 100 # integer
my_name = "Abdul Faiz" # string
height = 4.5 # float

# when interger is devided it automatically convert to float
# print(x)
# print(my_name)
# print(height)
# print("x divided by 10", x / 10)

 # casting means coverting from one datatype tp another
 # casting from interger string
# print(str(x))

# x_string = str(x)

# # print(type(10.0))

# # casting from string to interger
# my_score = "23"
# # print(type(my_score)) # checking datattype using type function

# my_score_int = int(my_score)
# # casting str to float
# my_score_flaot(my_score)
# print("converting str to float : " type(my_score_float)) 

# poem = """
# Tick says the clock,
# tick! Tick!
# What you have to do, do quickly!
# """

# print(poem)

# OVerwriting variable
student1 = 34
student1 = 35

# print(student1)

"""
Rules in naming variables
1. can not start with a number only underscore or letter
2. can contain a number but not start with a number
3. variable can only contain letters alphanumeric (a-z, A-Z and 0-9)and only contain underscore
4. A variable name are case sensitive
5. variable names cannot be python keywords 
"""

# Assigning vaules to a variable
a = 4, 5, 6
# print(type(a))

# we can assign multiple values to multiples variables
a, b, c = 3, 4, 5
# print("a : ", a)
# print("b : ", b)
# print("c : ", c)

# You ca assign single  values to multiple variables
a = b = c = 40

#print("a : ", a, "b : ", b, "c : ", c)

# Unpacking variables
student_score1, student_score2, *student_score3 = [5, 6, 7, 4]
# print("student_score1 : ", student_score1)
# print("student_score2 : ", student_score2)
# print("student_score3 : ", student_score3)

# print(5 * 6 + 7 - 3 ** 6)
a = "==" * 6

# Line Break
print('=======' * 10)

# A variable in a block of code is called local varible
def calmean():
   global a; a = 5 # loacal variable
calmean()
print(a)
a = 67 # global variable

"""
Pep 8 rules
if you're using variable with multiple name, seperate them with underscores
Snake Case Examples
student_name = "Frank"

same thing with function
def cal_student_score():
    pass
    
use camel case if it is class name
class studentName() :
    pass
    
Pascal case
def StudentName():
"""