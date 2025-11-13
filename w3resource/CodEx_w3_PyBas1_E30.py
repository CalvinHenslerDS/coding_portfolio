# w3resource

# Python Basic Part -I


# Exercise 30:


# Problem Statement:

# Write a Python program that will accept the base and height of a triangle and compute its area.


# Solution Attempt:

# Define a function
def triangle_area_calculator(base, height):

    # Initialize an empty string
    area = 0.5 * base * height

    return area

# Prompt the user to input a base and a height
base = int(input("Input a base: "))
height = int(input("Input a height: "))

# Call the triangle_area_calculator function
triangle_area = triangle_area_calculator(base, height)

# Print the result
print("The area of the triangle is %s units squared" % triangle_area)