def print_info(**kwargs: str | int) -> None:
    print("Kwargs received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_info(name="Mateen", age=21)
# Output:
# Kwargs received: {'name': 'Mateen', 'age': 21}
# name = Mateen
# age = 21
