class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self) -> None:
        print("Deleting radius")
        del self._radius

    @property
    def area(self) -> float:
        return 3.14159 * self._radius ** 2


# Usage
circle = Circle(5)
print(circle.radius)
print(circle.area)

circle.radius = 10
# circle.radius = -5

del circle.radius

circle.radius
