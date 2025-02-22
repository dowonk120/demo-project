import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
API_PASSWORD = os.getenv("DB_PASSWORD")

print(API_KEY)
print(API_PASSWORD)


# "DB_PASSWORD:", os.getenv("DB_PASSWORD"))
