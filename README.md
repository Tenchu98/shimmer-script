the goal is to have the script output something in this format
```
{
  "ColorReference": {
	"boricGreen": { "r": 41, "g": 200, "b": 50, "a": 50 },
	"brightWhite": { "r": 150, "g": 150, "b": 150, "a": 50 },
	"corundumBlack": { "r": 106, "g": 104, "b": 114, "a": 200 },
	"corundumBlue": { "r": 64, "g": 197, "b": 235, "a": 200 },
	"corundumGreen": { "r": 75, "g": 203, "b": 8, "a": 200 },
	"corundumIndigo": { "r": 97, "g": 99, "b": 230, "a": 200 },
	"corundumOrange": { "r": 240, "g": 127, "b": 0, "a": 200 },
	"corundumRed": { "r": 255, "g": 37, "b": 68, "a": 200 },
	"corundumViolet": { "r": 209, "g": 8, "b": 150, "a": 200 },
	"corundumWhite": { "r": 215, "g": 226, "b": 237, "a": 200 },
	"corundumYellow": { "r": 255, "g": 234, "b": 0, "a": 200 },
	"darkPink": { "r": 120, "g": 24, "b": 70, "a": 200 },
	"endPink": { "r": 100, "g": 26, "b": 99, "a": 200 },
	"faintBlue": { "r": 27, "g": 75, "b": 110, "a": 50 },
	"faintOrange": { "r": 120, "g": 55, "b": 0, "a": 50 },
	"faintRed": { "r": 120, "g": 26, "b": 0, "a": 150 },
	"faintWhite": { "r": 64, "g": 64, "b": 64, "a": 50 },
	"glowstoneOrange": { "r": 255, "g": 100, "b": 0, "a": 50 },
	"magmaRed": { "r": 255, "g": 26, "b": 0, "a": 150 },
	"ochre": { "r": 150, "g": 85, "b": 0, "a": 50 },
	"pastelOrange": { "r": 115, "g": 69, "b": 36, "a": 50 },
	"pastelPurple": { "r": 150, "g": 75, "b": 255, "a": 255 },
	"pearlescent": { "r": 50, "g": 0, "b": 100, "a": 50 },
	"portalPurple": { "r": 47, "g": 2, "b": 187, "a": 200 },
	"redstoneRed": { "r": 255, "g": 0, "b": 0, "a": 200 },
	"shroomRed": { "r": 255, "g": 80, "b": 50, "a": 50 },
	"soulBlue": { "r": 0, "g": 140, "b": 236, "a": 150 },
	"soulGreen": { "r": 0, "g": 211, "b": 200, "a": 50 },
	"verdant": { "r": 56, "g": 100, "b": 43, "a": 50 }
  },
  "Bloom": [
	{ "particle": "minecraft:dragon_breath" },
	
    { "block": "minecraft:amethyst_cluster" },
	
    { "fluid": "minecraft:lava" }
  ],
  "LightBlock": [
    { "block": "ad_astra:glowing_iron_pillar", "color": "#faintBlue", "radius": 3 },
    { "block": "ad_astra:glowing_steel_pillar", "color": "#pastelPurple", "radius": 3 },
    { "block": "ad_astra:glowing_desh_pillar", "color": "#faintRed", "radius": 3 },
    { "block": "ad_astra:glowing_ostrum_pillar", "color": "#corundumGreen", "radius": 3 },
    { "block": "ad_astra:glowing_calorite_pillar", "color": "#corundumYellow", "radius": 3 },
	{ "block": "davebuildingmod:green_lighton", "color": "#corundumGreen", "radius": 5 },
    { "block": "davebuildingmod:alarm_lighton", "color": "#corundumRed", "radius": 5 },
    { "block": "davebuildingmod:lighton", "color": "#corundumYellow", "radius": 5 },
    { "block": "davebuildingmod:offset_blue_lighton", "color": "#corundumBlue", "radius": 5 },
    { "block": "davebuildingmod:offset_green_lighton", "color": "#corundumGreen", "radius": 5 },
    { "block": "davebuildingmod:offset_alarm_lighton", "color": "#corundumRed", "radius": 5 },
    { "block": "davebuildingmod:offset_lighton", "color": "#corundumYellow", "radius": 5 },
    { "block": "davebuildingmod:offset_blue_lighton", "color": "#corundumBlue", "radius": 5 },
    { "block": "securitycraft:alarm", "state": { "lit": true }, "color": "#redstoneRed", "radius": 5 }
  ],
  "LightItem": [
    { "item_id": "ad_astra:glowing_steel_pillar", "color": "#pastelPurple", "radius": 5 }
  ]
}```

where the color reference section is populated from the proper json and all items aquire their appropriate color from their item names.
