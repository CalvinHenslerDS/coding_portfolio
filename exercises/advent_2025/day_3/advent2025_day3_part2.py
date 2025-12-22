# import data
from pathlib import Path

project_directory = Path(__file__).parent.resolve()
file_path = project_directory / "advent2025_day3_data.txt"

try:
    with open(file_path, 'r') as f:
        power_grid = [line.strip() for line in f if line.strip()]

    print(f"Loaded powerbanks: {power_grid}")

except FileNotFoundError:
    print("File not found.")

def joltage_maxxing(power_grid):

    # Initialize a list to store the max voltage for each bank in the grid
    max_joltages = []
    target_length = 12

    # Iterate over the grid to evaluate each bank
    for powerbank in power_grid:
        stack = []
        max_skip = len(powerbank) - target_length

        for battery in powerbank:
            while max_skip > 0 and stack and stack[-1] < battery:
                stack.pop()
                max_skip -= 1
            stack.append(battery)
        max_dozen_string = "".join(stack[:target_length])
        max_joltages.append(int(max_dozen_string))

    total_joltage = sum(max_joltages)

    print("The total max joltage is %s jolts" % total_joltage)

    return max_joltages, total_joltage

joltage_maxxing(power_grid)