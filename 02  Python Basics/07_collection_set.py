# Set = unordered, unique values only

my_set = {1, 2, 3, 3, 4}
print(my_set)  # {1, 2, 3, 4}

my_set.add(5)
my_set.remove(2)

# Loop through set
for item in my_set:
    print(item)

# Sets are good for removing duplicates
nums = [1, 2, 2, 3]
unique_nums = set(nums)
print(unique_nums)
