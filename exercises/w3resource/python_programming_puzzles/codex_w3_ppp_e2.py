'''
w3resource

# Python Programming Puzzles


# Exercise 2:


# Problem Statement:

Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False


# Solution Attempt:
'''

def list_tester(list):
    length = len(list)
    fifth_element = list[4]
    fifth_element_count = 0
    if length < 5:
        print("The list is too short to find a fifth element")
        return False
    elif length != 8:
        print("The list is not 8 items long.")
        return False
    else:
        for element in list:
            if element == fifth_element:
                fifth_element_count += 1
        if fifth_element_count == 3:
            print("The fifth element is %s" % fifth_element)
            return True
            

    
input_1 = [19, 19, 15, 5, 5, 5, 1, 2]
input_2 = [19, 15, 5, 7, 5, 5, 2]
input_3 = [11, 12, 14, 13, 14, 13, 15, 14]
input_4 = [19, 15, 11, 7, 5, 6, 2]

list_tester(input_1)
list_tester(input_2)
list_tester(input_3)
list_tester(input_4)

print(int_counter(input_1), int_counter(input_2), int_counter(input_3))

