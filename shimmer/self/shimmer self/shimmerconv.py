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

# Create a set to track processed lightblocks
processed_lightblocks = set()

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

    # Extract additional state information from properties
    state_info = {}

    # Extract lit and on information
    lit_match = re.search(r"lit=(\w+)", properties)
    if lit_match:
        state_info["lit"] = lit_match.group(1)
        # Create a new LightBlock item with updated information for lit=true
        radius_true = int(round((2 / 3) * int(light_level)))
        new_lightblock_true = {
            "block": block_name,
            "color": "#orange",  # Default color if not found
            "radius": radius_true,
            "state": {"lit": "true"}
        }
        # Add the new LightBlock item to the list of processed items
        processed_lightblocks.add(json.dumps(new_lightblock_true, sort_keys=True))

        # Create a new LightBlock item with updated information for lit=false
        radius_false = 0
        new_lightblock_false = {
            "block": block_name,
            "color": "#orange",  # Default color if not found
            "radius": radius_false,
            "state": {"lit": "false"}
        }
        # Add the new LightBlock item to the list of processed items
        processed_lightblocks.add(json.dumps(new_lightblock_false, sort_keys=True))

    on_match = re.search(r"on=(\w+)", properties)
    if on_match:
        state_info["on"] = on_match.group(1)
        # Create a new LightBlock item with updated information for on=true
        radius_true = int(round((2 / 3) * int(light_level)))
        new_lightblock_true = {
            "block": block_name,
            "color": "#orange",  # Default color if not found
            "radius": radius_true,
            "state": {"on": "true"}
        }
        # Add the new LightBlock item to the list of processed items
        processed_lightblocks.add(json.dumps(new_lightblock_true, sort_keys=True))

        # Create a new LightBlock item with updated information for on=false
        radius_false = 0
        new_lightblock_false = {
            "block": block_name,
            "color": "#orange",  # Default color if not found
            "radius": radius_false,
            "state": {"on": "false"}
        }
        # Add the new LightBlock item to the list of processed items
        processed_lightblocks.add(json.dumps(new_lightblock_false, sort_keys=True))

    # Extract power information from properties
    power_match = re.search(r"power=(\d+)", properties)
    if power_match:
        state_info["power"] = power_match.group(1)

    # Extract parts information from properties
    parts_match = re.search(r"part=(\w+)", properties)
    if parts_match:
        state_info["part"] = parts_match.group(1)

    # Create a new LightBlock item with updated information for the original state
    radius = int(round((2 / 3) * int(light_level)))
    new_lightblock = {
        "block": block_name,
        "color": "#orange",  # Default color if not found
        "radius": radius,
        "state": state_info
    }

    # Add the new LightBlock item to the list of processed items
    processed_lightblocks.add(json.dumps(new_lightblock, sort_keys=True))

    # Add the block name to the set of processed block names
    processed_block_names.add(block_name)

# Convert processed_lightblocks set back to a list
processed_lightblocks = [json.loads(item) for item in processed_lightblocks]

# Update shimmer_data['LightBlock'] with unique entries
shimmer_data['LightBlock'] = processed_lightblocks

# Combine the processed items with the original LightBlock list
shimmer_data['Bloom'] += processed_lightblocks

# Read fluids.txt and particles.txt (you can add code here to process these files as needed)

# Save the updated shimmer_data to shimmer2.json
with open(shimmer2_path, 'w') as shimmer2_file:
    json.dump(shimmer_data, shimmer2_file, indent=2)
