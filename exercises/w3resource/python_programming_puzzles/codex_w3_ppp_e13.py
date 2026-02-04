'''
w3resource

# Python Programming Puzzles


# Exercise 13:


# Problem Statement:

Write a Python program to find strings in a given list starting with a given prefix.
Input:
[( 'ca',('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']

# Solution Attempt:
'''

def prefix_checker(input_list):
    prefix = input_list[0][0]
    prefix_length = len(prefix)
    output_list = []
    for element in input_list[0][1]:
        element_prefix = element[:prefix_length]
        if element_prefix == prefix:
            output_list.append(element)

    return output_list



input1 = [( 'ca',('cat', 'car', 'fear', 'center'))]

print(prefix_checker(input1))