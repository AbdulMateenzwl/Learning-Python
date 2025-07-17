# Type casting means converting one data type to another.

# Convert string to int
num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int))

# Convert int to string
age = 22
age_str = str(age)
print(age_str, type(age_str))

# Convert float to int (loses decimal)
pi = 3.14
whole = int(pi)
print(whole)  # 3

# Convert number to float
num = 5
print(float(num))  # 5.0

# Convert to bool
print(bool(0))      # False
print(bool(1))      # True
print(bool("Hi"))   # True
print(bool(""))     # False
