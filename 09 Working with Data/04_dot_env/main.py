from dotenv import load_dotenv # type: ignore
import os

# Load .env file into environment variables
load_dotenv()

# Access them
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG") == "True"
port = int(os.getenv("PORT", 8000))  # default = 8000

print(f"API Key: {api_key}")
print(f"Debug Mode: {debug}")
print(f"Running on Port: {port}")
