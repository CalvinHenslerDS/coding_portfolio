# w3resource

# Python Basic Part -I


# Exercise 37:


# Problem Statement:

# Write a Python program that displays your name, age, and address on three different lines.


# Solution Attempt:

def personal_info():

    # Initialize variables for the personal information
    name, age = "Darrow", 16
    address = "Lykos"

    # Print the information
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# Call personal_info
personal_info()


# Lessons Learned:

# Syntax:
# str.format(): String method used for string formatting, allowing you to embed values into a template string at specific placeholders defined by curly breaces {} within the string