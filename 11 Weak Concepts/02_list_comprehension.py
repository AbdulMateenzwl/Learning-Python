numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [num**2 for num in numbers]


even = [num for num in numbers if num % 2 == 0]

print(even)

names = ["ali", "mateen", "saqib"]

uppercase = [name.upper() for name in names]

print(uppercase)

matrix = [[1, 2], [3, 4], [5, 6]]

simple_list = [val for row in matrix for val in row]

print(simple_list)

text = "hello world"
vowels = 'aeiou'

replaced = ["*" if c in vowels else c for c in text]

output = ''.join(replaced)

print(output)

tuple_square = [(num, num**2) if num % 2 == 0 else (num, num)
                for num in numbers]

print(tuple_square)

data = [
    {"name": "Ali", "age": 23},
    {"name": "Sara", "age": 30},
    {"name": "John", "age": 18},
]
adults = [person["name"] for person in data if person["age"] >= 21]

print(adults)

words = ["apple", "banana", "grape", "banana", "apple"]
word_dict = {word: len(word) for word in words}
print(word_dict)
