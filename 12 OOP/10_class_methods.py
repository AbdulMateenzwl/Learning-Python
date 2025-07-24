class Person:

    val = 'PersonA'

    def __init__(self, name) -> None:
        self.name = name

    def simple_method(self) -> str:
        return self.name

    @classmethod
    def get_method(cls) -> str:
        return cls.val

    @staticmethod
    def static_method() -> str:
        return "static_method"


p = Person("ali")

print(Person.get_method())

print(Person.static_method())

print(p.simple_method())
