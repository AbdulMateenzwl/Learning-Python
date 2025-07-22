from typing import List, Dict, Any
from .decorators import timing_decorator


@timing_decorator
def filter_by_city(users: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
    filtered_users: List[Dict[str, Any]] = []
    for user in users:
        if user.get('address', {}).get('city', '').lower() == city.lower():
            filtered_users.append(user)
    return filtered_users

# Use match-case (Python 3.10+) to categorize users based on city name length
@timing_decorator
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

# Function to group users by their company name using a dictionary
@timing_decorator
def group_users_by_company(users: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    company_groups: Dict[str, List[Dict[str, Any]]] = {}
    for user in users:
        company_name = user.get('company', {}).get('name', 'Unknown')
        if company_name not in company_groups:
            company_groups[company_name] = []
        company_groups[company_name].append(user)
    return company_groups