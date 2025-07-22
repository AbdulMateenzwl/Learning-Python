import re
from typing import List, Dict, Any, Set
from .decorators import timing_decorator


@timing_decorator
def extract_email_domains(users: List[Dict[str, Any]]) -> Set[str]:
    domains = set()
    for user in users:
        email = user.get('email', '')
        if email:
            match = re.search(r'@([a-zA-Z0-9.-]+)', email)
            if match:
                domain = match.group(1)
                domains.add(domain)
    return domains
