import pandas as pd
import os

# Import data
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'advent2025_day9_data.txt')

coords_df = pd.read_csv(file_path, header=None, names=['X', 'Y'])

def rectangle_maximizer(coords_df):
    max_area = 0
    for x1, y1 in coords_df.values:
        for x2, y2 in coords_df.values:
            delta_x = abs(x1 - x2) + 1
            delta_y = abs(y1 - y2) + 1
            area = delta_x * delta_y
            if area > max_area:
                max_area = area
    print("The maximum area is %s" % max_area)

rectangle_maximizer(coords_df)