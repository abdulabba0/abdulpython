# i = 0

# while i <= 10 :
#     i += 1

#     if i == 5 :
#         continue # breaks the loop and restart
#     print(i)

# else :
#     print("Code is done running")

# Q1
# sum_of_even = 0
# initial = 1

# while initial < 21 :
#     if intial % 2 == 0 :
#         sum_of_even += initial
#     initial += 1
# print("sum of even Numbers :", sum_of_even)

"""
Question 2
Step by step procedure
1. Understand the problem
2. Idenfity the input 
3. Idenfity the output 
4. Develop a method to solve the problem
5. Write a pseudocode to solve thr problem
6. Write the solution

Method:
- Create a variable to hold the end time
- We use a while loop to check if the variable is <= 0
- we print out the variable and decrement the counter
- while counter less than 0
    print counter
    counter --
"""
# counter = 10
# # initial = 1
# while initial >= 21 :
#     print(counter)
#     counter -= 1

"""
Step by step procedure
1. Understand the problem
2. Idenfity the input 
3. Idenfity the output 
4. Develop a method to solve the problem
5. Write a pseudocode to solve thr problem
6. Write the solution

- Create a variable for even numbers
- we use a while loop to check if the variable is divisable by 2
-we print out the variable and if it is an even number, we print that number, if not it repeats
- while 
"""

# while True :
#     user_input = input("Enter any number")
#     if "-" in user_input :
#         print("This a negative number, enter another number")
#     elif user_input == 0 :
#         print("You hae entered zero, please enter a positive number")
#     else :
#         print("This is a positive number")
#         break

"Create a 1-12 mulitiplications table"
i = 1
while i <= 12 :
    j = 1
    while j <= 12 :
        print(f"{i} x {j} = {i * j}")
        j += 1
    print()  
    i += 1

