def add_all(*args: int) -> int:
    print("Args received:", args)
    return sum(args)


print(add_all(1, 2, 3, 4))  # Output: 10
