import numpy as np
import re
import os
from scipy.optimize import linprog

def parse_matrix_data(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    parsed_results = []

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip(): continue
            
            # Parse Joltage Requirements (Vector Z)
            curly_match = re.search(r'\{(.*?)\}', line)
            if not curly_match: continue
            vector_z = np.array([int(x) for x in curly_match.group(1).split(',')], dtype=float)
            
            # Parse Buttons (Parenthetical Portions)
            paren_matches = re.findall(r'\((.*?)\)', line)
            indices_lists = []
            for match in paren_matches:
                indices = [int(x) for x in match.split(',') if x.strip()]
                indices_lists.append(indices)
            
            # Build Matrix A (Rows = Counters, Cols = Buttons)
            num_counters = len(vector_z)
            num_buttons = len(indices_lists)
            matrix_a = np.zeros((num_counters, num_buttons), dtype=float)
            
            for col_idx, button_indices in enumerate(indices_lists):
                for row_idx in button_indices:
                    # Only map if the index is valid for our counters
                    if row_idx < num_counters:
                        matrix_a[row_idx, col_idx] = 1.0
            
            parsed_results.append({
                'matrix_a': matrix_a,
                'vector_z': vector_z
            })
            
    return parsed_results

def solve_joltage_min_sum(A, z):
    # Identify variables there are
    num_vars = A.shape[1]
    
    # Define the objective function the solver will try to minimize (in this case, the sum of all button presses)
    c = np.ones(num_vars) 
    
    # Consider only whole number button presses
    integrality = np.ones(num_vars)
    
    # Call linprog to solve the Mixed-Integer Linear Programming problem
    # Use c as the Objective Vector
    # Use A-eq as the Constraint Matrix
    # Use b_eq as the Constraint Bounds
    # Use integrality as the Domain Constraint
    # Use the HiGHS solver
    res = linprog(c, A_eq=A, b_eq=z, integrality=integrality, method='highs')
    
    if res.success:
        # Return the solution
        return np.round(res.x).astype(int)
    return None

# Define helper variables
data = parse_matrix_data('advent2025_day10_data.txt')
total_button_presses = 0

# Loop over the data and apply the solver to each line, summing the results
for entry in data:
    A = entry['matrix_a']
    z = entry['vector_z']
    
    solution = solve_joltage_min_sum(A, z)
    
    if solution is not None:
        total_button_presses += np.sum(solution)
    else:
        print("Warning: A machine configuration could not be solved.")

print(f"Final Result: {total_button_presses}")