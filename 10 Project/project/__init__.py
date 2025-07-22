
from typing import List, Dict, Any
import logging

from .config import config

from .api_requests.fetch_users import fetch_users

from .data_processing import (
    filter_by_city,
    group_users_by_company,
    categorize_users_by_city_length
)

from . import file_operations as file_ops

# Initialize configuration and logging
config.setup_logging()
logger = logging.getLogger(__name__)


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
    users = fetch_users(config.api_url or "")
    return users


def init() -> None:
    users: List[Dict[str, Any]] = []
    filtered_users: List[Dict[str, Any]] = []
    # During Development
    users = load_user_by_default()
    while True:
        user_choice = menu()
        match user_choice:
            case "1":
                try:
                    logger.info("Fetching users from API...")
                    users = fetch_users(config.api_url or "")
                    logger.info("Fetched users successfully.")
                    logger.info("Total users fetched: %d", len(users))
                except Exception as e:
                    logging.error("Error fetching users: %s", e)

            case "2":
                data_choice = data_processing_menu()
                match data_choice:
                    case "1":
                        city = input("Enter city name to filter users: ")
                        filtered_users = filter_by_city(users, city)
                        logger.info("Filtered users by city '%s': %d",
                                    city, len(filtered_users))

                    case "2":
                        try:
                            categorized_users = categorize_users_by_city_length(
                                users)
                            logger.info("Users with small city length: %d",
                                        len(categorized_users['small']))
                            logger.info("Users with large city length: %d",
                                        len(categorized_users['large']))
                        except Exception as e:
                            logger.error(
                                "Error categorizing users by city length: %s", e)
                    case "3":
                        try:
                            company_groups = group_users_by_company(users)
                            for company, group in company_groups.items():
                                logger.info("Company: %s, Users: %d",
                                            company, len(group))
                        except Exception as e:
                            logger.error(
                                "Error grouping users by company: %s", e)
                    case _:
                        logger.warning(
                            "Invalid choice in data processing menu.")

            case "3":
                filename = input(
                    "Enter filename to save users (or press Enter for default): ")
                if not filename:
                    filename = ""
                file_path = file_ops.save_users_to_csv(users, filename)
                logger.info(f"Users saved to {file_path}")

                logger.info("Reading from CSV file...")
                read_users = file_ops.read_users_from_csv(file_path)
                logger.info(f"Read {len(read_users)} users from {file_path}")

            case "0":
                logger.info("Exiting application...")
                break
            case _:
                logger.warning("Invalid choice. Please select 0-6.")


if __name__ == "__main__":
    init()
