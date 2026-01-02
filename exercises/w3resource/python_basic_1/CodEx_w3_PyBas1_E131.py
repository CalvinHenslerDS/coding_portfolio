# w3resource

# Python Basic Part -I


# Exercise 131:


# Problem Statement:

# Write a Python program to split a variable length string into variables.


# Solution Attempt:

input_string = "Hail Reaper!"

def string_splitter(input_string):

    chars = []

    for char in input_string:
        chars.append(char)

    return chars

split_string = string_splitter(input_string)

print(split_string)
