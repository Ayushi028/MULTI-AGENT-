from dotenv import load_dotenv
import os
from pathlib import Path

print("Current directory:", os.getcwd())
print("\nLooking for .env file...")

# Try to find it
env_file = Path(".env")
print(f".env exists: {env_file.exists()}")

# Load it
load_dotenv()

key = os.getenv("MISTRAL_API_KEY")
print(f"Key: {repr(key)}")