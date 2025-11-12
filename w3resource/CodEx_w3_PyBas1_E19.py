# w3resource

# Python Basic Part -I


# Exercise 19:

# Problem Statement:

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".


# Solution Attempt:

# Define a function
def is_string(input_string):

    # Check whether input_string begins with "Is"
    if input_string[:2] != "Is":

        # Add "Is" to the beginning of input_string if it does not already begin with "Is"
        input_string = "Is" + input_string

    else:
        pass

    # Print the new string
    print(input_string)

    return input_string

# Prompt the user to input a string
input_string = input("Input a string: ")

# Call the is_string function
is_string(input_string)


# Lessons Learned:

# Syntax:
# "" + "": Concatenates two lists