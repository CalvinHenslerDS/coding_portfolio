# Import data
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

# For each range, iterate over each number in the range and compare the first half to the second half
# Add the number to a list if the first half and the second half are the same
def fake_finder(input_list):
    fake_id_list = []
    for start, end in input_list:
        for number in range(start, end + 1):
            number_string = str(number)
            string_length = len(number_string)
            if (string_length % 2) != 0:
                pass
            else:
                middle_index = string_length // 2
                if number_string[:middle_index] == number_string[middle_index:]:
                    fake_id_list.append(number)

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


