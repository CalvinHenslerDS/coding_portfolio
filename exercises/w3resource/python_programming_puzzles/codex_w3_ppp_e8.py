'''
w3resource

# Python Programming Puzzles


# Exercise 8:


# Problem Statement:

Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]


# Solution Attempt:
'''

def string_splicer(input_string):
    words = []
    commas_spaces = []
    working_words_string = ""
    working_commas_spaces_string = ""
    for index, char in enumerate(input_string):
        if char not in (',', ' '):
            if len(working_commas_spaces_string) > 0:
                commas_spaces.append(working_commas_spaces_string)
                working_commas_spaces_string = ""
            working_words_string += char
        else:
            if len(working_words_string) > 0:
                words.append(working_words_string)
                working_words_string = ""
            working_commas_spaces_string += char
        if index == len(input_string)-1:
            if len(working_commas_spaces_string) > 0:
                commas_spaces.append(working_commas_spaces_string)
            if len(working_words_string) > 0:
                words.append(working_words_string)
    return words, commas_spaces

input_string = "Mauler, brawler, legacy hauler"

print(string_splicer(input_string))