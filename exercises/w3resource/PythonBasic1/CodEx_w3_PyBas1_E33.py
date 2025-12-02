# w3resource

# Python Basic Part -I


# Exercise 33:


# Problem Statement:

# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.


# Solution Attempt:

# Import random module
import random

def sometimes_integer_summer(n_1, n_2, n_3):

    # Initialize a variable sum in which to store the sum of the inputs
    sum = 0

    # Create a list using the inputs
    number_list = [n_1, n_2, n_3]

    # If the list contains fewer than 3 unique items, return sum = 0
    if len(set(number_list)) < 3:
        pass

    # If the list contains 3 unique items, return the sum
    else:
        sum = n_1 + n_2 + n_3

    return sum

# Generate test data
n_1 = random.randint(-100,100)
n_2 = random.randint(-100,100)
n_3 = random.randint(-100,100)

# Call the sometimes_integer_summer function
sum = sometimes_integer_summer(n_1, n_2, n_3)
print(sum)


# Lessons Learned:

# Libraries:
# random: Built-in module that provides functions for generating pseudo-random numbers and performing random-based operations