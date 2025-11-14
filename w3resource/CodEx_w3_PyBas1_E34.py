# w3resource

# Python Basic Part -I


# Exercise 34:


# Problem Statement:

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.


# Solution Attempt:

def roundup_in_range(n_1, n_2):

    # Sum the inputs
    sum = n_1 + n_2

    # If the sum is between 15 and 20, set it equal to 20
    if 15 < sum < 20:
        sum = 20
    
    # If the sum is not between 15 and 20, leave it unchanged
    else:
        pass

    return sum

# Initialize test data
n_1 = 8
n_2 = 14


# Call the roundup_in_range function
sum = roundup_in_range(n_1, n_2)
print(sum)