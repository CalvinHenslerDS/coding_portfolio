import numpy as np
from pathlib import Path

# Import data
script_directory = Path(__file__).parent
file_path = script_directory / "advent2025_day4_data.txt"

grid = np.genfromtxt(file_path, dtype='U1', delimiter=1, comments=None)

rows, columns = grid.shape

def accessible_roll_counter(grid):

    # Initialize variables to count rolls and removals
    accessible_roll_count = 0
    new_removals = -1

    # Check for newly-accessible rolls if any were removed on the last loop
    while new_removals != 0:

        # Reset the new removal count each loop
        new_removals = 0

        # Iterate over the grid
        for r in range(rows):
            for c in range(columns):
                
                # Initialize variables to reference rolls and count adjacent rolls
                character = grid[r, c]
                adjacent_roll_count = 0

                # Skip non-roll characters in the grid
                if character != '@':
                    continue

                if r == 0:

                    # Count and remove rolls on corners (they are always accessible)
                    if c == 0 or c == columns - 1:
                        accessible_roll_count += 1
                        grid[r,c] = "."
                        new_removals += 1
                        continue

                    # Check the 5 adjacent rolls to edge rolls; count and remove if 3 or fewer adjacent rolls are found
                    else:
                        if grid[r, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c+1] == "@":
                            adjacent_roll_count += 1

                # Apply similar logic to the bottom row as to the top row
                elif r == rows - 1:

                    if c == 0 or c == columns - 1:
                        accessible_roll_count += 1
                        grid[r,c] = "."
                        new_removals += 1
                        continue

                    else:
                        if grid[r, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c+1] == "@":
                            adjacent_roll_count += 1

                else:

                    # Treat edge columns like top and bottom rolls (do not attempt to check rolls beyond the edges)
                    if c == 0:
                        if grid[r-1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c+1] == "@":
                            adjacent_roll_count += 1

                    elif c == columns -1:
                        if grid[r-1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c] == "@":
                            adjacent_roll_count += 1

                    # Check all 8 adjacent rolls of inner rolls
                    else:
                        if grid[r-1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r-1, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r, c+1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c+1] == "@":
                            adjacent_roll_count += 1
                            
                if adjacent_roll_count < 4:
                    accessible_roll_count += 1
                    grid[r,c] = "."
                    new_removals += 1
    print(grid)
    print("%s of the rolls are accessible by forklift" % accessible_roll_count)
    return grid, accessible_roll_count

accessible_roll_counter(grid)