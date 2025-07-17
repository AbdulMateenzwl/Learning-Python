class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")


p1 = Person("Mateen", 22)
p1.greet()


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print(f"My ID is {self.student_id}")


s1 = Student("Ali", 20, "UET123")
s1.greet()
s1.show_id()


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner: str = owner
        self.__balance: float = balance

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Mateen", 1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance())
# print(account.__balance)
