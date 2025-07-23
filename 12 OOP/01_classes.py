class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person ( {self.name}, {self.age} )"


p = person("mateen", 21)

print(p)
