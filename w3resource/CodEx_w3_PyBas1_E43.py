# w3resource

# Python Basic Part -I


# Exercise 43:


# Problem Statement:

# Write a Python program to get OS name, platform and release information.


# Solution Attempt:

import platform
import os

# Print the name of the operating system
print("Name of the operating system: ", os.name)

# Print the name of the OS system
print("Name of the OS system: ", platform.system())

# Print the version of the operating system
print("Version of the operating system: ", platform.release())


# Lessons Learned:

# Modules:
# platform: Built-in library that provides a portable way to access information about the underlying playform on which a Python program is running