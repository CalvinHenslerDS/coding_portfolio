# w3resource

# Python Basic Part -I


# Exercise 22:

# Problem Statement:

# Write a Python program to count the number 4 in a given list.


# Solution Attempt:


# Define a function
def item_counter(input_list, counted_item):

    # Initialize a counter for counted_item in input_list
    item_counter = 0

    # Iterate over items in input_list
    for item in input_list:

        # If the item matches counted_item, add 1 to item_counter
        if item == counted_item:
            item_counter += 1
    
        else:
            pass

    return item_counter

# Prompt the user to input a list of items
input_string = input("Input a list of items, separated by commas (no spaces): ")

# Split input_string into a list using comma as the delimiter
input_list = input_string.split(",")

# Prompt the user to input an item to be counted
counted_item = input("Input an item to be counted: ")

# Initialize a variable and set it equal to the result of item_counter when called with input_list and counted_item as its arguments
item_count = item_counter(input_list, counted_item)

# Print the result
print(item_count)