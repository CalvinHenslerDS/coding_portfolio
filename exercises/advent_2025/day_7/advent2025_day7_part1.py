import numpy as np
from pathlib import Path

# Import data as a list of lists of characters (including spaces)

script_directory = Path(__file__).parent
file_path = script_directory / "advent2025_day7_data.txt"

tachyon_manifold = np.genfromtxt(file_path, dtype='U1', delimiter=1, comments=None)

rows, columns = tachyon_manifold.shape

def beam_split_counter(tachyon_manifold):
    split_count = 0
    for r in range(rows):
        for c in range(columns):
                
            character = tachyon_manifold[r, c]
            if character == ".":
                if tachyon_manifold[r-1, c] in ("S", "|"):
                    tachyon_manifold[r, c] = "|"
            elif character == "^":
                if tachyon_manifold[r-1, c] in ("S", "|"):
                    tachyon_manifold[r, c-1] = "|"
                    tachyon_manifold[r, c+1] = "|"
                    split_count += 1
    print(split_count)

beam_split_counter(tachyon_manifold)
    

            