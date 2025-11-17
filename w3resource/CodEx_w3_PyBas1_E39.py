# w3resource

# Python Basic Part -I


# Exercise 39:


# Problem Statement:

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.


# Solution Attempt:

def investment_calculator(initial_principle, annual_interest_rate, years):

    # Calculate final value of the investment
    result = initial_principle * (1 + annual_interest_rate / 100) ** years

    return result

# Call investment_calculator
investment_calculator(10000, 3.5, 7)


