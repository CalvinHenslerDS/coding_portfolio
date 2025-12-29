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
    
    distances = []

    for (i, p1), (j, p2) in combinations(enumerate(coordinates), 2):
        distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**0.5
        distances.append({
            "pair": (i, j),
            "coordinates": (p1, p2),
            "distance": round(distance, 2)
        })
    
    return distances

distances = distance_finder(coordinates)

sorted_distances = sorted(distances, key=lambda x: x['distance'])

def circuit_maker(sorted_distances, coordinates):
    circuit_list = []
    for entry in sorted_distances[:999]:
        p = entry['pair']
        c = entry['coordinates']
        d = entry['distance']
        circuit_list.append((p[0], p[1], d))
    for i in range(1, len(circuit_list)):
        current_item = circuit_list[i]
        previous_item = circuit_list[i-1]
            if current_item[0] == previous_item[0]
    

circuit_maker(sorted_distances, coordinates)

