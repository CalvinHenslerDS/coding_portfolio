# w3resource

# Python Basic Part -I


# Exercise 36:


# Problem Statement:

# Write a Python program to add two objects if both objects are integers.


# Solution Attempt:

def add_integers(n_1, n_2):
    n_1 = float(n_1)
    n_2 = float(n_2)
    # If the inputs are integers, add them
    if n_1.is_integer() == True and n_2.is_integer() == True:
        sum = n_1 + n_2
        return sum
    
    #If the inputs are not integers, print an error message
    else:
        print("At least one input is not an integer")

# Initialize test data
n_1 = 6
n_2 = 8

# Call the compare_integers function
sum = add_integers(n_1, n_2)
print(sum)