# w3resource

# Python Basic Part -I


# Exercise 24:

# Problem Statement:

# Write a Python program to test whether a passed letter is a vowel or not.


# Solution Attempt:


# Define a function
def vowel_checker(input_letter):

    # Initialize a list containing all vowels
    vowels = ("a", "e", "i", "o", "u")

    # Check if input_letter is in vowels
    if input_letter in vowels:
        print("The input is a vowel.")

    # Check if input_letter is y
    elif input_letter == "y":
        print("The input is sometimes a vowel.")


    else:
        print("The input is not a vowel.")

# Prompt the user for an input letter and store it as a variable
input_letter = input("Input a letter: ")

# Call the vowel_checker function
vowel_checker(input_letter)


# Lessons learned:

# Syntax: 
# in: Membership operator to check if a specified value exists within a sequence or if a key exists within a dictionary
