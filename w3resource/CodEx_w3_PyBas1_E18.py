# w3resource

# Python Basic Part -I


# Exercise 18:

# Problem Statement:

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.


# Solution Attempt:


# Define a function
def maybe_sum_tripler(numbers_list):

    # Initialize a variable to store the sum of the items in numbers_list
    number_sum = 0

    # Iterate over numbers_list and calculate a running sum, storing the result in number_sum
    for i in numbers_list:
        i=float(i)
        number_sum += i
    
    # Check whether the length of the set of numbers_list is equal to 1 (indicating the number of unique items)
    if len(set(numbers_list)) == 1:

        # If all items in numbers_list are identical, triple number_sum
        print("All three numbers in the list are equal to each other")
        return number_sum * 3
    
    else:

        # If all items in numbers_list are not identical, return number_sum as is
        print("All three numbers in the list are not equal to each other")
        return number_sum

# Prompt user to input 3 numbers
numbers = input("Input a sequence of three numbers separated by commas: ")

# Create a list from the input string using comma as the delimiter
numbers_list = numbers.split(",")

# Call the maybe_sum_tripler function
maybe_sum_tripler(numbers_list)


# Alternate solution:


# Lessons learned:

# Syntax:
# +=: Augmented assignment operator which provides a shorthand for adding a value to a variable and then assigning the result back to the same variable
# len(): Built-in function used to determine the length or number of items within an object
# set(): Built-in function used to create a set (an unordered collection of unique elements)