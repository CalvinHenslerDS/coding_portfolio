# w3resource

# Python Basic Part -I


# Exercise 25:

# Problem Statement:

# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


# Solution Attempt:

# Define a function
def value_checker(input_sequence, n):

    # Check if n is in input_sequence
    if n in input_sequence:
        print("n is in input_sequence")

    # If n is not in input_sequence, print a statement indicating that
    else:
        print("n is not in input_sequence")

# Initialize a test sequence
input_sequence = [3, 4, 5, 6, 7]

# Call the value_checker function
value_checker(input_sequence, 3)
