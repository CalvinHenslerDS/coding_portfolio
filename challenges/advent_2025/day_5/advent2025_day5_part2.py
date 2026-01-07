from pathlib import Path

# Import data
def get_data():
    current_directory = Path(__file__).parent
    file_path = current_directory / "advent2025_day5_data1.txt"
    
    ranges = []
    
    try:
        content = file_path.read_text().splitlines()
        
        for line in content:
            if '-' in line:
                start, end = map(int, line.strip().split('-'))
                ranges.append((start, end))
                
        return ranges

    except FileNotFoundError:
        print("File not found. Make sure the .txt and .py files are in the same folder.")
        return []

data_ranges = get_data()

def fresh_ingredient_list(data_ranges):

    # Sort the ID ranges to facilitate merging
    sorted_ranges = sorted(data_ranges)

    # Initialize an empty list to store the merged ranges
    merged_ranges = []

    # Set the current_start and current_end to enable comparison of neighboring ranges
    current_start, current_end = sorted_ranges[0]

    # If the start of the next range overlaps with or butts up against the end of the current range, merge them
    for next_start, next_end in sorted_ranges[1:]:
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)

        # If there is no overlap, append the new range to merged_ranges
        else:
            merged_ranges.append((current_start,current_end))
            current_start, current_end = next_start, next_end

    merged_ranges.append((current_start,current_end))
    
    fresh_id_count = 0

    # Sum the differences between the upper and lower bound of each range (this represents the quantity of unique IDs in each range)
    for start, end in merged_ranges:
        fresh_id_count += (end - start + 1)

    print(fresh_id_count)
    return fresh_id_count

fresh_ingredient_list(data_ranges)