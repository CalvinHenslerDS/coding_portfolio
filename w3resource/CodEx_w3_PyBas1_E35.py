# w3resource

# Python Basic Part -I


# Exercise 35:


# Problem Statement:

# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.


# Solution Attempt:

def compare_integers(n_1, n_2):

    # Calculate the absolute value of the difference between n_1 and n_2
    abs_diff = abs(n_1 - n_2)

    # Return True if n_1 and n_2 are equal or if the absolute value of their difference is equal to 5
    if n_1 == n_2 or abs_diff == 5:
        return True

    # Otherwise, return False
    else:
        return False

# Initialize test data
n_1 = 8
n_2 = 8


# Call the compare_integers function
comparison = compare_integers(n_1, n_2)
print(comparison)