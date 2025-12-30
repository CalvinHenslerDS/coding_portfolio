---
layout: post
title: "Advent of Code 2025, Day 1: Simulating a Combination Lock"
date: 2025-12-29
categories: [Advent of Code, Algorithms]
---

## Overview
In [Day 1 of the Advent of Code 2025 challenge] (https://adventofcode.com/2025/day/1), you find yourself locked out of the North Pole. Fortunately, the elves left a set of convoluted instructions for you to follow in order to obtain the password to a secret entrance.  The crux of this challenge is simulating the behavior of a combination lock.

## The Problem Statement
The input consists of a sequence of alphanumeric strings: each beginning with an 'L' or 'R' and ending with an integer.  A leading 'L' represents a counter-clockwise turn; a leading 'R' represents a clockwise turn.  The integer represents how many digits to move the dial from the last position.  The starting position is 50.  The largest number on the lock is 99.

**Part 1:** 
The password to the secret door can by found by tallying up the total number of times the dial ends on 0 after completing an input on the elves' instructions.

**Part 2:**
It turns out, you were following old protocol.  The actual password can be found by tallying up the total number of times the dial crosses 0 while inputting the eleves' instructions.


## Strategic Approach
The difficulty of this challenge comes in simulating the behavior of a combination lock.  A combination lock sweeps through integers in order, skipping from 99 to 0 when turning clockwise or from 0 to 99 when turning counter-clockwise.

**Part 1:**
My initial thought was to use a circularly-linked list.  A circularly-linked list is a variation of a linked list in which the last node points back to the first node instead of to None or null.  Though I was confident the circularly-linked list approach would work, I thought it might be interesting to try something else: leveraging the modulo operator to calculate the ending location of the dial after a rotation.

The modulo operator (%) calculates the remainder of a division operation.  For a dial with 100 positions (0 through 99), dividing the sum of the starting position and the input value by 100 should yield the correct final position of the dial after the turn, regardless of the length of the turn.  

**Part 2:**
Although counting passed zeros as opposed to landed zeros seems like a trivial evolution, it adds several layers of complication for the approach I selected.  I opted to use floor division (//) to count the number of times zero was passed.  For simple test cases, a straightforward implementation was sufficient; however, I uncovered some quirks of floor division's functionality that I was not previously aware of, which I will discuss in the next section.




## Implementation
I built the solutions in Python.  Each solution consists of two primary functions: *list_converter* and *zero_counter*.  

*list_converter* works the same in both parts of the challenge.
1. **Initialize an empty list** to store signed integers in.  
2. **Iterate over the input list** of alphanumeric strings.
3. **Initialize helper variables** to store the direction ('L' or 'R') and the following integer for each element in the elves' instructions.
4. **Assign the correct sign based on the first character of the string**: strings beginning with 'L' will be converted into negative integers, and strings beginning with 'R' will be converted into positive integers.  The magnitude of the integer is equal to the integer converted string following the first character.
5. **Append the converted list element to *signed_integer_instructions*.** 
6. **Return *signed_integer_instructions*.**
```python
def list_converter(instructions_list):

    # 1. Initialize an empty list
    signed_integer_instructions = []

    # 2. Iterate over the input list
    for item in instructions_list:
        
        # 3. Initialize helper variables
        direction = item[0]
        magnitude_int = int(item[1:])

        # 4. Assign the correct sign based on the first character of the string
        if direction == "R":
            signed_value = magnitude_int

        else:
            signed_value = -magnitude_int

        # 5. Append the converted list element to signed_integer_instructions
        signed_integer_instructions.append(signed_value)

    # 6. Return signed_integer_instructions
    return signed_integer_instructions
```
**Part 1**: Counting zeros as the dial lands on them is straightforward: 
1. **Call the *list_converter* function** to convert the alphanumeric instructions into a list of usable, signed integers.
2. **Initialize helper variables**, *zero_count* and *value*.  *zero_count* stores the number of zeros on which the function lands while 'turning the dial.'  *value* stores the integer on which the dial lands after a turn.
3. **Iterate over the instructions** in *signed_instructions_list* (an output of the *list_converter* function) and apply the modulu operator to the sum of the integer the dial started on (*value*) and the current element in the elves' instructions.
4. **Add one to *zero_count* if the dial lands on zero** (meaning the modulo operator yielded a value of zero).
5. **Return *zero_count*.**

```python
def zero_counter(instructions_list):

    # 1. Call the list_converter function
    signed_instructions_list= list_converter(instructions_list)

    # 2. Initialize helper variables
    zero_count = 0
    value = 50

    # 3. Iterate over the instructions
    for item in signed_instructions_list:
        value = (value + item) % 100

        # 4. Add one to the zero count if the dial lands on zero
        if value == 0:
            zero_count += 1
    
    # 5. Return zero count
    return zero_count
```

**Part 2:**: Counting zeros as the dial passes them is more difficult: 
1. **Call the *list_converter* function** to convert the alphanumeric instructions into a list of usable, signed integers.
2. **Initialize helper variables**, *zero_count* and *value*.  *zero_count* stores the number of zeros on which the function lands while 'turning the dial.'  *value* stores the integer on which the dial lands after a turn.
3. **Iterate over the instructions** in *signed_instructions_list* (an output of the *list_converter* function) and apply the modulu operator to the sum of the integer the dial started on (*value*) and the current element in the elves' instructions.
4. **Do nothing for a zero magnitude turn.**
5. **Use floor division to determine the number of times zero is passed**.  When starting at zero and turning left, there is a subtlety: if a negative number is used for the floor division calculation, the result will not align with the logic we are simulating.  For this reason, flip the sign of the element of *signed_instructions_list* when performing the calculation.  Alternatively, flip the sign of the result.
6. **Use floor division to determine the number of times zero is passed.**  When performing a counter-clockwise turn starting from a nonzero *value*, we cannot simply flip the sign of the instruction and proceed with floor division as before.  Nor can we simply subtract from *value* because a quirk of floor division with negative numbers is that: $-1 // 2 = -1$ instead of $0$ as we might expect.  There are a number of ways to work around this pitfall, but I opted to maintain an approach that is consistent with the previous step: simulate a logically-equivalent clockwise turn.  To do this, set a starting value of $100$ within the calculation, subtract the starting value, and flip the sign of the element in *signed_instruction_list*.  For a starting value of $40$ and an input of $-110$, our simulation will act as if it is starting at $60=100-40$ and increasing by $110$ (and arriving at $170$) before performing the floor division.  This may seem counterintuitive, but note that turning the dial 30 more clicks in the same direction will register the next zero.  This is logically consistent with our starting parameters and, as it turns out, holds for all edge-cases.
7. **Use floor division to determine the number of times zero is passed.**  For a clockwise turn, no mental gymnastics are required.
8. **Update *value* using the modulo operator.**
9. **Return *zero_count*.**
```python
def zero_counter(instructions_list):

    # 1. Call the list converter function
    signed_instructions_list = list_converter(instructions_list)

    # 2. Initialize helper variables
    zero_count = 0
    value = 50

    # 3. Iterate over the instructions
    for item in signed_instructions_list:

        if item < 0:

            if value == 0:
                 # 4. Do nothing for a zero magnitude turn
                 if item == 0:
                      pass
                 
                 # 5. Use floor division to determine the number of times zero is passed
                 else:
                    zero_count += - item // 100

            # 6. Use floor division to determine the number of times zero is passed
            else:
                zero_count += (100 - value - item) // 100

        # 7. Use floor division to determine the number of times zero is passed
        else:
            zero_count +=  (value + item) // 100

        # 8. Update value using the modulo operator
        value = (value + item) % 100

    # 9. Return zero_count 
    return zero_count
```