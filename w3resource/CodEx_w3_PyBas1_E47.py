# w3resource

# Python Basic Part -I


# Exercise 47:


# Problem Statement:

# Write a Python program to find out the number of CPUs used.


# Solution Attempt:

import multiprocessing

# Use multiprocessing.cpu_count to determine the number of available CPU cores
cpu_count = multiprocessing.cpu_count()

# Print the result
print(cpu_count)


# Lessons Learned:

# Modules:
# multiprocessing: Enables true parallelism by allowing programs to leverage multiple CPU cores