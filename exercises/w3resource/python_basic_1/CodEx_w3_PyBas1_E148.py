# w3resource

# Python Basic Part -I


# Exercise 148:


# Problem Statement:

# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.


# Solution Attempt:

import random

sequence = []
for i in range(0,10):
    sequence.append(random.randint(1,100))

def min_max_finder(input_sequence):
    min = 101
    max = 0
    for item in input_sequence:
        if item < min:
            min = item
        if item > max:
            max = item
    return min, max

min, max = min_max_finder(sequence)

print(sequence, min, max)