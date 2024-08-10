"""
a variable can only store a single item,
of you want to store multiple items in a variable you have to use any of the sequence.

- list
- tuple
- dictionary
- set
- frozenset
"""

#this is a list
#index  = self    0         1           2
student_name = ["Kola", "kayode", "Franklin"]

#a list can contain any tada type
student_details = ["Kola", 34, 3.4, True, ["Musa", "saminu"], [1, 2, 3]]

# lst alloes duplicate items
ages = [23, 23, 34, 35]

#list are ordered 
#index  = self    0         1           2
student_names = ["Kola", "kayode", "Franklin"]
print(student_names[0])

# to check the number of items in a list
print(len(student_names))

# to check the last item in a list 
print(student_names[len(student_names) - 1])

# to check the number of items in a list in reverse order as -1 for the last item in the list
print(student_names[len(student_names) - 2])

