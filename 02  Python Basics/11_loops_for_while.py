# FOR LOOP – used to repeat over a sequence (list, range, string)

for i in range(5):
    print("For loop iteration:", i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# WHILE LOOP – repeats while a condition is True

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

# Loop control: break, continue

for i in range(5):
    if i == 3:
        break  # exits the loop
    print("i before break:", i)

for i in range(5):
    if i == 2:
        continue  # skips this iteration
    print("i with continue:", i)
