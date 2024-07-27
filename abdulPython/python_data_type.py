"""
Text type :
1. String

Number type :
1. Interger
2. FLoat
3. Complex

Sequence :
1. List
2. Tuple
3. Range

Mapping Type :
1. Dictionary

Set Type :
1. Set
2. Frozen set

Byte Type :
1. Bytes
2. Byte array
3. Memory view

Boolean Type :
1. True 
2. False

None type :
1. None
"""

student_name = "Today is Great" #str
student_age = 27 # int
student_height = 6.7 # float
student_id = 5j # complex
student_names = ["Kola", "Abu", "Musa"] # List
student_names = ("Kola", "Abu", "Musa") # tuple
student_scores = [1, 2, 3, 4, 5, 6] # List
student_names_range = range(1, 8) # range
all_student_scores = {
"Math" : 87, 
"GNS101" : 80, 
"COM101" : 80
} # dictionary

studen_grade = {"A1", "B3", "B1", "A1"} # set
studen_grade_2 = ({"A1", "B3", "B1", "A1"}) # frozen set

# boolean (True or False)
is_today_sunday = True 
is_tomorrow_weekend = False

my_bytes = b"toda is awesome"
My_bytes_array = bytearray(55) # byte array
my_memory = memoryview(bytes(4)) # memory view
my_none = None # none type
# type = type() # To check the type

print(type(my_none))
print(type(My_bytes_array))
print(type(my_memory))
print(type(is_tomorrow_weekend))
print(type(is_today_sunday))
print(type(studen_grade ))
print(type(studen_grade_2))
print(type(all_student_scores))
print(type(student_names_range))
print(type(student_names))
print(type(student_scores))