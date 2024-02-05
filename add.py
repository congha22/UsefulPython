# This will generate a string from all filename found in a folder

import os

dialogue_folder = "dialogue"  # Replace with the actual path to your "dialogue" folder

# Create a list of filenames in the "dialogue" folder without extensions
dialogue_files = [os.path.splitext(file)[0] for file in os.listdir(dialogue_folder)]

# Print out filenames in the specified form on the same line
print(','.join([f'Characters/Dialogue/{filename}' for filename in dialogue_files]))