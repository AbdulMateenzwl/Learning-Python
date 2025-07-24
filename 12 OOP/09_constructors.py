class Person:
    def __init__(self, name, age, city="Unknown"):
        self.name = name
        self.age = age
        self.city = city
        print(f"Person object created: {self.name}, {self.age}, {self.city}")
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, from {self.city}"

person1 = Person("Alice", 25, "New York")
print(person1.introduce())

person2 = Person("Bob", 30)
print(person2.introduce())

person3 = Person(name="Charlie", age=35, city="London")
print(person3.introduce())

person4 = Person("Diana", age=28, city="Paris")
print(person4.introduce())

print("\n" + "="*50 + "\n")


class user:
    def __init__(self, name, email, *args, username="unknown", **kwargs) -> None:
        self.name = name
        self.email = email
        self.args = args
        self.username = username
        print(kwargs)

u = user("name", "test@mail.com", "value", "data", username="mateen")

print(u.username)