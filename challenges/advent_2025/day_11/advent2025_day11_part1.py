import pathlib
import sys

# Get the directory where this script is saved
current_dir = pathlib.Path(__file__).parent

# Define the filename (ensure this matches your .txt file name)
filename = "advent2025_day11_data.txt"
file_path = current_dir / filename

# Read and process the data
list_of_lists = []

with open(file_path, "r") as file:
    for line in file:
        # Strip whitespace and split by the colon to separate the key
        if ":" in line:
            parts = line.split(":", 1)
            # The second part contains the items; split them by space
            items = parts[1].strip().split()
            # Insert the key as the first element if you want it included
            list_of_lists.append([parts[0].strip()] + items)

# Parse data into a dictionary for fast lookups
graph = {}
for line in list_of_lists:
    node = line[0]
    neighbors = line[1:]
    graph[node] = neighbors

# Initialize a memoization dictionary to store results of sub-problems
memo = {}

def count_paths(current_node):
    # If we reached the output, we found a single successful path
    if current_node == 'out':
        return 1
    
    # If the device is not in our list and is not out, it is a dead end
    if current_node not in graph:
        return 0
    
    # If we have already calculated paths from this node, return it
    if current_node in memo:
        return memo[current_node]
    
    # Set the total paths equal to the sum of paths from all neighbors
    total_paths = 0
    for neighbor in graph[current_node]:
        total_paths += count_paths(neighbor)
    
    # Store and return the count of the result
    memo[current_node] = total_paths
    return total_paths

# Execute count_paths and print the result
result = count_paths('you')
print(f"Total number of paths: {result}")