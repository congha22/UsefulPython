# This will translate all {{i18n:KEY}} from mail.json to VALUE found in default.json


import os
import json5

def find_i18n_keys(data):
    keys = []

    def find_i18n_keys_recursive(value):
        i18n_keys = []

        if isinstance(value, list):
            for item in value:
                i18n_keys.extend(find_i18n_keys_recursive(item))
        elif isinstance(value, dict):
            for key, item in value.items():
                i18n_keys.extend(find_i18n_keys_recursive(item))
        elif isinstance(value, str):
            i18n_keys.extend(find_i18n_keys_in_string(value))

        return i18n_keys

    def find_i18n_keys_in_string(value):
        i18n_keys = []
        index = 0

        while index < len(value):
            start_index = value.find("{{i18n:", index)
            if start_index == -1:
                break

            end_index = value.find("}}", start_index)
            if end_index == -1:
                break

            key_start = start_index + len("{{i18n:")
            key_end = end_index

            captured_string = value[key_start:key_end]
            i18n_keys.append(captured_string)

            # Move to the next occurrence
            index = end_index + len("}}")

        return i18n_keys

    keys = find_i18n_keys_recursive(data)
    return keys

def replace_i18n_keys_with_values(data, i18n_keys, default_data):
    for key in i18n_keys:
        if key in default_data:
            value = default_data[key]
            data = replace_i18n_key_with_value(data, key, value)
    return data

def replace_i18n_key_with_value(data, key, value):
    if isinstance(data, list):
        return [replace_i18n_key_with_value(item, key, value) for item in data]
    elif isinstance(data, dict):
        return {k: replace_i18n_key_with_value(v, key, value) for k, v in data.items()}
    elif isinstance(data, str):
        return data.replace(f"{{{{i18n:{key}}}}}", value)
    else:
        return data

def process_files(input_folder, output_folder, default_data):
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path) as input_file:
                data = json5.load(input_file)

            # Find i18n keys in the current file
            i18n_keys = find_i18n_keys(data)

            # Replace i18n keys with values in the current file
            data_updated = replace_i18n_keys_with_values(data, i18n_keys, default_data)

            # Write the updated data to the output file
            with open(output_path, 'w') as output_file:
                json5.dump(data_updated, output_file, indent=2)

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    with open('default.json') as default_file:
        default_data = json5.load(default_file)

    process_files(input_folder, output_folder, default_data)
