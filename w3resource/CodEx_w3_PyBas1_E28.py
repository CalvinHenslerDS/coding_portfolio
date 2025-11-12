# w3resource

# Python Basic Part -I


# Exercise 28:


# Problem Statement:

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.


# Solution Attempt:

# Define a function
def even_reporter(input_list):

    # Initialize an empty string
    even_list = []

    # Loop over the list
    for item in input_list:

        # Calculate half of the item
        half_item = item/2

        # Check whether half of the item is an integer (indicating that the item is even); if yes: append to even_list
        if half_item.is_integer() == True:
            even_list.append(item)

        # Check whether the item is equal to 237; if yes: append it to even_list and exit the loop    
        elif item == 237:
            even_list.append(item)
            print("237 encountered.")
            break

        # If the item is neither even nor equal to 237, move on to the next item
        else:
            pass

    return even_list

# Initialize a sample list of numbers
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

# Call the even_reporter function and set its result equal to even_list
even_list = even_reporter(numbers)

# Print the result
print(even_list)
        

# Lessons Learned:

# Syntax:
# .append(): Built-in method used with lists to add a single item to the end of the list