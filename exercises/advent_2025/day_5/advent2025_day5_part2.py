from pathlib import Path

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
    sorted_ranges = sorted(data_ranges)
    merged_ranges = []
    current_start, current_end = sorted_ranges[0]

    for next_start, next_end in sorted_ranges[1:]:
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start,current_end))
            current_start, current_end = next_start, next_end
    merged_ranges.append((current_start,current_end))
    
    fresh_id_count = 0

    for start, end in merged_ranges:
        fresh_id_count += (end - start + 1)

    print(fresh_id_count)
    return fresh_id_count

fresh_ingredient_list(data_ranges)