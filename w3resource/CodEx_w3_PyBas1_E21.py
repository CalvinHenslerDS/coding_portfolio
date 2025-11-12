# w3resource

# Python Basic Part -I


# Exercise 21:

# Problem Statement:

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.


# Solution Attempt:

# Define a function
def even_odd_checker(n):

    # Initialize a new variable equal to half of n
    half_n = n/2

    # Check whether half of n is an integer (n is even) or not (n is odd), and print the appropriate message
    if half_n.is_integer():
        print("n is even")
    else:
        print("n is odd")

# Prompt the user to input an integer
n = int(input("Input an integer: "))

# Call the even_odd_checker function
even_odd_checker(n)


# Lessons learned:

# Syntax:
# .is_integer(): Built-in method that determines whether a float value represents an integer without any fractional part