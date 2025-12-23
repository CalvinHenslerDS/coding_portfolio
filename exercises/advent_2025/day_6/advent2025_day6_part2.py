import math
import os

# Import data as a list of lists of characters (including spaces)

script_directory = os.path.dirname(__file__) 
file_path = os.path.join(script_directory, 'advent2025_day6_data.txt')

try:
    with open(file_path, 'r') as file:
        homework_grid = [list(line.rstrip('\n')) for line in file]

except FileNotFoundError:
    print("Error: data.txt not found in the script directory.")

def homework_completer(input_grid):

    # Add a padding column to the grid to trigger the solution append action for the final problem set later
    for row in input_grid:
        row.append(" ")

    # Initialize variables to facilitate tracking of problems (as they're built) and solutions (as they're calculated)
    non_integer_items = ["+", "*", " "]
    current_problem_numbers = []
    solutions = []

    # Iterate over the columns in the grid
    for column in zip(*input_grid):

        # Initialize a string to build each number in the math problem IAW cephalopod math conventions
        working_column = ""

        for item in column:

            # If an item in the column is an integer, add it to the working_column string
            if item not in non_integer_items:
                working_column += str(item)

            # If an item in the column is an operator, store it as the operator to be used when the solution is calculated for the associated problem
            if item == "*" or item == "+":
                working_operator = item

        # Append the working_column string to the current_problem_numbers list to facilitate calculation
        if working_column != "":
            current_problem_numbers.append(int(working_column))

        # If the column was all spaces, perform the calculation with the stored current_problem_numbers and working_operator
        # Append the result to solutions and reset current_problem_numbers in preparation for the next calculation
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