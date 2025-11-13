# w3resource

# Python Basic Part -I


# Exercise 30:


# Problem Statement:

# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.


# Solution Attempt:

def GCD_Calculator(n_1, n_2):

    # Initialize empty lists to store divisors in
    divisors_1 = []
    divisors_2 = []

    for i in range(1, n_1):

        # Calculate the quotient of n_1 and i
        quotient_1 = n_1 / i

        # If the quotient of n_1 and i is an integer, i is a divisor of n_1, so append it to divisors_1
        if quotient_1.is_integer() == True:
            divisors_1.append(i)
        else:
            pass
    
    # If the remainder of n_2 / i is 0, i is a divisor of n_2, so append it to divisors_2
    for i in range(1, n_2):
        if n_2 % i == 0:
            divisors_2.append(i)
        else:
            pass
    
    # Initialize a variable GCD to store the greatest common divisor
    GCD = 1

    # Update GCD to store the largest item shared between divisor_1 and divisor_2
    for i in divisors_1:
        if i in divisors_2:
            GCD = i
    return GCD
        
# Call GCD_Calculator and print the result
test = GCD_Calculator(336,360)
print(test)


# Lessons Learned:

# Syntax:
# x % y: The modulo operator returns the remainder of the division of x by y