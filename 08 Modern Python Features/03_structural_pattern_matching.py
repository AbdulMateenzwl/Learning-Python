def get_day_message(day: str):
    match day:
        case "Monday":
            return "Start of work week!"
        case "Friday":
            return "Almost weekend!"
        case "Sunday":
            return "Relax day!"
        case _:
            return "Just a regular day."

print(get_day_message("Friday"))  # Output: Almost weekend!


def point_info(point: tuple[int, int]):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis at y={y}"
        case (x, 0):
            return f"X-axis at x={x}"
        case (x, y):
            return f"Point at x={x}, y={y}"

print(point_info((5, 0)))  # Output: X-axis at x=5


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def greet(person: Person):
    match person:
        case Person(name="Alice", age=30):
            return "Hi Alice!"
        case Person(name=name, age=age):
            return f"Hello {name}, age {age}"

p1 = Person("Alice", 30)
p2 = Person("Bob", 22)

print(greet(p1))  # Hi Alice!
print(greet(p2))  # Hello Bob, age 22
