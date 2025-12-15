# w3resource

# Python Basic Part -I


# Exercise 83:


# Problem Statement:

# Write a Python program to swap two variables.


# Solution Attempt:

def variable_swapper(a, b):
    b, a = a, b
    return a, b

a, b = variable_swapper(1, 2)
print(a, b)