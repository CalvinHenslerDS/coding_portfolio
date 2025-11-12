# w3resource

# Python Basic Part -I


# Exercise 26:


# Problem Statement:

# Write a Python program to create a histogram from a given list of integers.


# Solution Attempt:

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
sample_data = np.random.normal(loc=170, scale=10, size=250)

# Generate histogram
plt.hist(sample_data, bins = 25, color = "cyan", edgecolor = 'blue')

# Generate labels
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Sample Data Distribution")

# Display histogram
plt.show()


# Lessons learned:

# Libraries:
# NumPy: Fundamental Python library for scientific computing
# Matplotlib: Comprehensive 2-D plotting library for Python

# Modules: 
# pyplot: Module within Matplotlib, providing a MATLAB-like interface for creating visualizations

# Syntax:
# plt.: Conventional alias used when importing the pyplot module
    # .hist(): Generates a histogram
    # .xlabel(): Generates a label for the x-axis
    # .ylabel(): Generates a label for the y-axis
    # .title(): Generates a title
    # .show(): Displays the visualization