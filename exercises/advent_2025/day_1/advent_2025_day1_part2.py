from pathlib import Path

# Load the elves' instructions from the text file in the project folder
project_directory = Path(__file__).parent.resolve()
data = project_directory/"combination.txt"

try:
    with open(data, 'r') as f:
        instructions_list = [line.strip() for line in f]

    print(f"Successfully loaded {len(instructions_list)} instructions.")
    print(instructions_list[:5]) # Display the first 5 items to verify

except FileNotFoundError:
    print(f"Error: The file '{data}' was not found.")

# Convert the list of strings into a list of positive (R) or negeative (L) integers
def list_converter(instructions_list):

    signed_integer_instructions = []

    for item in instructions_list:

        direction = item[0]
        magnitude_int = int(item[1:])

        if direction == "R":
            signed_value = magnitude_int

        else:
            signed_value = -magnitude_int
        signed_integer_instructions.append(signed_value)

    return signed_integer_instructions

# Count the zeros passed while executing the instructions
def zero_counter(instructions_list):

    signed_instructions_list = list_converter(instructions_list)
    #print(signed_instructions_list)
    zero_count = 0
    value = 50

    for item in signed_instructions_list:
        #print(item)
        if item < 0:
            if value == 0:
                 if item == 0:
                      pass
                 else:
                    zero_count += -1 + (100 - value - item) // 100
            else:
                zero_count += (100 - value - item) // 100
        else:
            zero_count +=  (value + item) // 100
        #print(value, item, zero_count)
        value = (value + item) % 100
        
        
    
    return zero_count

print(zero_counter(instructions_list))
