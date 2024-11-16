a = [4, 5, 6, 7, 8, 9, 0, 5, 3, 1, 7, 9]
even =[x for x in a if x % 2 == 0 and x != 0]
print(even)

even_list = []
for x in a :
    if x % 2 == 0 and x != 0 :
        even_list.append(x)

print(f"even list : {even_list}")

# checking if a string is pallindrome
strings = "level"

if strings == strings[::-1] :
    print(f"{strings} is a pallindrome")
else :
    print(f"{strings} is not a pallindrome")
    
# Fibonnaci numbers
""" 
Fibonacci numbers are numbers in which the addition of the last two
number is the next
1, 2, 3, 5, 8, 13, 21, 34, 55
"""
fib_list = [1, 2]

for x in range(2, 12) :
    first_prev = fib_list[x - 1]
    second_prev = fib_list[x - 2]
    next = first_prev + second_prev
    fib_list.append(next)
    
print(fib_list)


# print out the largest number using a loop
big_list = [3, 5, 6, 3, 4, 5, 7, 55, 34, 23, 67]
big_number = big_list[0]

for x in big_list:
    if x > big_number :
        big_number = x

print(f"The biggest number in the list is {big_number}")
    
    


    
    
# # for x in a :
# #     print(x)

# for x in range(len(a)):
#     print(a[x])
    
# check 