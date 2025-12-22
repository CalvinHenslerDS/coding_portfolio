import numpy as np
from pathlib import Path

script_directory = Path(__file__).parent
file_path = script_directory / "advent2025_day4_data.txt"

grid = np.genfromtxt(file_path, dtype='U1', delimiter=1, comments=None)

rows, columns = grid.shape

def accessible_roll_counter(grid):
    accessible_roll_count = 0
    new_removals = -1
    while new_removals != 0:
        new_removals = 0
        for r in range(rows):
            for c in range(columns):
                
                character = grid[r, c]
                adjacent_roll_count = 0
                if character != '@':
                    continue
                if r == 0:
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
                        if grid[r+1, c-1] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c] == "@":
                            adjacent_roll_count += 1
                        if grid[r+1, c+1] == "@":
                            adjacent_roll_count += 1
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