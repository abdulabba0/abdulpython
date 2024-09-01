a = (3, 4, 5, 6)

"""
Tuples are a way of storing more than one item in a variable 
They are are ordered, unchangable, and allow duplicate
"""
# print(a)
# print(len(a))
# print(type(a))

# # Ordered - each item has a position
# print(a[1])
# print(a[-1])

# # they are unchangable, you can't remove, add or delete
# a[-1] = 5
# print(a)

#tuple item all duplicate
# c = (5, 6, 4, 5, 6)
# print(c)

# tuple can contain any data type
# d = (4, 6.4, "kola", [4, 3, 5], 3j)
# print(d)

# using the tule method to create a tuple
# re1 = [2, 3, 4, 5]
# re2 = "1234"

# re1 = tuple(re1)
# re2 = tuple(re2)

# print(re1)
# print(re2)

student_name = ["Frank", "Kola", "Isah", "Abdul"]

# accessing a tuple
# print (student_name[3])
# print(student_name[-2])

# tuple slicing
# print(student_name[:2])

# re3 = re1 + re2
# print(re3)

# re4 = re3 * 2
# print(re4)

# unpacking a tuple
# names_of_student = ["frank", "Ibrahim", "Godje", "hassan", "Bliueder"]
# *st1, st2, st3, = names_of_student
# print(st1)
# print(st2)
# print(st3)
# # print(st4)
# # print(st5)

# throwaway variable
# _, _, *last_three = names_of_student
# print(last_three)

# Looping through a tuple
names_of_student = ("frank", "Ibrahim", "Godje", "hassan", "Bliueder")

for x in names_of_student :
    print(x)

for x in range(len(names_of_student)):
    print(names_of_student[x])

i = 0
while i < len(names_of_student) :
    print(names_of_student[i])
    i += 1

# Joining tuple
names_of_student2 = ("frank", "Ibrahim", "Godje", "hassan", "Bliueder")

new_names = names_of_student + names_of_student2
print(new_names)
mul_names = new_names * 2
print(mul_names)