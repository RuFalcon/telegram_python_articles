import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = str(os.getenv('SLACK_API_TOKEN'))
CHAT_ID = str(os.getenv('CHAT_ID'))
DATABASE = str(os.getenv('DATABASE'))
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
HOST = str(os.getenv('HOST'))
PORT = str(os.getenv('PORT'))

