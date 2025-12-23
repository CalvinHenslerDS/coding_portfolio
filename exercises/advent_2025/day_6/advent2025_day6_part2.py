# import re
# import math
# import numpy as np
# from pathlib import Path

# def load_data_as_list_of_lists():
#     file_path = Path(__file__).parent / "advent2025_day6_data.txt"
#     master_list = []
    
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 tokens = re.findall(r'\d+|\+|\*', line)
                
#                 row = [int(t) if t.isdigit() else t for t in tokens]
                
#                 if row:
#                     master_list.append(row)
                    
#         return master_list

#     except FileNotFoundError:
#         print("File not found.")
#         return []

# math_homework = load_data_as_list_of_lists()

# def homework_completer(math_homework):
#     solutions_list = []
#     for column in zip(*math_homework):
#         working_list_strings = []
#         working_list_string_lengths = []
#         cephalopod_list = []
#         for item in column[:-1]:
#             working_list_strings.append(str(item))
#             working_list_string_lengths.append(len(str(item)))
#         max_string_length = max(working_list_string_lengths)

#         for index in range(0,max_string_length):
#             this_string = ""
#             for item in working_list_strings:
#                 if len(item) > index:
#                     this_string += item[index]
#             this_integer = int(this_string)
#             cephalopod_list.append(this_integer)
            
#         if column[-1] == "+":
#             solution = sum(cephalopod_list)
#         else:
#             solution = math.prod(cephalopod_list)
#         solutions_list.append(solution)
#         print(solution)
#     solution_total = sum(solutions_list)
#     print(solution_total)

test_data = [[1,2,3," ", 3,2,8," "," ",  5,1," ", 6,4," "], 
  [" ",4,5," ", 6,4," "," ",  3,8,7," ", 2,3," "], 
   [" "," ",6, " ",9,8," "," ",  2,1,5," ", 3,1,4],
   ["*"," "," "," ","+"," "," "," ","*"," "," "," ","+"," "," "," "]]

# homework_completer(test_data)

import math
import os

# Get the directory where the script is located
script_directory = os.path.dirname(__file__) 
# Join the directory path with the file name
file_path = os.path.join(script_directory, 'advent2025_day6_data.txt')

try:
    with open(file_path, 'r') as file:
        # rstrip('\n') removes the newline, list() breaks string into characters
        homework_grid = [list(line.rstrip('\n')) for line in file]

except FileNotFoundError:
    print("Error: data.txt not found in the script directory.")

def homework_completer(input_grid):
    for row in input_grid:
        row.append(" ")
    non_integer_items = ["+", "*", " "]
    current_problem_numbers = []
    solutions = []
    for column in zip(*input_grid):
        working_column = ""
        for item in column:
            if item not in non_integer_items:
                working_column += str(item)
            if item == "*" or item == "+":
                working_operator = item
        if working_column != "":
            current_problem_numbers.append(int(working_column))
        else:
            if working_operator == "*":
                solutions.append(math.prod(current_problem_numbers))
                current_problem_numbers = []
            else:
                solutions.append(sum(current_problem_numbers))
                current_problem_numbers = []
    print(solutions)
    solutions_total = sum(solutions)
    print(solutions_total)

homework_completer(homework_grid)
        





# Loop through each row in your list of lists
for row in homework_grid:
    # Slice from the start to index 10
    first_ten = row[:10]
    print(first_ten)