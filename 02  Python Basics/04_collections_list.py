# List = ordered, changeable, allows duplicates

fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple

fruits.append("mango")  # Add item
fruits[1] = "grape"     # Change item
print(fruits)

# Loop through list
for fruit in fruits:
    print(fruit)

# Remove an item
fruits.remove("cherry")
print(fruits)
