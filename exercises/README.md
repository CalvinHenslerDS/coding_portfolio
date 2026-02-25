---
layout: post
title: "Algorithmic Patterns"
date: 2026-2-25
categories: [Algorithms]
---



# Linear Patterns (Arrays and Strings)


## Two Pointers

The two-pointer algorithm is a highly efficient technique for searching, sorting, or manipulating linear data structures.  It typically reduces $O(n^2)$ complexity to $O(n)$.  By using two indices to traverse data, you can compare, swap, or identify pairs without nested loops.

| Example Exercises | |
| -------- | -------- |
| [LeetCode #11](https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_11.py) |
| [LeetCode #283](https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_283.py) |
| [LeetCode #392](https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_392.py) |
| [LeetCode #1679](https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_1679.py) |



## Sliding Window

The sliding window algorithm is a problem-solving technique used to efficiently process contiguous subsets of data.  The core idea is to transform a problem with nested loops into a single loop to reduce the process to linear time complexity by maintaining and moving a window of elements through a dataset.

| Example Exercises |  |
| -------- | -------- |
| [LeetCode #643](https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_643.py) |
| [LeetCode #1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75) | Solution in Progress |

## Prefix Sum

The prefix sum algorithm, also known as the cumulative sum or scan operation, is a data structure technique used to efficiently calculate the sum of elements within any range of an array.  This preprocessing technique transforms range sum queries from $O(n)$ time to $O(1)$ time.

| Example Exercises | |
| -------- | -------- |
| [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_238.py) |

## Fast and Slow Pointers (Hare  Tortoise)

The fast and slow pointers algorithm, also known as the Tortoise and Hare algorithm or Floyd's Cycle Detection Algorithm, is a technique that uses two pointers that traverse a data structure at different speeds to efficiently find cycles, locate the middle element, and solve other related problems.

# Searching & Sorting

## Binary Search

The binary search algorithm is an efficient search method for finding a target value within a sorted array.  It works by repeatedly dividing the search interval in half, which gives it a time complexity of $O(\log(n))$, making it significantly faster than a linear search for large datasets.

## Modified Binary Search

The modified binary search algorithm is an adaptation of the standard binary search to solve problems with altered constraints or to find specific results other than a single exact match.  The core idea of reducing the search space by half in each iteration remains, but the conditions for adjusting the pointers are changed based on the problem's specific requirements.

## Top 'K' Elements (Heaps)

The top 'K' elements algorithm involves efficiently finding the 'K' largest, smallest, or most frequent items in a dataset.  The most common and efficient algorithms use heaps or bucket sort to achieve better time complexity than a simple full sort.

# Tree and Graph Traversals

## Breadth-First Search (BFS)

BFS is a graph traversal method that systematically explores a graph or tree level by level.  It starts at a source node and explores all of its immediate neighbors before moving on to the neighbors of those neighbors and so on.

## Depth-First Search (DFS)

DFS is a graph traversal method that explores as far as possible along a single branch before backtracking to explore other paths.

## Two Heaps

The two heaps algorithm is a technique used to efficiently manage and track relative extremes within a dynamic stream of data.  It typically involves using a min-heap and a max-heap simultaneously to divice the data into two parts.

# Advanced Optimization and Logic

## Backtracking

The backtracking algorithm is a technique that systematically searches for solutions by incrementally building candidate solutions and abandoning a candidate (backtracking) as soon as it determines that it cannot possible lead to a valid solution.  It is essentially a DFS on an implicit tree of decision points.

## Dynamic Programming (DP)

DP is a method for solving complex problems by breaking them down into smaller, overlapping subproblems.  Each subproblem is solved only once, and their solutions are stored to avoid redundant computations.  This technique is especially useful for optimization problems and problems that can be formulated recursively.

## Monotonic Stack

Monotonic stack is an algorithmic technique that uses a standard stack data structure while strictly maintaining its elements in either monotonically-increasing or monotonically-decreasing order.  The key insight is to pop elements that violate this order before pushing a new element, which enables solving certain array problems in linear time instead of the typical quadratic time of brute force solutions.

## Union-Find (Disjoint Set)

Union-Find, also known as Disjoint Set Union (DSU) is used to group elements into non-overlapping sets and efficiently manage connections between them.  It is primarily a data structure that partitions a set of elements, supporting two core operations: find and union.

# Logic and Implementation

## Greedy

A greedy algorithm is a problem-solving approach that makes the best available choice at each step with the hope of finding a globally optimal solution.  This method is "short-sighted" because it never reconsiders past decisions or evaluates future possibilities in a comprehensive way.

| Example Exercises | |
| -------- | -------- |
| [LeetCode #334](https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_334.py) |
| [LeetCode #605](https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_605.py) |

## Simulation

A simulation algorithm computers the behavior of a system over time by initializing state variables, iteratively updating them according to defined logic or physical laws, and advancing a simulated clock.  These algorithms range from discrete event simulations to stochastic methods.

| Example Exercises | |
| -------- | -------- |
| [LeetCode #1431](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_1431.py) |
| [LeetCode #1071](https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_1071.py) |
| [LeetCode #1768](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75) | [My Solution](https://github.com/CalvinHenslerDS/coding_portfolio/blob/main/exercises/leetcode/leetcode_75/lc75_1768.py)