# w3resource

# Python Basic Part -I


# Exercise 49:


# Problem Statement:

# Write a Python program to list all files in a directory.


# Solution Attempt:

from os import listdir
from os.path import isfile, join

# Create a list that contains the names of files in the specified directory
files_list = [f for f in listdir('C:/Users/624371/coding-exercises/w3resource') if isfile(join('C:/Users/624371/coding-exercises/w3resource', f))]

# Print files_list
print(files_list)