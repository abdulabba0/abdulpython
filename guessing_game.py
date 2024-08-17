"""
1. Understand and interprete the problem
2. Identify the input
3. Identify the output
4. Develop method to the problem
5. Write pseudocode to solve the problem
6. Write code to solve the problem
7. Test your code


1. The is to create a guessing game where user will be presented with a list of number and will be asked to guess which of the number the computer has guessed

2. The guessed number from the user

3. The output should any or all of
a. True or false if the user guessed right
b. Display the computer guess
c. Display the user guess
d. The number of guess attempt left for the user have
e. Display the list of number to guess from

4.
- we use random module to generate a random number from 1-9, that will be the computer guess
We take the computer guess and list of numbers including the answer
- We run a while loop that checks if the computer guess is the same thing as the user guess, if yes will terminate the lopp and tell the user has won, else we tell the use the guess again.
- We give the user 3 lives (3 guesses)

5.
var computerguess = random_generated_number
var userguess = 0
live = 3
while true :
    generated_random = random(1, 3)
    generated_list_range(computerguess- 2, computerguess +2)
    shuffle(generated-list_range)
    print guess a number from this list : generated_list_range
    userguess =  input("")
if userguess == compterguess:
    Print congratulations you win guess is correct
    break
else :
    live= -1
    userguess = input("")
"""

import random

computer_guess = random.randint(4, 9)
user_guess = 0
generated_list_range = list(range(computer_guess - 3, computer_guess + 3))
user_guess = int(input(f"Guess the correct number the copmuter chose? {generated_list_range}"))
lives = 2

while lives > 0 : 
   
        random.shuffle(generated_list_range)
   
        if user_guess == computer_guess :
            print("Hurray you won your guess is {user_guess} the computer is {computer_guess}")
            
        else :
            lives -= 1
        print("Your guess is wrong!")
        user_guess = int(input(f"Guess the correct number the copmuter chose? {generated_list_range}"))
        if lives == 0:
            print(F"""You have exhausted the lives left, the computer guess is {computer_guess} loser!""")
            break
