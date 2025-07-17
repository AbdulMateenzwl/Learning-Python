def describe_person(name: str, age: int, country: str = "Pakistan"):
    print(f"Name: {name}, Age: {age}, Country: {country}")


# Positional arguments
describe_person("Mateen", 21)

# Keyword arguments
describe_person(age=22, name="Ali", country="India")
