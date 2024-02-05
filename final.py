# This will warp the KEY to "KEY" to be a proper .json

import os
import json5

# Specify the input and output folders
input_folder = 'remove'
output_folder = 'final'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        # Construct the full path for the input and output files
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename)

        # Read the original JSON file
        with open(input_filepath, 'r') as file:
            data = json5.load(file)

        # Create a new dictionary to store the modified data
        new_data = {}

        # Iterate through the original data
        for key, value in data.items():
            # Wrap the key in "KEY" and store in the new dictionary
            new_key = f'"KEY_{key}"'
            new_data[new_key] = value

        # Write the new data to the output file in the 'final' folder
        with open(output_filepath, 'w') as file:
            json5.dump(new_data, file, indent=2)

        print(f"Conversion complete for {filename}. Check {output_filepath} for the result.")
