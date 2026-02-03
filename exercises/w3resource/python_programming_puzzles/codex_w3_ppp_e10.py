'''
w3resource

# Python Programming Puzzles


# Exercise 10:


# Problem Statement:

Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']

# Solution Attempt:
'''

def parenthesis_parser(input_str):
    left_counter = 0
    right_counter = 0
    output_list_element = ""
    output_list = []

    for element in input_str:
        if element == "(":
            left_counter += 1
            output_list_element += element
        if element == ")":
            right_counter += 1
            output_list_element += element
        
        if (left_counter == right_counter) and (left_counter > 0):
            output_list.append(output_list_element)
            output_list_element = ""
            left_counter = 0
            right_counter = 0

    return output_list

input1 = "( ()) ((()()())) (()) ()"
input2 = "() (( ( )() ( )) ) ( ())"

print(parenthesis_parser(input1))
print(parenthesis_parser(input2))