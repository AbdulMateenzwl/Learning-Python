import json
from typing import Any, Dict

# Python dictionary
data: Dict[str, Any] = {"name": "Alice", "age": 25, "is_student": True}

# Convert to JSON string
json_string = json.dumps(data)
print("JSON String:", json_string)

# Convert back to Python object
parsed_data = json.loads(json_string)
print("Parsed Data:", parsed_data)

# Writing to a JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# Reading from a JSON file
with open("data.json", "r") as f:
    read_data = json.load(f)
    print("Data from file:", read_data)
