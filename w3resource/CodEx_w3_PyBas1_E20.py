# w3resource

# Python Basic Part -I


# Exercise 20:

# Problem Statement:

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.


# Solution Attempt:


# Define a function
def string_duplicator(input_string, n):

    # Initialize an empty string
    output_string_placeholder = ""

    # Check whether n is non-negative
    if n >= 0:

        # If n is non-negative, append the input_string (and a newline character)
        for i in range(n):
            output_string_placeholder = output_string_placeholder + input_string + """
"""

    else:

        # If n is negative, notify the user
        print("n is less than 0")

    # Remove the final newline character from the output
    output_string = output_string_placeholder[:-1]
    return output_string

# Prompt user to input a string
input_string = input("Input a string: ")

# Initialize a variable equal to the result of calling the string_duplicator function
result = string_duplicator(input_string,3)

# Print the result
print(result)


# Lessons learned:

# Other:
# Variables created inside a function only exist within that function; to use the value outside, assign the function’s return value to a variable