from typing import Dict, Any
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check if request succeeded
if response.status_code == 200:
    data = response.json()  # Convert JSON response to dict
    print(data["title"])
else:
    print("Failed to fetch data.")


payload: Dict[str, Any] = {
    "title": "My Post",
    "body": "This is a post",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=payload)

print(response.status_code)
print(response.json())
