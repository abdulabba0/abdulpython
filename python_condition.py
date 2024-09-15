"""
Conditions are if, elif and else

== equal to
!= not equal to
< less than
> greater than
<= less than or equal to
>= greater than or equal to

weather condition
cold : tea
hot : cold water
hot and weekend : chilled soft drink
raining : beverage

"""
weather = "cold"
week_day = "saturday"

# if weather == "hot" :
#     print("Drink cold water")
# elif weather == "cold" :
#     print("Drink hot Tea")
# elif weather == "hot" and (week_day == "saturday" or week_day == "sunday") :
#     print("Take a chilled soft Drink")
# else :
#     print("Take any beverage of your choice")

# amount_to_purchase = int(input("How much Goods do you buy : "))
# if amount_to_purchase > 500 :
#     print("Congratulations you won a lottery Ticket")
# else :
#     print("Sorry, you're not qualified for the lottery. Buy more to qualify.")

a = 10
b = 20

# one line of if statement
# if b > 20 :
#     print(f"{b} is greater than {a}")

# one line of if-else statement
# print("a is grater than b") if a > b else print("b is greater than a")

# Multiple conditions on same line
# print("a is greater than b") if a > b else print("they're equal") if a == b else print("b is greater than a")

# using not in if statement 
# if not (a > b) :
#     print("b is greater than a")

# Nested of if statement
"""
Send a message to a number, the message can only send to number that statr with +234
08055535553
90333434443
2348111223344
+234837584783

integer - string
"""
# number = "08078776605"

# initial_number = ""

# if int(number) :
#     initial_number = number
#     if initial_number[0] == "0" :
#         initial_number = "+234" + initial_number[1:] 
#     elif initial_number.startswith("234") : 
#         initial_number = "+" + initial_number

# print(initial_number)

"""
1. check if a variable is a string
2. check if it's a sentence or a work
3. if it's sentence, checkif the string contain a number
4. if yes, check if it's positive or negative
"""

string_check = "This is good -223"

if type(string_check) == str :
    print("It's a  string")
    if len(string_check.split(" ")) > 1 :
        print("It's a sentence")
        for word in string_check.split(" ") :
            print(word)
            if word.isdigit() or word[1:].isdigit() :
            # if word.isdigit() :
                print("There's a number in the string")
                if int(word) >= 0 :
                    print("yes, it's a positive number")
                else :
                    print("no, it's a negative number")

#pass
if 4 > 2 :
    pass