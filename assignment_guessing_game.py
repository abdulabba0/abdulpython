import random

def guessing_game():
    while True:
        
        computer_guess = random.randint(3, 8)
        user_guess = 0
        generated_list_range = list(range(computer_guess -2, computer_guess + 2))
        user_guess = int(input(f"Guess the correct number the copmuter chose? {generated_list_range}"))
        lives = 3

        while lives > 1:
            
            print("Guess a number from this list:", generated_list_range)
            # user_guess = int(input(f"You have {lives} lives left. Take a guess: "))

            if user_guess == computer_guess:
                print("Congratulations! You've guessed the correct number!")
                break
            else:
                print("Wrong guess.")
                lives -= 1
                user_guess = int(input(f"Guess the correct number the copmuter chose? {generated_list_range}"))
        if lives == 1:
            print(f"Sorry, you've run out of lives. The number was {computer_guess}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Start the game
guessing_game()