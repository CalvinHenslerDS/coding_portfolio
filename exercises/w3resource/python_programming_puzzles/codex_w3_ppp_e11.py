'''
w3resource

# Python Programming Puzzles


# Exercise 11:


# Problem Statement:

Write a Python program to find the indexes of numbers in a given list below a given threshold.
Original list:

[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold: 100
Check the indexes of numbers of the said list below the given threshold:
[0, 1, 2, 3, 7, 8, 9, 10]

Original list:
[0, 12, 4, 3, 49, 9, 1, 5, 3]
Threshold: 10
Check the indexes of numbers of the said list below the given threshold:
[0, 2, 3, 5, 6, 7, 8]

# Solution Attempt:
'''

def index_lister(input_list, threshold):
    indices_list = []

    for index, item in enumerate(input_list):
        if item < threshold:
            indices_list.append(index)

    return indices_list

input1 = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
input2 = [0, 12, 4, 3, 49, 9, 1, 5, 3]

print(index_lister(input1, 100))
print(index_lister(input2, 10))