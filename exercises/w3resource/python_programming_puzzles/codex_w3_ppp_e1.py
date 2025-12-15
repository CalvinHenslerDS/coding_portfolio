'''
w3resource

# Python Programming Puzzles


# Exercise 1:


# Problem Statement:

Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True


# Solution Attempt:
'''
def int_counter(a):
    count_19 = 0
    count_5 = 0
    for i in a:
        if i == 19:
            count_19 += 1
        elif i == 5:
            count_5 += 1
    if count_19 == 2 and count_5 >= 3:
        return True
    else:
        return False
    
input_1 = [19, 19, 15, 5, 3, 5, 5, 2]
input_2 = [19, 15, 15, 5, 3, 3, 5, 2]
input_3 = [19, 19, 5, 5, 5, 5, 5]

print(int_counter(input_1), int_counter(input_2), int_counter(input_3))

