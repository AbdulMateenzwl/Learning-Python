# Python Fundamentals Assignment

## Prerequisites

- Python development environment with an IDE of your choice
- Manage dependencies and virtual environments using `venv` or `pipenv`

## Assignment Tasks

### 2. Fetch and Parse JSON Data

- Use the `requests` library to fetch user data from the public API: `https://jsonplaceholder.typicode.com/users`
- Parse the JSON response into a Python list of dictionaries
- Use type hints to define the data structure (e.g., for lists and dictionaries)
- Log the number of users fetched and any errors encountered

### 3. Data Processing with Collections and Control Flow

- Write a function to filter users by their city (from the `address.city` field) using a list comprehension
- Use `match-case` (Python 3.10+) to categorize users based on city name length:
  - "small" for names < 10 characters
  - "large" otherwise
- Create a function to group users by their company name (from `company.name`) using a dictionary
- Handle potential errors (e.g., missing keys in JSON) with `try-except-else-finally`

### 4. File Operations

- Save the filtered user data to a CSV file
- Use `pathlib` to create directories and manage file paths (avoid `os.path`)
- Read the CSV file back and log the number of records processed
- Ensure proper file handling with `with` statements

### 5. Modules and Packages

- Organize your code into modules (e.g., separate files for API fetching, data processing, and file operations)
- Create a package structure with an `__init__.py` file
- Use `import`, `from`, and `as` to manage module imports effectively

### 6. Modern Python Features

- Use type hints for function arguments and return types (e.g., `def process_data(data: list[dict]) -> dict`)
- Use f-strings for string formatting when generating logs or output messages
- Apply structural pattern matching (`match-case`) in at least one function

### 7. Environment Variables and Regular Expressions

- Store the API URL in an environment variable using `python-dotenv`
- Use the `re` module to validate or extract patterns (e.g., extract email domains from user emails in the JSON data)

### 8. Additional Features

- Write a decorator to measure and log the execution time of your data processing functions
- Use a lambda function for a simple data transformation (e.g., converting names to uppercase)
- Explore the `datetime` module to add timestamps to your logs or output files

## Requirements

- ✅ Use Python 3.12+
- ✅ Avoid using `print()` for logging; use the `logging` module instead
- ✅ Include exception handling for robust error management
- ✅ Use `pathlib` for all file and directory operations
- ✅ Follow best practices for code organization, readability, and modularity
