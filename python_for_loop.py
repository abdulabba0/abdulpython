"""
We use for loop to cycle through an iterable, or for iterable over a sequence

Sequence :
- String
- List 
- Tuple 
- Dictionary
- set
"""

# String
# String_var = "This is a string"

# for char in String_var :
#     print(char)

# print("==" * 10)

# List
# list_var = ["apple", "banana", "cherry"]
            
# for fruit in list_var :
#     print(fruit)

#     print("==" * 10)

# Tuple

# Using a break
# list_of_countries = ["nigeria", "canda", "kenya", "niger"]

# for country in list_of_countries :
#     print(country)
#     if country == "kenya" :
#         break

# Using a continue
# list_of_countries = ["nigeria", "canda", "kenya", "niger"]

# for country in list_of_countries :
#     print(country)
#     if country == "kenya" :
#         continue

# # Looping through a range
# for number in range(12) :
#     print(f"5 * {number} = {number * 5}")

# else :
#     print("Loop finished")

# for x in range(2) :
#     pass

# # Neested or loops
# a = ["a", "b", "c", "d", "e"]
# b = [2, 3, 4, 6, 7]

# for x in a :
#     for y in b :
#         print(f"x = {x}, y = {y}")

# List Comprehension

number = [1, 2, 3, 4, 5]
square = []

for x in number :
    square.append(x ** 2)

print(square)

squares = [x ** 2 for x in number]
print(squares)