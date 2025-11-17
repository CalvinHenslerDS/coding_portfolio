# w3resource

# Python Basic Part -I


# Exercise 46:


# Problem Statement:

# Write a Python program to retrieve the path and name of the file currently being executed.


# Solution Attempt:

import os

# Use ose.path.realpath(__name__) to get the full path of the current file
print("Current File Name: ", os.path.realpath(__name__))