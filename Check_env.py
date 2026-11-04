import os
from dotenv import load_dotenv

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION_NAME")


print(f"api_id: {api_id}")
print(f"api_hash: {api_hash}")
print(f"session: {session}")

