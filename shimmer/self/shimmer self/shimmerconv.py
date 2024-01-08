import os
import json
import re

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
shimmer_path = os.path.join(script_directory, 'shimmer.json')
shimmer2_path = os.path.join(script_directory, 'shimmer2.json')
particles_path = os.path.join(script_directory, 'particles.txt')
fluids_path = os.path.join(script_directory, 'fluids.txt')

# Read shimmer.json
with open(shimmer_path, 'r') as shimmer_file:
    shimmer_data = json.load(shimmer_file)

# Ensure 'Bloom' key is present and initialize it as an empty list if not
if 'Bloom' not in shimmer_data:
    shimmer_data['Bloom'] = []

# Create a set to track processed block states
processed_block_states = set()

# Create a list to store the processed items
processed_blocks = []

# Read lightblocks.txt
with open('lightblocks.txt', 'r') as lightblocks_txt:
    # Use regular expressions to extract block information and color from item name
    block_pattern = re.compile(r"Block\{(.*?)\}(\[.*?\])? -> (\d+)")
    blocks = block_pattern.findall(lightblocks_txt.read())

# Update shimmer_data based on lightblocks information
for block_name, properties, light_level in blocks:
    # Check if the block name is already present in processed_block_states
    if block_name in processed_block_states:
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
        "radius": int(round((2 / 3) * int(light_level)))  # Updated radius calculation
    }

    # Check if properties are specified and add them to the "state" section if present
    if properties:
        # Extract properties from the string inside the square brackets
        property_list = re.findall(r"(\w+=[^,\]]+)", properties)
        if property_list:
            # Create the "state" dictionary and add properties to it
            state_dict = {prop.split('=')[0]: prop.split('=')[1] for prop in property_list}

            # If "part" is present in the state, process lit, on, and power states
            if "part" in state_dict:
                part = state_dict["part"]

                # If "lit" or "on" is present, create two entries for each part
                if "lit" in state_dict or "on" in state_dict:
                    for lit_state in [True, False]:
                        new_lightblock_state = new_lightblock.copy()
                        new_lightblock_state["state"] = {"lit": str(lit_state).lower(), "part": part}
                        new_lightblock_state["radius"] = 0 if not lit_state else int(round((2 / 3) * int(light_level)))
                        processed_blocks.append(new_lightblock_state)

                # If "power" is present, create entries for each power level
                elif "power" in state_dict:
                    for power_level in state_dict["power"].split(','):
                        new_lightblock_state = new_lightblock.copy()
                        new_lightblock_state["state"] = {"power": power_level, "part": part}
                        new_lightblock_state["radius"] = int(power_level) if lit_state else 0
                        processed_blocks.append(new_lightblock_state)

                # If none of the above, create a single entry for each part
                else:
                    new_lightblock_state = new_lightblock.copy()
                    new_lightblock_state["state"] = {"part": part}
                    processed_blocks.append(new_lightblock_state)

            # If "part" is not present, process lit, on, and power states as mentioned above
            else:
                if "lit" in state_dict or "on" in state_dict:
                    for lit_state in [True, False]:
                        new_lightblock_state = new_lightblock.copy()
                        new_lightblock_state["state"] = {"lit": str(lit_state).lower()}
                        new_lightblock_state["radius"] = 0 if not lit_state else int(round((2 / 3) * int(light_level)))
                        processed_blocks.append(new_lightblock_state)

                elif "power" in state_dict:
                    for power_level in state_dict["power"].split(','):
                        new_lightblock_state = new_lightblock.copy()
                        new_lightblock_state["state"] = {"power": power_level}
                        new_lightblock_state["radius"] = int(power_level) if lit_state else 0
                        processed_blocks.append(new_lightblock_state)

                else:
                    new_lightblock_state = new_lightblock.copy()
                    processed_blocks.append(new_lightblock_state)

    # If no properties, create a single entry with color and radius
    else:
        processed_blocks.append(new_lightblock)

    # Add the block name to the set of processed block states
    processed_block_states.add(block_name)

# Update shimmer_data['LightBlock'] with unique entries
shimmer_data['LightBlock'] = [entry for entry in shimmer_data['LightBlock'] if entry['block'] not in processed_block_states]

# Combine the processed items with the original LightBlock list
shimmer_data['LightBlock'] += processed_blocks

# Create a set to track processed particle names
processed_particle_names = set()

# Process particles from particles.txt
with open(particles_path, 'r') as particles_txt:
    # Use regular expressions to extract particle names after the hyphen (-)
    particle_pattern = re.compile(r"- (.+)")
    particles = particle_pattern.findall(particles_txt.read())

for particle_name in particles:
    # Check if the particle is already present in shimmer_data
    if any('particle' in entry and entry['particle'] == particle_name for entry in shimmer_data['Bloom']):
        continue  # Skip processing if the particle is already in shimmer_data

    # Debug: Print information before updating
    print(f"Updating particle_name: {particle_name}")

    # Create a new Bloom item with the particle name
    new_bloom_item = {
        "particle": particle_name
    }

    # Add the new Bloom item to the list of processed items
    shimmer_data['Bloom'].append(new_bloom_item)

    # Add the particle name to the set of processed particle names
    processed_particle_names.add(particle_name)

# Debug: Print the updated shimmer_data
print("Updated Shimmer Data (Bloom - Particles):", shimmer_data)

# Create a set to track processed fluid names
processed_fluid_names = set()

# Process fluids from fluids.txt
with open(fluids_path, 'r') as fluids_txt:
    # Use regular expressions to extract fluid names after the hyphen (-)
    fluid_pattern = re.compile(r"- (.+)")
    fluids = fluid_pattern.findall(fluids_txt.read())

for fluid_name in fluids:
    # Check if the fluid is already present in shimmer_data
    if any('fluid' in entry and entry['fluid'] == fluid_name for entry in shimmer_data['Bloom']):
        continue  # Skip processing if the fluid is already in shimmer_data

    # Debug: Print information before updating
    print(f"Updating fluid_name: {fluid_name}")

    # Create a new Bloom item with the fluid name
    new_bloom_item = {
        "fluid": fluid_name
    }

    # Add the new Bloom item to the list of processed items
    shimmer_data['Bloom'].append(new_bloom_item)

    # Add the fluid name to the set of processed fluid names
    processed_fluid_names.add(fluid_name)

# Debug: Print the updated shimmer_data
print("Updated Shimmer Data (Bloom - Fluids):", shimmer_data)

# Write the updated data to shimmer2.json
with open(shimmer2_path, 'w') as output_file:
    json.dump(shimmer_data, output_file, indent=2)

print("Task completed successfully. Check shimmer2.json for the updated data.")
