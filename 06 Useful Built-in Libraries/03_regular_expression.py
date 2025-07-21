import re

text = "My email is example123@gmail.com"

# Find an email
match = re.search(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)
if match:
    print("Email found:", match.group())

# Replace digits
print("Removed digits:", re.sub(r'\d+', '', text))

# Find all words
print("Words:", re.findall(r'\w+', text))
