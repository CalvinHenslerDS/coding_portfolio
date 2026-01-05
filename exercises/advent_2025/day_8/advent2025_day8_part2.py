from pathlib import Path
import math
from itertools import combinations

# Import data
directory = Path(__file__).resolve().parent
data = directory / "advent2025_day8_data.txt"

def load_data():
    if not data.exists():
        print(f"Error: Could not find '{data.name}' in {directory}")
        return None
    try:
        content = data.read_text()
        coordinates = [
            [int(val) for val in line.split(",")]
            for line in content.strip().splitlines()
        ]
        return coordinates
    except ValueError as e:
        print(f"Data Error: {e}")
        return None

coordinates = load_data()
if not coordinates:
    exit()

# DSU setup

# Create a list where every box points to itself
parent = list(range(len(coordinates)))
# Set the size of each box (the length of each circuit) equal to 1
size = [1] * len(coordinates)
# Track the number of disjoint sets (circuits)
num_circuits = len(coordinates)

def find(i):
    # Check whether this box is its own leader
    if parent[i] == i:
        return i
    
    # Keep checking one step up the chain until the leader is found
    # Compress the path, so the recursion need not be conducted again for this box
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):

    # Use the num_circuits variable initialized outside of this function
    global num_circuits

    # Find the leader of boxes i and j
    root_i = find(i)
    root_j = find(j)

    if root_i != root_j:
        # Merge smaller circuit into larger one if the leaders are different
        if size[root_i] < size[root_j]:
            root_i, root_j = root_j, root_i
        parent[root_j] = root_i
        # Calculate the size of the combined circuit
        size[root_i] += size[root_j]
        # Decrease the number of circuits by 1 for every successful union
        num_circuits -= 1
        return True
    # If the leaders are the same, they are already in the same circuit
    return False

# Get all pairs calculate their distance
all_edges = []
for i, j in combinations(range(len(coordinates)), 2):
    p1, p2 = coordinates[i], coordinates[j]
    dist = math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))
    all_edges.append((dist, i, j))

# Sort all pairs by distance
all_edges.sort()

last_edge = None

for dist, i, j in all_edges:
    # If union is successful, check if it was the final connection
    if union(i, j):
        if num_circuits == 1:
            last_edge = (i, j)
            break

if last_edge:
    idx1, idx2 = last_edge
    x1 = coordinates[idx1][0]
    x2 = coordinates[idx2][0]
    result = x1 * x2
    print(f"Last connection indices: {idx1} and {idx2}")
    print(f"X coordinates: {x1} and {x2}")
    print(f"Result (Product of X coordinates): {result}")
else:
    print("Could not connect all junction boxes.")