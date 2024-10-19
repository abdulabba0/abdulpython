"""
a variable can only store a single item,
of you want to store multiple items in a variable you have to use any of the sequence.

- list
- tuple
- dictionary
- set
- frozenset
"""

# #this is a list
# #index  = self    0         1           2
# student_name = ["Kola", "kayode", "Franklin"]

# #a list can contain any tada type
# student_details = ["Kola", 34, 3.4, True, ["Musa", "saminu"], [1, 2, 3]]

# # list allows duplicate items
# ages = [23, 23, 34, 35]

# #list are ordered 
# #index  = self    0         1           2
# student_names = ["Kola", "kayode", "Franklin"]
# print(student_names[0])

# # to check the number of items in a list
# print(len(student_names))

# # to check the last item in a list 
# print(student_names[len(student_names) - 1])

# # to check the number of items in a list in reverse order as -1 for the last item in the list
# print(student_names[len(student_names) - 2])

# #checking the data type of the list
# print(type(student_names))

# # We can have an empty list
# empty_class = []
# print("The empty list ; ", empty_class)
# print("the lenght of the list : ", len(empty_class))
# print("the datayoe will return list : ", type(empty_class))

# #using the list contructor
# range_list = range(1, 10)
# print("range data type will be : ", type(range_list))
# print(range_list)
# print(list(range(1, 20)))

# # converting string to list
# poem = "Today is Great"
# print(list(poem))

# # converting tuple to list
# Height = (3, 4, 5)
# print(Height)
# print("Tuple type : ", type(Height))
# print(list(Height))

#Accessing a list
# students = ["abdul", "frank", "John", "kemi", "musa"]
# print("Accessing the item in the second index : ", students[2])
#  #using negative indexing
# print("Accessing the item in the second index : ", students[-2])
# # seleceting range of item [start:end:skip] skip = 1
# print("using range of number : ", students[0:3])
# # We can omit the start
# print(students[:3:1])
# # We can omit the end
# print(students[1:])
# # We can use negetaive slicing
# print(students[-4:-1])

# if "kemi" in [students.lower() for students in students] :
#     print("Yes, Kemi is in students list")

# Changing item in a list
students = ["abdul", "frank", "John", "kemi", "musa"]
# students[1] = "isah"
# print(students)

# # Changing a range of items
# students[1:3] = ["Ramon", "Yusuf"]
# print(students)
# students[1:3] = ["Faruk"]

# #using the insert to add at a specific index
# students.insert(0, "grey")
# print(students)

"to add at the end of the list"
# students.append("Craig")
# print(students)

# # adding a range of items
# students.extend(["bola", "ahmad", "tasiu"])
# print(students)

# # removing items from the list
# students.remove("bola")
# print(students)

# remove items from the list
# students.remove("abdul")
# print(students)

# # remove items from the list using indexing
# students.pop()
# print(students)
# students.pop(2)
# print(students)

# to delete a list
# del students
# print(students)

# # to make the list empty
# # students.clear() 
# print(students)

# looping through a list
# product_list = [["product1", 40, "product image"], ["product2", 60, "product image"], ["product3", 90, "product image"]]

# for prod in product_list:
    # print(f"""
    #         product image : {prod[2]}
    #         product Title : {prod[1]}   
#     #         product price : {prod[0]}   
#     #         """)
# count = 1
# for product in product_list:
#     print(count)
#     print(product)
#     count += 1

# for x in range(len(product_list)):
#     print(product_list[x])

# using while loop
# x = 0

# while x < len(product_list):
#     print(product_list[x])
#     x += 1

# list comprehension
# fruits = ["mango", "pear", "pinepapple", "orange", "apple"]
# new_fruits = []

# for x in fruits:
#     if x .endswith("ple"):
#         new_fruits.append(x)

# print(new_fruits)

# print([x for x in fruits if x.endswith("ple")])
# print([x.upper() for x in fruits if x.endswith("ple")])
# print([x.upper() for x in fruits if not x.endswith("ple")])

# sorting a list of numbers
# list_num = [6, 7, 8, 9, 10, 11]
# list_num.sort()
# list_num.sort(key=lambda x: x * 2, reverse=True)
# print(list_num)

# sorting a list of strings
frut = ["Orange", "Red", "Green", "Yellow"]
frut.sort(key=lambda x: x * 2, reverse=True)
print(frut)