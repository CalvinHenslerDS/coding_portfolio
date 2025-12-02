# w3resource

# Python Basic Part -I


# Exercise 39:


# Problem Statement:

# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

# Solution Attempt:

def distance_calculator(x1, x2, y1, y2):

    # Calculate distance using the Pythagorean Theorem
    result = ((x2 - x1) ** 2 + (y2 - y1) **2) ** (1/2)

    return result

# Call distance_calculator
distance_calculator(1,4,1,5)


