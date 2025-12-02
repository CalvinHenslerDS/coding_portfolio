# w3resource

# Python Basic Part -I


# Exercise 42:


# Problem Statement:

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.


# Solution Attempt:

import struct

# Use the calcsize function to determine the size in bytes of the C int type for the current platform
# "P" is used to represent the C void pointer type
# Multiply by 8 to get the size in bits
print(struct.calcsize("P") * 8)


# Lessons Learned:

# Modules:
# struct: Module that provides functionality to convert between Python values and C structs represented as Python bytes objects