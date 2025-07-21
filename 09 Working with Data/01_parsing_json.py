import json

json_data = '{"name": "Mateen", "age": 22, "skills": ["Python", "C#", "React"]}'

# Convert JSON string to Python dict
data = json.loads(json_data)

print(data["name"])     # Output: Mateen
print(data["skills"])   # Output: ['Python', 'C#', 'React']

from typing import Dict, Any

python_data: Dict[str, Any] = {
    "name": "Mateen",
    "age": 22,
    "skills": ["Python", "C#", "React"]
}

# Convert dict to JSON string
json_string = json.dumps(python_data, indent=4)

print(json_string)

with open("data.json", "w") as file:
    json.dump(python_data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["name"])  # Output: Mateen
