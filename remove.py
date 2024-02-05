# This will remove everything from the beginning to the "Entries: ", and remove everything from the last "}"

import os
import json

input_folder_path = 'output'
output_folder_path = 'remove'

# Ensure output folder exists
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Process all files in the output folder
for filename in os.listdir(input_folder_path):
    input_file_path = os.path.join(input_folder_path, filename)
    output_file_path = os.path.join(output_folder_path, filename)

    with open(input_file_path, 'r') as input_file:
        data = input_file.read()

    # Find the index of the first occurrence of "Entries"
    entries_index = data.find("Entries: ")

    if entries_index != -1:
        # Trim the data from the beginning until the first "Entries"
        trimmed_data = data[entries_index + len("Entries: "):]

        # Find the index of the first '}'
        closing_brace_index = trimmed_data.find("}")

        if closing_brace_index != -1:
            # Remove everything after the first '}'
            final_trimmed_data = trimmed_data[:closing_brace_index + 1]

            # Write the final trimmed data to the output file in the remove folder
            with open(output_file_path, 'w') as output_file:
                output_file.write(final_trimmed_data)

            print(f"Final trimmed data written to {output_file_path}")
        else:
            print(f"No '}}' found after 'Entries' in {filename}.")
    else:
        print(f"No 'Entries' found in {filename}.")
