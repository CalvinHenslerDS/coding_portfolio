# w3resource

# Python Basic Part -I


# Exercise 19:

# Problem Statement:

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".


# Solution Attempt:


# Prompt the user to input a string
input_string = input("Input a string: ")

def is_string(input_string):
    if input_string[:2] != "Is":
        input_string = "Is" + input_string
    else:
        pass
    print(input_string)
    return input_string

is_string(input_string)


# Lessons Learned:

# Syntax:
# "" + "": Concatenates two lists