
from typing import List, Dict, Any
import logging
from dotenv import load_dotenv
import os

from api_requests.fetch_users import fetch_users
from data_processing import filter_by_city, group_users_by_company
from data_processing import categorize_users_by_city_length
from file_operations import save_users_to_csv, read_users_from_csv


# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def menu() -> str:
    print("\n 1. Fetch and Parse JSON Data")
    print(" 2. Data Processing with Collections and Control Flow")
    print(" 3. Save and Read Users from CSV")
    choice = input("Enter your choice: ")
    return choice


def data_processing_menu() -> str:
    print("1. Filter user by city")
    print("2. Filter user by City Length")
    print("3. Group users by Company")
    choice = input("Enter your choice: ")
    return choice


def load_user_by_default() -> List[Dict[str, Any]]:
    url = os.getenv("API_URL")
    if not url:
        return []
    users = fetch_users(url)
    return users


if __name__ == "__main__":
    users: List[Dict[str, Any]] = []
    filtered_users: List[Dict[str, Any]] = []
    # During Development
    users = load_user_by_default()
    while True:
        user_choice = menu()
        if user_choice == "1":
            try:
                logging.info("Fetching users from API...")
                # Fetch users from the API
                url = os.getenv("API_URL")
                if not url:
                    logging.error("API_URL environment variable is not set.")
                    break

                users = fetch_users(url)

                logging.info("Fetched users successfully.")
                logging.info("Total users fetched: %d", len(users))
            except Exception as e:
                logging.error("Error fetching users: %s", e)

        elif user_choice == "2":
            data_choice = data_processing_menu()
            if data_choice == "1":
                city = input("Enter city name to filter users: ")
                filtered_users = filter_by_city(users, city)
                logging.info("Filtered users by city '%s': %d",
                             city, len(filtered_users))

            elif data_choice == "2":
                try:
                    categorized_users = categorize_users_by_city_length(users)
                    logging.info("Users with small city length : %d",
                                 len(categorized_users['small']))
                    logging.info("Users with large city length : %d",
                                 len(categorized_users['large']))
                except Exception as e:
                    logging.error(
                        "Error categorizing users by city length: %s", e)
            elif data_choice == "3":
                try:
                    company_groups = group_users_by_company(users)
                    for company, group in company_groups.items():
                        logging.info("Company: %s, Users: %d",
                                     company, len(group))
                except Exception as e:
                    logging.error("Error grouping users by company: %s", e)
            else:
                logging.warning("Invalid choice in data processing menu.")

        elif user_choice == "3":
            filename = input(
                "Enter filename to save users (or press Enter for default): ")
            if not filename:
                filename = ""
            file_path = save_users_to_csv(users, filename)
            logging.info(f"Users saved to {file_path}")

            logging.info("Reading from CSV file...")
            read_users = read_users_from_csv(file_path)
            logging.info(f"Read {len(read_users)} users from {file_path}")
        else:
            logging.warning("Invalid choice.")
