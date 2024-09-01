students_score = {67, 57, 89, 90, 45}
"""
-A set is not ordered.
-A set is unchangeable but we can add to it, but -cannot remove or replace.
-A set does not allow duplicate.
-A set can hold any data type.
"""

# print(students_score)
# print(f"len {len(students_score)}")
# print(f"type {type(students_score)}")

# # Another way we can create a set is using a set constructor
# new_set = set([2, 4, 5, 3,4])
# new_set2 = set([2, 4, 5, 3,4])
# print(new_set)
# print(new_set2)

# # changing the item of a set
# new_set = {34, 54, 65, 23, 54}
# print(new_set)

# # Accessing 
# for x in new_set :
#     print(x)

# # Checking if an item in the set
# print(45 in new_set)

# # adding a new item
# new_set.add(66)
# print(f" set after adding a number {new_set}")

# #combing sets
# new_set.update(new_set)
# print(f"set after updating {new_set}")

# method to use
"""
remove
discard
pop
clear
del
"""
# Removing  duplicate from a list or tuple
num_set = {45, 67, 3, 3, 3, 4, 4, 3, 6}
num_set2 = {34, 34, 54, 34, 2, 4, 3}
print(num_set)

# Removing item using remove
# num_set.remove(45)
# print(num_set)
# num_set.discard(3)
# print(num_set)
# num_set.pop()
# print(num_set)

# Joining a set
"""
- Union or update: use to combine all the items of the sets
- Intersection: keeps duplicates alone
- Difference: keeps the items of the first set that are noy in the other set
- Symmetric difference 
"""
union_set = num_set.union(num_set2)
print(union_set)

inter_set = num_set.intersection(num_set2)
print(inter_set)

diff_set = num_set.difference(num_set2)
print(diff_set)

sym_diff_set = num_set.symmetric_difference(num_set2)
print(sym_diff_set)

union2 = num_set | (num_set2)
print(union2)

inter_set2 = num_set & num_set2
print(inter_set2)

diff2 = num_set - (num_set2)
print(diff2)