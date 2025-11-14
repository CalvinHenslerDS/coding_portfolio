# w3resource

# Python Basic Part -I


# Exercise 32:


# Problem Statement:

# Write a Python program to find the least common multiple (LCM) of two positive integers.


# Solution Attempt:

def LCM_calculator(n_1, n_2):

    # Initialize a variable in which to store the LCM
    LCM = 0

    # Initialize a variable in which to store a check variable (to determine when we've arrived at the LCM)
    check_var = 0

    # Iterate from 1 up to, and including, n_2
    for i in range(1,n_2+1):

        # Multiply the current number in the iteration by n_1 and check to see whether the product divided by n_2 yields an integer
        LCM = i * n_1
        check_var = LCM / n_2

        # Break from the loop when check_var is an integer because LCM is now our actual LCM
        if check_var.is_integer() == True:
            break

        else:
            pass

    return LCM

# Initialize test variables
n_1 = 8
n_2 = 4

# Call the LCM_calculator function
LCM = LCM_calculator(n_1,n_2)
print("The LCM of %s and %s is %s" % (n_1, n_2, LCM))


# Alternative Solution:

def LCM_calculator_2(n_I, n_II):

    # Set the larger of n_I and n_II equal to LCM_2
    if n_I > n_II:
        LCM_2 = n_I
    else:
        LCM_2 = n_II

    # Check whether LCM_2 is divisible by n_I and n_II; if not, add 1 to LCM_2 and check again; repeat until the LCM is found
    while LCM_2 % n_I != 0 and LCM_2 % n_II !=0:
        LCM_2 += 1

    return LCM_2

# Initialize test variables
n_I = 4
n_II = 8

#Call the LCM_calculator_2 function
LCM_2 = LCM_calculator_2(n_I,n_II)
print(LCM_2)


# Lessons Learned:

# Syntax:
# while: Used to repeatedly execute a block of code as long as a specified condition remains true