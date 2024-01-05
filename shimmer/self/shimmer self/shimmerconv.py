import os
import json
import re

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
shimmer_path = os.path.join(script_directory, 'shimmer.json')
shimmer2_path = os.path.join(script_directory, 'shimmer2.json')

# Read shimmer.json
with open(shimmer_path, 'r') as shimmer_file:
    shimmer_data = json.load(shimmer_file)

# Ensure 'Bloom' key is present and initialize it as an empty list if not
if 'Bloom' not in shimmer_data:
    shimmer_data['Bloom'] = []

# Create a set to track processed block names
processed_block_names = set()

# Create a list to store the processed items
processed_blocks = []

# Read lightblocks.txt
with open('lightblocks.txt', 'r') as lightblocks_txt:
    # Use regular expressions to extract block information and color from item name
    block_pattern = re.compile(r"Block\{(.*?)\}(\[.*?\])? -> (\d+)")
    blocks = block_pattern.findall(lightblocks_txt.read())

# Update shimmer_data based on lightblocks information
for block_name, properties, light_level in blocks:
    # Check if the block name is already present in processed_block_names
    if block_name in processed_block_names:
        continue  # Skip processing if the block name is already processed

    color = "#orange"  # Default color if not found

    # Rule 1: Look for a color from the color reference list in the name of the item
    for color_name, color_info in shimmer_data['ColorReference'].items():
        if color_name in block_name:
            color = f"#{color_name}"
            break  # Break out of the loop if color is found
    else:
        # Rule 2: Look for 'soul' in the name and assign dark blue to any items that have it
        if 'soul' in block_name:
            color = "#dark_blue"

        # Rule 3: Look for 'redstone' in the name and assign dark red to any items that have it
        elif 'redstone' in block_name:
            color = "#dark_red"

        # Rule 4: If the name contains XP, experience, or knowledge with word boundaries and no letters on either side, set the color to lime
        elif re.search(r'(?<![a-zA-Z])(?:XP|experience|knowledge)(?![a-zA-Z])', block_name, re.IGNORECASE):
            color = "#lime"

    # Debug: Print information before updating
    print(f"Updating block_name: {block_name}, color: {color}, lightLevel: {light_level}")

    # Create a new LightBlock item with updated information
    new_lightblock = {
        "block": block_name,
        "color": color,
        "radius": int(light_level)
    }

    # Check if properties are specified and add them to the "state" section if present
    if properties:
        # Extract properties from the string inside the square brackets
        property_list = re.findall(r"(\w+=[^,\]]+)", properties)
        if property_list:
            # Create the "state" dictionary and add properties to it
            state_dict = {prop.split('=')[0]: prop.split('=')[1] for prop in property_list}

            # Check if the "on" state is present and set it to "true" in the "state" dictionary
            if state_dict.get("on") == "true":
                new_lightblock['state'] = {"on": "true"}

    # Add the new LightBlock item to the list of processed items
    processed_blocks.append(new_lightblock)

    # Add the block name to the set of processed block names
    processed_block_names.add(block_name)

# Update shimmer_data['LightBlock'] with unique entries
shimmer_data['LightBlock'] = [entry for entry in shimmer_data['LightBlock'] if entry['block'] not in processed_block_names]

# Combine the processed items with the original LightBlock list
shimmer_data['LightBlock'] += processed_blocks

# Debug: Print the updated shimmer_data
print("Updated Shimmer Data:", shimmer_data)

# Write the updated data to shimmer2.json
with open(shimmer2_path, 'w') as output_file:
    json.dump(shimmer_data, output_file, indent=2)

print("Task completed successfully. Check shimmer2.json for the updated data.")
