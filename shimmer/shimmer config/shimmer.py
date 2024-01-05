import json

def determine_color(item_name, category, color_reference):
    if "flame" in category:
        return "orange"
    elif "white" in category:
        return "white"
    else:
        for color in color_reference:
            if color in item_name:
                return color
        print(f"No color found in item name: {item_name}")
        return None

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
shimmer_config = {"ColorReference": color_reference, "LightBlocks": [], "LightItems": []}

# Process each file
for category, filename in files.items():
    with open(filename, 'r') as f:
        items = f.read().splitlines()
        for item in items:
            # Strip the <item: or <block: prefixes
            item_name = item.replace("<item:", "").replace("<block:", "").replace(">", "")

            color = determine_color(item_name, category, color_reference)
            if color is None:
                continue

            is_block = "block" in category
            entry = {is_block and "block" or "item_id": item_name, "color": "#" + color, "radius": is_block and 14 or 7}

            # Append to the appropriate list in shimmer_config
            shimmer_config[is_block and "LightBlocks" or "LightItems"].append(entry)

# Write the formatted shimmer config to a new JSON file
with open('shimmer.json', 'w') as f:
    json.dump(shimmer_config, f, indent=4)
