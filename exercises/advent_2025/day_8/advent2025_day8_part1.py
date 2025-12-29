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
        
        print(f"Successfully imported {len(coordinates)} rows from {directory}")
        return coordinates

    except ValueError as e:
        print(f"Data Error: Ensure the file contains only numbers and commas. {e}")
        return None

coordinates = load_data()

# 1. Standard DSU/Union-Find implementation

# Create a list where every box points to itself
parent = list(range(len(coordinates)))
# Set the size of each box (the length of each circuit) equal to 1
size = [1] * len(coordinates)

def find(i):
    # Check whether this box is its own leader
    if parent[i] == i:
        return i
    
    # Keep checking one step up the chain until the leader is found
    # Compress the path, so the recursion need not be conducted again for this box
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):

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

# Call the union functino for the shortest 1000 edges
for dist, i, j in all_edges[:1000]:
    union(i, j)

# Get sizes of all unique circuits
final_sizes = [size[i] for i in range(len(coordinates)) if parent[i] == i]
final_sizes.sort(reverse=True)

# Multiply the top 3 circuit sizes (node counts)
result = final_sizes[0] * final_sizes[1] * final_sizes[2]
print(f"Result: {result}")