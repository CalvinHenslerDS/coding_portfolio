import numpy as np
from pathlib import Path
from functools import lru_cache

# Import data as a list of lists of characters (including spaces)
script_directory = Path(__file__).parent
file_path = script_directory / "advent2025_day7_data.txt"

tachyon_manifold = np.genfromtxt(file_path, dtype='U1', delimiter=1, comments=None)

# Convert tachyon_manifold to a tuple so it's hashable
grid = tuple("".join(row) for row in tachyon_manifold)
rows = len(grid)
columns = len(grid[0])

# Unlimit the lru_cache
@lru_cache(None)

def count_possible_paths(r, c):

    # If we reached the bottom row, this is 1 valid path
    if r == rows - 1:
        return 1
    
    character = grid[r][c]
    
    # Propagate the tachyon beam until it hits a split
    if character == "." or character == "S" or character == "|":
        return count_possible_paths(r + 1, c)
    
    # Count the possible paths created when a split is encountered
    elif character == "^":
        paths = 0
        if c > 0:
            paths += count_possible_paths(r + 1, c - 1)
        if c < columns - 1:
            paths += count_possible_paths(r + 1, c + 1)
        return paths
    
    # Default to a single path for other characters
    return 1

# Find the starting position
start_column = grid[0].find('S')

# Call the function
total_states = count_possible_paths(0, start_column)

# Print the result
print(f"Total possible unique states: {total_states}")