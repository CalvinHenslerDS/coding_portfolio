'''
w3resource

# Python Programming Puzzles


# Exercise 9:


# Problem Statement:

Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False

# Solution Attempt:
'''

def integer_counter(input_list):
    if len(set(input_list)) != 4:
        return False
    for index, element in input_list:
        if 