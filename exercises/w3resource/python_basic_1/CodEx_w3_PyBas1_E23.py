# w3resource

# Python Basic Part -I


# Exercise 23:

# Problem Statement:

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.


# Solution Attempt:


# Define a function
def potentially_partial_string_duplicator(input_string, n):

    output_string = ""

    # If n is negative, print an error message
    if n < 0:
        print("n is negative.")

    else:
        for i in range(n):

            # If input_string is two characters or shorter, repeat the entire string n times with a trailing newline character
            if len(input_string) <= 2:
                output_string = output_string + input_string + """
"""

            # If input_string is longer than two characters, repeat the first two characters of the string n times with a trailing newline character
            else:
                output_string = output_string + input_string[:2] + """
"""

    # Remove the final newline character from the string
    output_string = output_string[:-1]

    return output_string

# Prompt the user to input a string and store it as a variable
input_string = input("Input a string: ")

# Prompt the user to input an integer, convert it to an integer, and store it as a variable
n = int(input("Input a non-negative integer: "))


# Initialize a variable and set it equal to the result of potentially_partial_string_duplicator when called with input_string and n as its arguments
output_string = potentially_partial_string_duplicator(input_string, n)

# Print the result
print(output_string)
