from pathlib import Path

def get_variants(shape_lines):
    """Generates all 8 unique rotations/flips as lists of row-bitmasks."""
    # Rotate the shape 90 degrees clockwise
    def rotate(g): return ["".join(r) for r in zip(*g[::-1])]

    # Mirror the shape horizontally
    def flip(g): return [r[::-1] for r in g]
    
    unique_patterns = set()
    curr = shape_lines

    # Rotate the shape 4 times
    # After each rotation, add both the rotated version and a flipped version to a set
    for _ in range(4):
        curr = rotate(curr)
        unique_patterns.add(tuple(curr))
        unique_patterns.add(tuple(flip(curr)))
    
    variants = []
    for p in unique_patterns:
        h, w = len(p), len(p[0])
        # Use list comprehension to process each row in the shape using a Bitwise Left Shift
        mask = [sum(1 << c for c, char in enumerate(row) if char == '#') for row in p]
        # Store the width, height, and bit masks in a variants dictionary
        variants.append({'w': w, 'h': h, 'mask': mask})
    return variants

def solve_region(width, height, counts, all_shapes):
    # Initialize a master list of all individual presents that must fit into the box
    pieces_to_place = []
    # Add the presents in the data set to the master list
    for s_id, qty in enumerate(counts):
        for _ in range(qty):
            pieces_to_place.append(all_shapes[s_id])
            
    # Prioritize larger pieces first
    pieces_to_place.sort(key=lambda v: (v[0]['w'] * v[0]['h']), reverse=True)
    
    # Initialize a list of empty bits
    grid = [0] * height

    def backtrack(idx):
        # If the index reaches the end of the list, every piece is placed
        if idx == len(pieces_to_place):
            return True
        
        # Try each of the 8 rotations/flips for the current piece
        for variant in pieces_to_place[idx]:
            v_h, v_w = variant['h'], variant['w']
            v_mask = variant['mask']
            
            # Try every valid top-left corner (r, c)
            for r in range(height - v_h + 1):
                for c in range(width - v_w + 1):
                    # Check for collisions
                    can_place = True
                    for i in range(v_h):
                        # Take the piece's bit mask for row i, shift it over by c columns, and compare it to the grid row using a bitwise AND
                        if grid[r + i] & (v_mask[i] << c):
                            can_place = False
                            break
                    
                    if can_place:
                        # If can_place remains True, use bitwise OR to flip the grid's bits from 0 to 1, stamping the piece into the grid
                        for i in range(v_h):
                            grid[r + i] |= (v_mask[i] << c)
                        
                        # Place the next piece
                        if backtrack(idx + 1):
                            return True
                        
                        # If the next piece can't fit, use bitwise AND NOT to flip the bits back to 0 and try the next coordinate or rotation
                        for i in range(v_h):
                            grid[r + i] &= ~(v_mask[i] << c)
        return False

    return backtrack(0)

def solve():
    # Import data
    data_file = Path(__file__).parent / "advent2025_day12_data.txt"

    if not data_file.exists():
        print(f"Error: {data_file.name} not found.")
        return

    shape_areas = {}
    regions = []
    
    with open(data_file, 'r') as f:
        current_shape_id = None
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Detect the shape header to start counting area
            if ":" in line and "x" not in line:
                try:
                    current_shape_id = int(line.replace(":", ""))
                    shape_areas[current_shape_id] = 0
                except ValueError:
                    pass
            
            # Detect region lines and store them
            elif "x" in line and ":" in line:
                regions.append(line)
            
            elif current_shape_id is not None:
                shape_areas[current_shape_id] += line.count('#')

    # Convert dictionary to a sorted list of areas
    sorted_ids = sorted(shape_areas.keys())
    area_list = [shape_areas[i] for i in sorted_ids]
    
    print(f"Detected Shape IDs: {sorted_ids}")
    print(f"Detected Shape Areas: {area_list}")

    valid_count = 0
    for line in regions:
        try:
            meta, counts_str = line.split(':')
            w, h = map(int, meta.split('x'))
            counts = list(map(int, counts_str.strip().split()))
            
            # Calculate the total number of square units available in the box
            grid_area = w * h
            # Calculate the sum of the areas of every individual piece
            total_required = sum(q * a for q, a in zip(counts, area_list))
            
            # If the pieces are less than or equal to the box area, increment valid_count
            if total_required <= grid_area:
                valid_count += 1
        except Exception as e:
            continue

    print(f"Total valid regions: {valid_count}")

if __name__ == "__main__":
    solve()