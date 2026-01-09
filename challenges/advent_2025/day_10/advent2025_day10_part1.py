import numpy as np
from itertools import product
import re
import os

def parse_matrix_data(filename):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    # Initialize an empty list in which to store the data
    parsed_results = []

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            
            # Parse Vector Y (length determines the matrix width before transpose)
            bracket_match = re.search(r'\[(.*?)\]', line)
            if not bracket_match: continue
            bracket_content = bracket_match.group(1)
            # . is even (0), # is odd (1)
            vector_y = np.array([1 if char == '#' else 0 for char in bracket_content])
            
            # Parse Parenthetical Portions
            paren_matches = re.findall(r'\((.*?)\)', line)
            indices_lists = []
            for match in paren_matches:
                indices = [int(x) for x in match.split(',') if x.strip()]
                indices_lists.append(indices)
            
            # Define dimensions for the button matrix
            num_rows = len(indices_lists)
            num_cols = len(vector_y) 
            
            # Initialize an empty matrix
            raw_matrix = np.zeros((num_rows, num_cols), dtype=int)
            
            # Populate the empty matrix in accordance with the button wiring schematic
            for row_idx, col_indices in enumerate(indices_lists):
                for c_idx in col_indices:
                    if c_idx < num_cols:
                        raw_matrix[row_idx, c_idx] = 1
            
            # Transpose the input matrix
            matrix_a = raw_matrix.T
            
            # Parse curly brackets
            curly_match = re.search(r'\{(.*?)\}', line)
            list_z = []
            if curly_match:
                list_z = [int(x) for x in curly_match.group(1).split(',')]
            
            # Create a dictionary of the inputs: desired lighting schema, matrix of button wiring diagrams, and joltage requirements
            parsed_results.append({
                'vector_y': vector_y,
                'matrix_a': matrix_a,
                'curly_list': list_z
            })
            
    return parsed_results

data = parse_matrix_data('advent2025_day10_data.txt')

def solve_minimal_sum_gf2(A, y):

    # Store the number of rows of matrix A as m and the number of columns as n
    m, n = A.shape
    # Horizontally stack the target vector y with the input matrix A
    # Use the modulo operator to map all evens to 0 and odds to 1 to ensure the the entire input is binary in nature
    A_aug = np.hstack((A, y.reshape(-1, 1))) % 2
    

    pivot_row = 0
    pivot_columns = []
    
    # Perform Full Gauss-Jordan Elimination
    for j in range(n):
        if pivot_row >= m: break
        
        # Find the first 1 in column j
        k = pivot_row + np.argmax(A_aug[pivot_row:, j])
        if A_aug[k, j] == 0: continue
        
        # Switch the current row with the identified pivot row (containing the first 1 in column j)
        A_aug[[pivot_row, k]] = A_aug[[k, pivot_row]]
        
        # If there are other 1s in the column, eliminate them by adding the pivot row to them (resulting in an even element) and computing modulo 2
        for i in range(m):
            if i != pivot_row and A_aug[i, j] == 1:
                A_aug[i] = (A_aug[i] + A_aug[pivot_row]) % 2
        
        # Append the pivot column and move on to the next row (simulating a diagonal stair-step motion along the input matrix)
        pivot_columns.append(j)
        pivot_row += 1

    # Identify Free Variables by subtracting the set of pivot columns from all indices
    all_indices = set(range(n))
    pivot_set = set(pivot_columns)
    free_indices = sorted(list(all_indices - pivot_set))

    # Define a function to get a solution based on free variable choices
    def get_solution(free_values):

        # Initialize a vector in which to store the minimum number of button presses
        x = np.zeros(n, dtype=int)
        # Set free variables
        for index, value in zip(free_indices, free_values):
            x[index] = value
        # Set pivot variables based on Row Reduced Echelon Form rows
        for i, pivot_column in enumerate(pivot_columns):
            # The value is the augmented constant XORed with any free variables in that row
            row_sum = A_aug[i, -1]
            for f_idx in free_indices:
                if A_aug[i, f_idx] == 1:
                    row_sum ^= x[f_idx]
            x[pivot_column] = row_sum
        return x

    # 4. Search combinations of free variables for minimum sum
    best_x = None
    min_sum = float('inf')
    
    # Iterate through all 2^k combinations of free variables
    for free_vals in product([0, 1], repeat=len(free_indices)):
        current_x = get_solution(free_vals)
        current_sum = np.sum(current_x)
        if current_sum < min_sum:
            min_sum = current_sum
            best_x = current_x
            
    return best_x

# Example usage with your matrix
total_button_presses = 0
for i in range(len(data)):
    A = data[i]['matrix_a']
    y = data[i]['vector_y']
    solution = solve_minimal_sum_gf2(A, y)
    total_button_presses += sum(solution)

print(total_button_presses)