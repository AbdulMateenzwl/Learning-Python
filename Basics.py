from typing import Tuple
from typing import List


name = "Mateen"

age = 22

val = 3 + 5

len("hello")

print(name)

flag: bool = False


arr: List[int] = [1, 2, 3, 4, 5]


tuple: Tuple[int, ...] = (1, 2, 3, 4, 5)

dic: dict[str, int | str] = {"name": name, "age": age, "val": val}

setArr: set[int] = set(arr)

if age > 18:
    print("Adult")
else:
    print("Child")

for i in range(5):
    print(i)

while age < 25:
    print("Still young")
    age += 1


def greet(name: str) -> str:
    return f"Hello, {name}!"


# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("mango")
fruits[1] = "grape"
print(fruits)


# Dictionaries
person: dict[str, str | int | bool] = {
    "name": "Mateen",
    "age": 22,
    "student": True
}

print(person["name"])
person["age"] = 23
person["city"] = "Lahore"
print(person)

# Tuples
coordinates = (10.0, 20.5)
print(coordinates[1])
# coordinates[0] = 5


# Sets
numbers = {1, 2, 3, 3, 4}
print(numbers)

numbers.add(5)
print(numbers)


# List Comprehensions
squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

nums = [1, 2, 3]
squares = {x: x**2 for x in nums}
print(squares)   # {1: 1, 2: 4, 3: 9}


# File Operations
with open("sample.txt", "w") as f:
    f.write("Hello, Mateen!\n")
    f.write("This is Python.\n")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
