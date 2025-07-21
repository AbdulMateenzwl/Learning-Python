from typing import List, Dict, Any

from typing import List, Dict, Any


def filter_by_city(users: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
    filtered_users: List[Dict[str, Any]] = []
    for user in users:
        if user.get('address', {}).get('city', '').lower() == city.lower():
            filtered_users.append(user)
    return filtered_users

# Use match-case (Python 3.10+) to categorize users based on city name length (e.g., "small" for names < 10 characters, "large" otherwise).
def categorize_users_by_city_length(users: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    categorized_users: Dict[str, List[Dict[str, Any]]] = {'small': [], 'large': []}
    for user in users:
        city_name = user.get('address', {}).get('city', '')
        match len(city_name):
            case length if length < 10:
                categorized_users['small'].append(user)
            case _:
                categorized_users['large'].append(user)
    return categorized_users