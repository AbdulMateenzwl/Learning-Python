try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


try:
    x = int("10")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful:", x)


f = open("03 Files & OS Operations/06_try_catch.py", "r")
try:
    data = f.read()
    print(data)
finally:
    f.close()  # Always closes the file, even if error occurs


try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
