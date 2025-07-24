from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def test(self):
        return "test"

    def sound(self):
        return "sound"


d = Dog()

print(d.sound())
