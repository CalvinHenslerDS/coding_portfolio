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

def load_list_data():
    current_directory = Path(__file__).parent
    file_path = current_directory / "advent2025_day5_data2.txt"
    
    data_list = []
    
    try:
        with file_path.open('r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line: 
                    data_list.append(int(clean_line))
        
        return data_list
    
    except FileNotFoundError:
        print(f"Error: {filename} not found in {current_directory}")
        return []
    except ValueError as e:
        print(f"Error: Found non-numeric data in the file: {e}")
        return []

data_ranges = get_data()
id_list = load_list_data()

def check_freshness(data_ranges, id_list):
    fresh_id_list = []
    for id in id_list:
        for start, end in data_ranges:
            if int(id) > int(start) and int(id) < int(end):
                fresh_id_list.append(id)
    

    print(len(set(fresh_id_list)))

check_freshness(data_ranges, id_list)