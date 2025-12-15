# w3resource

# Python Basic Part -I


# Exercise 27:


# Problem Statement:

# Write a Python program that concatenates all elements in a list into a string and returns it.


# Solution Attempt:

# Define a function
def list_concatenator(input_list):

    # Initialize an empty string
    item_string = ""

    # Add every item in the list to the empty string
    for item in input_list:
        item_string = item_string + item

    return item_string

# Initialize a sample input list
input_list = ("H", "a", "i", "l", " ", "R", "e", "a", "p", "e", "r", "!")

# Store the result of list_concatenator as a variable
item_string = list_concatenator(input_list)

# Print the result of list_concatenator
print(item_string)