import json

# Load existing shimmer JSON
with open('shimmer.json', 'r') as json_file:
    shimmer_json = json.load(json_file)

# Read CraftTweaker items from the input text file
crafttweaker_items = []
with open('crafttweaker_items.txt', 'r') as input_file:
    crafttweaker_items = [line.strip() for line in input_file.readlines() if line.strip()]

# Categorize items based on type (block, fluid, particle)
categorized_items = {"block": {}, "fluid": {}, "particle": {}}

for item in crafttweaker_items:
    # Check for block
    if "<item:" in item:
        modid, item_name = item.split(":")[1], item.split(":")[2][:-1]
        color_found = False
        for color_name, color_data in shimmer_json["ColorReference"].items():
            if color_name in item_name:
                categorized_items["block"][item] = {
                    "block": f"{modid}:{item_name}",
                    "state": {"lit": True},
                    "color": f"#{color_name}",
                    "radius": 16
                }
                color_found = True
                break
        if not color_found:
            categorized_items["block"][item] = {
                "block": f"{modid}:{item_name}",
                "state": {"lit": True},
                "color": "#orange",
                "radius": 16
            }
    # Check for particle
    elif "<particle:" in item:
        modid, particle_name = item.split(":")[1], item.split(":")[2][:-1]
        categorized_items["particle"][item] = {
            "particle": f"<particle:{modid}:{particle_name}>",
            "radius": 16
        }

# Ensure 'bloom' section exists in shimmer_json
if 'bloom' not in shimmer_json:
    shimmer_json['bloom'] = []

# Append categorized items to the "LightBlock" and "bloom" sections
for block_item in categorized_items["block"].values():
    shimmer_json["LightBlock"].append(block_item)

for particle_item in categorized_items["particle"].values():
    shimmer_json["bloom"].append(particle_item)

# Save the updated shimmer_json to a new file
with open('shimmer2.json', 'w') as json_file:
    json.dump(shimmer_json, json_file, indent=2)

print("Categorization completed. Updated shimmer JSON saved to 'shimmer2.json'.")
