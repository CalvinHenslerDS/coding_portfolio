# w3resource

# Python Basic Part -I


# Exercise 138:


# Problem Statement:

# Write a Python program to convert true to 1 and false to 0.


# Solution Attempt:

import random

def boolean_converter():
    unconverted_boolean = random.choice([True, False])
    if unconverted_boolean == True:
        converted_boolean = 1
    else:
        converted_boolean = 0
    print("The unconverted boolean is %s, and the converted boolean is %s" % (unconverted_boolean, converted_boolean))

boolean_converter()