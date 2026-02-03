'''
w3resource

# Python Programming Puzzles


# Exercise 12:


# Problem Statement:

Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]

# Solution Attempt:
'''

def palindrome_checker(input_string):
    is_palindrome = True
    for number in range(len(input_string)//2):
        if input_string[number] != input_string[-(number+1)]:
            is_palindrome = False
    return is_palindrome

def palindrome_list_checker(input_list):
    results = []
    for element in input_list:
        if palindrome_checker(element) == True:
            results.append(True)
        else:
            results.append(False)

    return results


input1 = ['palindrome', 'madamimadam', '', 'foo', 'eyes']

print(palindrome_list_checker(input1))