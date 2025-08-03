import os
from dotenv import load_dotenv
import urllib.parse
from mongoengine import connect

load_dotenv()  # завантажує .env у os.environ

username = os.getenv("MONGO_USER")
raw_password = os.getenv("MONGO_PASS")
if raw_password is None:
    raise ValueError("MONGO_PASS is not set in environment variables")
password = urllib.parse.quote(raw_password)
domain = os.getenv("DOMAIN")
db_name = os.getenv("DB_NAME")

uri = f"mongodb+srv://{username}:{password}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Cluster0"

connect(host=uri, ssl=True)