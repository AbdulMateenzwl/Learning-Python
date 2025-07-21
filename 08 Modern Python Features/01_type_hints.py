def add(a: int, b: int) -> int:
    return a + b

def is_adult(age: int) -> bool:
    return age >= 18

def get_names() -> list[str]:
    return ["Alice", "Bob", "Charlie"]


def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

print(greet("Alice", 25))  # Output: Hello, Alice. You are 25 years old.
