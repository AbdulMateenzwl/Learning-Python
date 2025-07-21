import os

# Get current working directory
print("Current Dir:", os.getcwd())

# Create and remove directory
os.makedirs("test_dir", exist_ok=True)
print("Directory created.")
os.rmdir("test_dir")

# List files
print("Files:", os.listdir("."))

# Environment variables
print("HOME:", os.getenv("HOME"))
