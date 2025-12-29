---
layout: post
title: "Advent of Code 2025, Day 1: Simulating a Combination Lock"
date: 2025-12-29
categories: [Advent of Code, Algorithms]
---

## Overview
In [Day 1 of the Advent of Code 2025 challenge] (https://adventofcode.com/2025/day/1), you find yourself locked out of the North Pole. Fortunately, the elves left a set of convoluted instructions for you to follow in order to obtain the password to a secret entrance.  The crux of this challenge is simulating the behavior of a combination lock.

## The Problem Statement
The input consists of a sequence of alphanumeric strings: each composed of an 'L' or 'R' followed by an integer.  A leading 'L' represents a counter-clockwise turn; a leading 'R' represents a clockwise turn.  The integer represents how many digits to move the dial from the last position.  The starting position is 50.  The largest number on the lock is 99.

Part 1:
The password to the secret door can by found by tallying up the total number of times the dial ends on 0 after completing an input on the elves' instructions.

Part 2:
It turns out, you were following old protocol.  The actual password can be found by tallying up the total number of times the dial crosses 0 while inputting the eleves' instructions.


## Strategic Approach
The difficulty of this challenge comes in simulating the behavior of a combination lock.  A combination lock sweeps through integers in order, skipping from 99 to 0 when turning clockwise or from 0 to 99 when turning counter-clockwise.

Part 1:
My initial thought was to use a circularly-linked list.  A circularly-linked list is a variation of a linked list in which the last node points back to the first node instead of to None or null.  Though I was confident the circularly-linked list approach would work, I thought it might be interesting to try something else: leveraging the modulo operator to calculate the ending location of the dial after a rotation.

The modulo operator (%) calculates the remainder of a division operation.  For a dial with 100 positions (0 through 99), dividing the sum of the starting position and the input value by 100 should yield the correct final position of the dial after the turn.

Part 2:




## Implementation
The solution was built in Python using `itertools.combinations` for the initial pair generation and a recursive `find` function for the DSU logic.

```python
# Core DSU Logic
def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i]) # Path compression
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        # Merge the smaller group into the larger group
        if size[root_i] < size[root_j]:
            root_i, root_j = root_j, root_i
        parent[root_j] = root_i
        size[root_i] += size[root_j]
        return True
    return False