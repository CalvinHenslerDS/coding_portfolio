import re
import math
from pathlib import Path

# Import the data
def load_data_as_list_of_lists():
    file_path = Path(__file__).parent / "advent2025_day6_data.txt"
    master_list = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                tokens = re.findall(r'\d+|\+|\*', line)
                
                row = [int(t) if t.isdigit() else t for t in tokens]
                
                if row:
                    master_list.append(row)
                    
        return master_list

    except FileNotFoundError:
        print("File not found.")
        return []

math_homework = load_data_as_list_of_lists()

def homework_completer(math_homework):

    # Initialize an empty list to store solutions as they are calculated
    solutions_list = []

    # Iterate over the columns; sum them if the last element is '+', multiply them otherwise
    for column in zip(*math_homework):
        if column[-1] == "+":
            solution = sum(column[:-1])
        else:
            solution = math.prod(column[:-1])
        solutions_list.append(solution)

    solution_total = sum(solutions_list)
    print(solution_total)

homework_completer(math_homework)
        