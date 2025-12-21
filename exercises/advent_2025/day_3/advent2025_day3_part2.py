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
        candidate_battery_dozens = []
        this_battery_string = ""
        this_powerbank_max_joltage = 0
        stored_next_index = 0

        # Iterate over the batteries in the bank, and make a list of all batteries with the highest joltage

        for i, battery in enumerate(powerbank[:-11]):
            # if i == len(powerbank) - 12:
            #     candidate_battery_dozens.append(int(powerbank[-12:]))
            this_battery_joltage = int(battery)
            if candidate_battery_dozens == []:
                candidate_battery_dozens.append((i, battery))
            elif this_battery_joltage == candidate_battery_dozens[0][1]:
                candidate_battery_dozens.append((i, battery))
            elif this_battery_joltage > candidate_battery_dozens[0][1]:
                candidate_battery_dozens = [(i, battery)]

        # Iterate over the batteries in the bank to the right of each candidate first battery
        while len(this_battery_string) < 12:
            for index, joltage in candidate_battery_dozens:
                this_battery_string = joltage
                if stored_next_index == 0:
                    next_index = index + 1
                else:
                    next_index = stored_next_index

                for number in range(-10, 0):
                    current_window = powerbank[next_index : number]
                    candidate_battery = 0
                    for battery in current_window:

                        this_battery_joltage = int(battery)
                        next_index += 1
                        if this_battery_joltage > candidate_battery:
                            candidate_battery = this_battery_joltage
                            stored_next_index = next_index     
                    this_battery_string += str(candidate_battery)
                joltage = int(this_battery_string)



        
                

        # Once the maximum possible joltage in the bank is found, add it to the list of max joltages
        max_joltages.append(this_powerbank_max_joltage)

    total_joltage = 0

    # Calculate the sum of the max possible joltage for each bank
    for max_joltage in max_joltages:
        total_joltage = total_joltage + max_joltage
    
    return total_joltage

print("The total, max joltage of the grid is %s jolts" % joltage_maxxing(power_grid))