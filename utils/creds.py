import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')
username = os.getenv('User_id')
password = os.getenv('Password')