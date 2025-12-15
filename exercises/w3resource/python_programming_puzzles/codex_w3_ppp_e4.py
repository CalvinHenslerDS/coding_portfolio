'''
w3resource

# Python Programming Puzzles


# Exercise 4:


# Problem Statement:

We are making n stone piles! 
The first pile has n stones. 
If n is even, then all piles have an even number of stones. 
If n is odd, all piles have an odd number of stones. 
Each pile must have more stones than the previous pile but as few as possible. 
Write a Python program to find the number of stones in each pile.

Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


# Solution Attempt:
'''

def pile_builder(n):
    pile_heights = [n]
    if n < 1:
        pile_heights = []
    else:
        while n - 2 > 0:
            pile_heights.append(n-2)
            n = n - 2
        pile_heights = list(reversed(pile_heights))
    return pile_heights

pile_builder(6)
pile_builder(9)
pile_builder(-4)