"""
File operations module for handling CSV files and directory management.
Uses pathlib for modern file path handling.
"""

from pathlib import Path
from typing import List, Dict, Any
import csv
import logging
from datetime import datetime


def save_users_to_csv(users: List[Dict[str, Any]], filename: str = "") -> Path:
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"users_{timestamp}.csv"
    
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    file_path = output_dir / filename
    
    if not users:
        logging.warning("No users to save to CSV")
        return file_path
    
    # Extract all fieldnames for complete user data
    fieldnames = [
        "id", "name", "username", "email", 
        "address_street", "address_suite", "address_city", "address_zipcode",
        "address_geo_lat", "address_geo_lng", 
        "phone", "website",
        "company_name", "company_catchPhrase", "company_bs"
    ]

    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for user in users:
                row = {
                    "id": user.get("id", ""),
                    "name": user.get("name", ""),
                    "username": user.get("username", ""),
                    "email": user.get("email", ""),
                    "address_street": user.get("address", {}).get("street", ""),
                    "address_suite": user.get("address", {}).get("suite", ""),
                    "address_city": user.get("address", {}).get("city", ""),
                    "address_zipcode": user.get("address", {}).get("zipcode", ""),
                    "address_geo_lat": user.get("address", {}).get("geo", {}).get("lat", ""),
                    "address_geo_lng": user.get("address", {}).get("geo", {}).get("lng", ""),
                    "phone": user.get("phone", ""),
                    "website": user.get("website", ""),
                    "company_name": user.get("company", {}).get("name", ""),
                    "company_catchPhrase": user.get("company", {}).get("catchPhrase", ""),
                    "company_bs": user.get("company", {}).get("bs", "")
                }
                writer.writerow(row)
    except Exception as e:
        logging.error(f"Error saving users to CSV: {e}")
        return file_path
    
    logging.info(f"Saved {len(users)} users to {file_path}")
    return file_path


def read_users_from_csv(file_path: Path) -> List[Dict[str, Any]]:
    users = []
    
    if not file_path.exists():
        logging.error(f"File {file_path} does not exist")
        return users
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            users = list(reader)
        
        
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
    
    return users


