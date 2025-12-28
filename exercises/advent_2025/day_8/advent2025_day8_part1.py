from pathlib import Path
from itertools import combinations

# Get the absolute path to the directory where THIS script is saved
directory = Path(__file__).resolve().parent

# Define the filename
data = directory / "advent2025_day8_data.txt"

def load_data():
    # Check if the file actually exists in that folder
    if not data.exists():
        print(f"Error: Could not find '{data.name}' in {directory}")
        return None

    # Read and parse
    try:
        content = data.read_text()
        
        # Create list of lists:
        # 1. splitlines() handles different OS line endings
        # 2. strip() removes empty lines at the end
        # 3. int() converts the text to numbers
        coordinates = [
            [int(val) for val in line.split(",")]
            for line in content.strip().splitlines()
        ]
        
        print(f"Successfully imported {len(coordinates)} rows from {directory}")
        return coordinates

    except ValueError as e:
        print(f"Data Error: Ensure the file contains only numbers and commas. {e}")
        return None

# Execute the import
coordinates = load_data()

# Verification: Print the first 3 rows
if coordinates:
    for row in coordinates[:3]:
        print(row)

def distance_finder(coordinates):
    distance_map = {}
    for (i, p1), (j, p2) in combinations(enumerate(coordinates), 2):
        distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**0.5
        distance_map[(i, j)] = distance
    
    return distance_map
