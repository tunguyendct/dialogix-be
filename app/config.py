import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
DATABASE_NAME = os.getenv('DATABASE_NAME')
USER_COLLECTION = os.getenv('USER_COLLECTION')
CHAT_COLLECTION = os.getenv('CHAT_COLLECTION')
MESSAGE_COLLECTION = os.getenv('MESSAGE_COLLECTION')