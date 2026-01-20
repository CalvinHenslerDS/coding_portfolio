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

def count_paths(start, end, graph):
    # If the device is the destination, we have completed a single path
    if start == end:
        return 1
    
    # If the device is not in our list and is not out, it is a dead end
    if start not in graph:
        return 0
    
    # Store the result as a state
    state = (start, end)
    if state in memo:
        return memo[state]
    
    # Set the total paths equal to the sum of paths from all neighbors
    total = 0
    for neighbor in graph[start]:
        total += count_paths(neighbor, end, graph)
    
    # Store and return the count of the result
    memo[state] = total
    return total

# Define Sequence 1: svr -> fft -> dac -> out
path_a = (count_paths('svr', 'fft', graph) * count_paths('fft', 'dac', graph) * count_paths('dac', 'out', graph))

# Define Sequence 2: svr -> dac -> fft -> out
path_b = (count_paths('svr', 'dac', graph) * count_paths('dac', 'fft', graph) * count_paths('fft', 'out', graph))

# Calculate the total, which is the sum of both sequences
total_valid_paths = path_a + path_b

print(f"Total paths visiting both: {total_valid_paths}")