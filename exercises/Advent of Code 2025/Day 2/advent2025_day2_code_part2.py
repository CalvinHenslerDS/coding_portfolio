# import data
from pathlib import Path

project_directory = Path(__file__).parent.resolve()
file_path = project_directory / "advent2025_day2_data.txt"

ranges_list = []

try:
    with open(file_path, 'r') as f:
        content = f.read().strip()

        ranges_list = [
            tuple(map(int, part.split('-'))) 
            for part in content.split(',')
        ]

    print(f"Loaded ranges: {ranges_list}")

except FileNotFoundError:
    print("File not found.")

def fake_finder(input_list):
    # Initiate an empty list to store fake IDs in
    fake_id_list = []

    # Iterate over each range bookended by the tuple in the input data
    for start, end in input_list:
        for number in range(start, end + 1):

            # Convert each number to a string and find the length of that string
            number_string = str(number)
            string_length = len(number_string)

            # Iterate over half of the length of the string
            for i in range(1,((string_length//2)+1)):

                # If a factor is found, split the string into that many equal length parts
                if string_length % i == 0:
                    number_of_segments = string_length / i
                    segments = [number_string[j : j + i] for j in range(0, len(number_string), i)]

                    # Initiate a boolean to track whether all parts match each other
                    are_matching = True

                    # Initiate a counter to facilitate the while loop for checking for repeats
                    current_element = 0

                    # Loop over all elements of the split string
                    # If they all match, add the ID to the fake ID list (as an integer)
                    # If not, try again for another factor
                    while current_element != (number_of_segments-1):
                        if segments[current_element] != segments[current_element+1]:
                            are_matching = False
                        current_element += 1
                    if are_matching == True:
                        print(number_string)
                        fake_id_list.append(int(number_string))

                        # If a pattern is found, break from the loop to avoid double-counting
                        break

    return fake_id_list

# Sum the elements of fake_id_list
def fake_id_summer(input_list):
    fake_id_sum = 0
    for id in input_list:
        fake_id_sum += id
    print(fake_id_sum)

# Call the functions
fake_id_list = fake_finder(ranges_list)
fake_id_summer(fake_id_list)


