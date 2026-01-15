import os
from dotenv import load_dotenv

load_dotenv()


if os.getenv("GITHUB_ACTIONS") == "true":
    url = os.getenv("URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
else:
    url = os.getenv("URL")
    username = os.getenv("User_id")
    password = os.getenv("Password")
