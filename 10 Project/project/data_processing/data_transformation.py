
from typing import List, Dict, Any

uppercase_transform = lambda users: [
    {**user, 'name': user.get('name', '').upper()} for user in users
]
