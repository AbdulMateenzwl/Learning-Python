# writing_example.py

# 'w' = write mode (overwrites if file exists)
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a new file.\n")


# reading_example.py

# 'r' = read mode
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


