import random


"""
Step by step procedure
1. Understand the problem
2. Idenfity the input 
3. Idenfity the output 
4. Develop a method to solve the problem
5. Write a pseudocode to solve thr problem
6. Write the solution

1: To create a tic tac toe game
-it is a game where two people can play.
-The game consist of 3x3 grid, each 
- Each player maps a O or X on each square
- first player which maps 3 in a vertically, horinzontally, diagonally wins.
- In case where none of the players wins, the game ends in a tie and asks to reset or end

2. Input : 2 players (X and O), and the grid of 3x3.

3. Output: The final state of the grid after the game ends.

4.:
- Create an empty list representing the 9 squares of the box
- Print out a 3x3 grid assigning indexes from the list to the sqaures

- create a list representing each possible combination that will result to a win.
- 
"""

board = [" " for x in range(9)]

def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]}"
    row2 = f"| {board[3]} | {board[4]} | {board[5]}"
    row3 = f"| {board[6]} | {board[7]} | {board[8]}"
    print(row1)
    print(row2)
    print(row3)

# print(print_board())
def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), 
                            (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    
    if " " not in board :
        return "Tie"
    return False

# def play_game():
#     current_player = "X"
#     while True:
#         print_board()
#         move = input(f"Player {current_player} choose position from 1-9: ")
#         if board[int(move) - 1] != " " :
#             print("Invalid move, choose an empty square")
#             continue

#         board[int(move) - 1] = current_player
#         result = check_winner()
#         if result :
#             print_board()
#             if result == "Tie" :
#                 print("It's a Tie!")
#             else:
#                 print(f"Player {result} has won the game")
#             break
#         if current_player == "X" :
#             current_player = "0"
#         else :
#             current_player == "X"

# play_game()

"create for player com"

def play_game():
    current_player = "X"
    while True:
        print_board()
        if current_player == "X":
            move = input(f"Player {current_player} choose position from 1-9: ")
        else:
            move = str(random.choice([i for i in range(1, 10) if board[i - 1] == " "]))
            print(f"Invalid move, choose an empty square")

        if board[int(move) - 1] != " " :
            if current_player == "X" :
                print("Invalid move, choose an empty square")
            continue

        board[int(move) - 1] = current_player
        result = check_winner()
        if result :
            print_board()
            if result == "Tie" :
                print("It's a Tie!")
            else:
                print(f"Player {result} has won the game")
            break
        if current_player == "X" :
            current_player = "0"
        else :
            current_player = "X"
        
play_game()