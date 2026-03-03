# lees json data in van het json bestand weerdata.json

import json
with open("weerdata.json", "r") as f:
    data = json.load(f)
print(data)

#geef me de copyright uit de json data
copyright_text = data.get("copyright")

print(f"Top-level keys: {list(data.keys())}")
print(f"copyright: {}")