# Import data
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

    # Initialize a list store the max voltage for each bank in the grid as well as the target battery chain length
    max_joltages = []
    target_length = 12

    # Iterate over the grid to evaluate each bank
    for powerbank in power_grid:

        # Initialize a list to facilitate Monotonic Stack logic
        stack = []

        # Initialize a variable to limit the number of batteries we can skip (so we don't run out of batteries in our bank to meet our target)
        max_skip = len(powerbank) - target_length

        for battery in powerbank:

            # Replace a weaker battery on the top of the stack when we encounter a stronger one as long as we have enough left in the bank to complete our chain
            while max_skip > 0 and stack and stack[-1] < battery:
                stack.pop()
                max_skip -= 1
            stack.append(battery)

        # Append the first 12 batteries in our stack in order (as an integer) to our max_joltages list
        max_dozen_string = "".join(stack[:target_length])
        max_joltages.append(int(max_dozen_string))

    total_joltage = sum(max_joltages)

    print("The total max joltage is %s jolts" % total_joltage)

    return max_joltages, total_joltage

joltage_maxxing(power_grid)