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

    # Iterate over the grid to evaluate each bank
    for powerbank in power_grid:

        # Initialize variables to facilitate candidate battery comparisons
        candidate_batteries_1 = []
        candidate_battery_dozens = []
        candidate_batteries_2 = []
        candidate_batteries_3 = []
        candidate_batteries_4 = []
        candidate_batteries_5 = []
        candidate_batteries_6 = []
        candidate_batteries_7 = []
        candidate_batteries_8 = []
        candidate_batteries_9 = []
        candidate_batteries_10 = []
        candidate_batteries_11 = []
        candidate_battery_12 = 0
        this_battery_string_working = []
        this_powerbank_max_joltage = 0

        # Iterate over the batteries in the bank, and make a list of all batteries with the highest joltage

        for i, battery in enumerate(powerbank[:-11]):
            if i == len(powerbank) - 12:
                candidate_battery_dozens.append(powerbank[-12:])
            this_battery_joltage = int(battery)

            if this_battery_string_working == []:
                this_battery_string_working.append(battery)

            elif this_battery_joltage == candidate_batteries_1[0][1]:
                candidate_batteries_1.append((i, this_battery_joltage))

            elif this_battery_joltage > candidate_batteries_1[0][1]:
                candidate_batteries_1 = [(i, this_battery_joltage)]
        this_battery_string = "".join(this_battery_string_working)
        # Iterate over the batteries in the bank to the right of each candidate first battery
        for index, joltage in candidate_batteries_1:

            next_index = index + 1

            for battery in powerbank[next_index:]:

                this_battery_joltage = int(battery)

                if candidate_battery_2 == 0:
                    candidate_battery_2 = this_battery_joltage
                    this_powerbank_max_joltage = (joltage * 10) + this_battery_joltage
                    
                elif this_battery_joltage > candidate_battery_2:
                    candidate_battery_2 = this_battery_joltage
                    this_powerbank_max_joltage = (joltage * 10) + this_battery_joltage

        # Once the maximum possible joltage in the bank is found, add it to the list of max joltages
        max_joltages.append(this_powerbank_max_joltage)

    total_joltage = 0

    # Calculate the sum of the max possible joltage for each bank
    for max_joltage in max_joltages:
        total_joltage = total_joltage + max_joltage
    
    return total_joltage

print("The total, max joltage of the grid is %s jolts" % joltage_maxxing(power_grid))