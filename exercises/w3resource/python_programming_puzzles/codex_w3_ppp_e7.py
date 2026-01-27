'''
w3resource

# Python Programming Puzzles


# Exercise 7:


# Problem Statement:

Write a Python program to check a given list of integers where the sum of the first i integers is i.
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False


# Solution Attempt:
'''

def i_summer(input_list):
    i_sum = 0
    for index, element in enumerate(input_list):
        i_sum += element
        if i_sum != index + 1:
            return False
    return True
input1 = [0, 1, 2, 3, 4, 5]
input2 = [1, 1, 1, 1, 1, 1]
input3 = [2, 2, 2, 2, 2]
print(i_summer(input1))
print(i_summer(input2))
print(i_summer(input3))