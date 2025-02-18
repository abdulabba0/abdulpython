
import os
"""
Q. 144.	Write a function that counts occurrences of each character in a file.

Step by step procedure
1. Understand the problem
2. Idenfity the input 
3. Idenfity the output 
4. Develop a method to solve the problem
5. Write a pseudocode to solve thr problem
6. Write the solution

1. Give

2. Input:
    - A single character, a string or a list of characters
    - A file: a file path, file as a binary data

3. Output:
    - A dictionary WITH characters as keys and their counts as values

    
4. Develop method or ways to solve the problem
    - we need t check if the character is a string or a list of characters, or 
"""

# def count_characters(char, file_path:str):
#     # check if char is a list of characters or a single character
#     char_dict = {}
#     try:
#         if (isinstance(char, str) and len(char) > 1) or isinstance(char, list):
#             # Initialize an empty dictionary
#             if not os.path.exists(file_path):
#                 raise FileExistsError(f"File '{file_path}' does not exist.")
#             else:
#                 with open(file_path, 'r') as f:
#                     for line in f.readlines():
#                         for ch in line :
#                             if ch.lower() in char or ch.upper() in char:
#                                 if ch.lower() in char_dict :
#                                     char_dict[ch.lower()] += 1
#                                 else:
#                                     char_dict[ch.lower()] = 1
#                 return char_dict
#         elif isinstance(char, str) and len(char) == 1:
#             with open(file_path, 'r') as f:
#                 for line in f.readlines():
#                     if char.lower() in line.lower():
#                         if char.lower() in char_dict:
#                             char_dict[char.lower()] += 1
#                         else:
#                             char_dict[char.lower()] = 1
#             return char_dict
#         else:
#             print("Wrong character frmat your character should be a list, string or a single character")
#     except Exception as e:
#         print(f"Error occured: {e}")

# res= count_characters('s', "C:\Users\Abdul Abba\Documents\abdulpython\output.txt")
# print(res)


"""Q. 147.	Write a program that finds the most common word in a file.

Step by step procedure
1. Understand the problem
2. Idenfity the input 
3. Idenfity the output 
4. Develop a method to solve the problem
5. Write a pseudocode to solve thr problem
6. Write the solution

1.
2. input : a word and a file
3. Output: the most common word in the file
4. Develop a method to solve the problem
    - Read the file
    - Split the file into words
    - Count the occurence of each word
    - Return the most common word
5. Pseudocode to solve the problem


"""
import re

def most_common_word(file_path:str):
    word_count = {}
    with open('Me.text', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            # strip each line of punctuations
            line = re.sub(r'[^\w\s]', '', line)
            # convert each line to lowercase
            line = line.lower()
            # split the line into words
            words = line.split()
            # for each word in the line, increment the count of the word in the dictionary
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    x, y = list(word_count.items()[0])
    for a, b in word_count.items():
        if b > y:
            x, y = a, b
    return (x, y)


# Test
# res = most_common_word("C:\Users\Abdul Abba\Documents\Me")
# print(res)