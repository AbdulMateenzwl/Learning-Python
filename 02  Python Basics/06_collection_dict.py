# Dictionary = key-value pairs, unordered, changeable

person: dict[str, str | int] = {
    "name": "Mateen",
    "age": 22,
    "city": "Lahore"
}

print(person["name"])       # Access value by key

person["age"] = 23          # Modify
person["country"] = "PK"    # Add new key-value

# Loop through dictionary
for key, value in person.items():
    print(key, "->", value)

# Remove a key
del person["city"]
print(person)
