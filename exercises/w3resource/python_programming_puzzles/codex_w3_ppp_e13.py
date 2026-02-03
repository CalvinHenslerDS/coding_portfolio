'''
w3resource

# Python Programming Puzzles


# Exercise 13:


# Problem Statement:

Write a Python program to find strings in a given list starting with a given prefix.
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']

# Solution Attempt:
'''

def prefix_checker(input_list):
    prefix = input_list[0][0]
    print(prefix)
    prefix_length = len(prefix)
    output_list = []
    for element in input_list[0][1]:
        element_length = len(element)
        element_prefix_delta = element_length - prefix_length
        print(element_prefix_delta)
        not_prefix = element[:element_prefix_delta]
        print(not_prefix)
        if element[prefix_length:] == prefix:
            output_list.append(element)

    return output_list



input1 = [( 'ca',('cat', 'car', 'fear', 'center'))]

print(prefix_checker(input1))