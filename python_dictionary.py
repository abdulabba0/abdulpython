"""
- Dictionary are used to store data in key value pairs.
- They are ordered, changeable but does not allow duplicate.
"""

student_info = {
    "name" : "Abdulrahim",
    "value" : 27,
    "hobbies" : ["reading", "writing", "painting"]
}

print(student_info)
print(student_info["name"])
print(student_info.get("name"))

for x in student_info :
    print(x)

# print(type(student_info))
# if type(student_info) == dict :
#     print("Yes, it is a dictionary!")
# else :
#     print("No, it is not a dictionary!")

# Accessing a dictionary
# print(student_info["hobbies"])
# print(student_info.get("name"))

# print(student_info.keys())
# for key in student_info.keys() :
#     print(key)

# print("Dictionary.values()")
# print(student_info.values())
# for values in student_info.values() :
#     print(values)

# print("Dictionary.items()")
# print(student_info.items())

# for keys, values in student_info.items() :
#     print(keys, " : ", values)

# if "name" in student_info :
#     print("Yes, name is in the dictionary!")
# else :
#     print("No, name is not in the dictionary!")
# if "age" in student_info :
#     print("Yes, age is in the dictionary!")
# else :
#     print("No, age is not in the dictionary!")

"""
A file containing duplicate items, and we want to remove the duplicate item and return a file a new file
"""
# customer_details = {}
# num = 0
# with open("customer_info.txt", "r") as f:
#     for line in f.readlines() :
#         if num > 0 :
#             dat = line.split(",") # how to spilt lines
#             if dat[0].strip() not in customer_details : #checking is name is in dictinary
#                 customer_details[dat[0].strip()] = (dat[1].strip(), dat[2].strip())
#         num += 1

# print(customer_details)

# Changing items in a dictionary 
student_info["age"] = 55
# print(student_info["age"])

student_info.update({"name" : "Sulaiman"})
print(student_info["name"])
print(student_info.get("name"))

# Adding an item to the dictionary
student_info["height"] = 66
print(student_info.get("height"))

# student_info.update({"complexion : Dark"}) 
# print(student_info.get("complexion"))

# removing an item from the dictionary
print("Removing item from a dictionary")
student_info.popitem()
print(student_info)

my_books = {
    "shakespeare" : ["Tempest", "king Henry IIV"],
    "wolesonyika" : ["Harvest of Kogi", "The Trail of Brother Jero"]
}

my_books2 = my_books.copy()

print(my_books2)

# Dictionary can contain multiple dictionaries

a = {
    "b" : [1, 2, 3],
    "c" : ["Musa", "Isah", "Tanimu"]

}
