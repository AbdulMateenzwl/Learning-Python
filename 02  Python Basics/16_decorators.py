from typing import Callable, Optional, Any


def smart_divide(func: Callable[[float, float], None]) -> Callable[[float, float], None]:
    def wrapper(a: float, b: float) -> Optional[Any]:
        if b == 0:
            print("Division by zero is not allowed.")
            return None
        return func(a, b)
    return wrapper


@smart_divide
def divide(a: float, b: float) -> None:
    print(f"Result: {a / b}")


divide(10, 2)  # Works fine
divide(5, 0)   # Error handled
