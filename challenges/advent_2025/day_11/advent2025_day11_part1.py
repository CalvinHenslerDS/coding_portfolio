import pathlib

# Get the directory where this script is saved
current_dir = pathlib.Path(__file__).parent

# Define the filename (ensure this matches your .txt file name)
filename = "advent2025_day11_data.txt"
file_path = current_dir / filename

# Read and process the data
list_of_lists = []

with open(file_path, "r") as file:
    for line in file:
        # Strip whitespace and split by the colon to separate the key
        if ":" in line:
            parts = line.split(":", 1)
            # The second part contains the items; split them by space
            items = parts[1].strip().split()
            # Insert the key as the first element if you want it included
            list_of_lists.append([parts[0].strip()] + items)

# Verify the result
print(list_of_lists[:3]) # Prints first three sub-lists

def path_finder(list_of_lists):
    paths = []
    for device in list_of_lists:
        if device[0] == "you":
            for output in device[1:]:
                paths.append([device[0], output])
    for i in range(len(paths)):
        for device in list_of_lists:
            if device[0] == paths[i][-1]:
                for output in device[1:]:
              #      paths.append(paths[i])
                    paths[i].append(output)


    return paths
        
test = path_finder(list_of_lists)
print(test)
