import requests
from typing import List, Dict, Any

def fetch_users(url: str) -> List[Dict[str, Any]]:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []
