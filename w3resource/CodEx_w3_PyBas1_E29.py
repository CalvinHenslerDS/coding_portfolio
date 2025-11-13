# w3resource

# Python Basic Part -I


# Exercise 29:


# Problem Statement:

# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.


# Solution Attempt:

# Define a function
def color_sifter(color_list_1, color_list_2):

    # Initialize an empty string
    color_list_1_not_2 = []

    # Loop over the list
    for item in color_list_1:

        # Check whether each item in color_list_1 is not in color_list_2
        if item not in color_list_2:

            # If an item in color_list_1 is not in color_list_2, append it to color_list_1_not_2
            color_list_both.append(item)

        # If an item in color_list_1 is not in color_list_2, move on to the next item
        else:
            pass

    return color_list_1_not_2

# Initialize sample data
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


# Call the color_sifter function
color_list_both = color_sifter(color_list_1,color_list_2)

# Print the result
print(color_list_both)