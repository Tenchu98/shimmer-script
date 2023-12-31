import json
from collections import OrderedDict

# Define the file names
files = {
    "colored_blocks": "colored_blocks.txt",
    "colored_items": "colored_items.txt",
    "natural_flame_blocks": "natural_flame_blocks.txt",
    "natural_flame_items": "natural_flame_items.txt",
    "white_light_blocks": "white_light_blocks.txt",
    "white_light_items": "white_light_items.txt",
}

# Load the color reference file
with open("color_reference.json", 'r') as f:
    color_reference = json.load(f)["ColorReference"]

# Initialize the shimmer config dictionary
shimmer_config = OrderedDict()
shimmer_config["ColorReference"] = {color: {"r": values["r"], "g": values["g"], "b": values["b"], "a": values["a"]} for color, values in color_reference.items()}
shimmer_config["LightBlocks"] = []
shimmer_config["LightItems"] = []

# Process each file
for category, filename in files.items():
    with open(filename, 'r') as f:
        items = f.read().splitlines()
        for item in items:
            # Strip the <item: or <block: prefixes
            item_name = item.replace("<item:", "").replace("<block:", "").replace(">", "")

            # Determine the color based on the file category
            if "flame" in category:
                color = "orange"
            elif "white" in category:
                color = "white"
            else:
                # Search for a color in the item name that matches a color in the reference list
                color = next((c for c in color_reference if c in item_name), None)
                if color is None:
                    print(f"No color found in item name: {item_name}")
                    continue

            # Determine if it's a block or item based on the category
            is_block = "blocks" in category

            # Add the item to the shimmer config
            color_values = color_reference[color]
            entry = {"block" if is_block else "item_id": item_name, "color": f"#{color}", "radius": 14 if is_block else 7}

            # Append to the appropriate list in shimmer_config
            shimmer_config["LightBlocks" if is_block else "LightItems"].append(entry)

# Write the condensed shimmer config to a new JSON file
with open('shimmer.json', 'w') as f:
    json.dump(shimmer_config, f, indent=4)
