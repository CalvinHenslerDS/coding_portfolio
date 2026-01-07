import pandas as pd
import os

# Import data
script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, 'advent2025_day9_data.txt'), header=None, names=['x', 'y'])
red_tiles = list(df.itertuples(index=False, name=None))

# Collect edges
edges = []
for i in range(len(red_tiles)):
    p1 = red_tiles[i]
    p2 = red_tiles[(i + 1) % len(red_tiles)]
    edges.append((p1, p2))

def is_inside(px, py, poly_points):
    """Ray casting algorithm: check if a point is inside the polygon."""

    # Initialize n equal to the number of coordinate pairs
    n = len(poly_points)
    inside = False

    # Initialize p1x and p1y as the 0th element of the list of coordinate pairs
    p1x, p1y = poly_points[0]
    # Iterate over a list of consecutive integers equal in length to the length of the list
    for i in range(n + 1):
        # Use the modulo operator when initializing p2x and p2y to ensure the "looping" behavior (to close the polygon)
        p2x, p2y = poly_points[i % n]
        # Check whether the y-coordinate of the midpoint of the candidate rectangle is between the y-coordinates of p1 and p2
        if py > min(p1y, p2y) and py <= max(p1y, p2y):
            # Check whether the x-coordinate of the midpoint of the candidate rectangle is to the left of at least one edge
            if px <= max(p1x, p2x):
                # Check whether p1 and p2 form a horizontal line; if not, proceed to linear interpolation
                if p1y != p2y:
                    # Use linear interpolation to find the x-coordinate at which a projected ray would intersect the boundary between p1 and p2
                    xints = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                # Check whether p1 and p2 form a vertical line or if the center of the rectangle lies to the left of the boundary between p1 and p2
                if p1x == p2x or px <= xints:
                    # Toggle inside (if it is toggled an even number of times, it will return False, and the center of the rectangle must be outside the bounds of the polygon)
                    inside = not inside
        # Update p1x and p1y to look at the next pair of coordinates
        p1x, p1y = p2x, p2y
    return inside

def is_valid_rectangle(x1, y1, x2, y2, poly_edges, poly_points):
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    # Allow zero width or height rectangles
    if x_min == x_max or y_min == y_max:
        return True
    
    # Check if center is inside the green zone
    if not is_inside((x_min + x_max) / 2, (y_min + y_max) / 2, poly_points):
        return False

    # Check if any polygon boundary cuts through the rectangle
    for (ex1, ey1), (ex2, ey2) in poly_edges:
        # Vertical edge check
        if ex1 == ex2:
            if x_min < ex1 < x_max:
                if not (max(ey1, ey2) <= y_min or min(ey1, ey2) >= y_max):
                    return False
        # Horizontal edge check
        elif ey1 == ey2:
            if y_min < ey1 < y_max:
                if not (max(ex1, ex2) <= x_min or min(ex1, ex2) >= x_max):
                    return False
    return True

# Create a list of candidate rectangles
candidates = []
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > 0:
            candidates.append((area, x1, y1, x2, y2))

# Sort by area descending
candidates.sort(key=lambda x: x[0], reverse=True)

# Report the first valid rectangle from the descending list (along with its area)
for area, x1, y1, x2, y2 in candidates:
    if is_valid_rectangle(x1, y1, x2, y2, edges, red_tiles):
        print(f"Area: {area}")
        print(f"Between Corners: ({x1}, {y1}) and ({x2}, {y2})")
        break