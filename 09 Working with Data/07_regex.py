import re

phone = "+92-300-1234567"
pattern = r"^\+92-\d{3}-\d{7}$"

if re.match(pattern, phone):
    print("Valid Pakistani phone number")


sentence = "Python is powerful and clean."
words = re.findall(r"\b\w+\b", sentence)
print(words)  # ['Python', 'is', 'powerful', 'and', 'clean']


text = "There are 3 cats and 4 dogs."
new_text = re.sub(r"\d+", "some", text)
print(new_text)  # "There are some cats and some dogs."
