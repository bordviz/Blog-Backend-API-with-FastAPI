from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')

JWT_SECRET = os.environ.get('JWT_SECRET')
VERIFICATION_SECRET = os.environ.get('VERIFICATION_SECRET')

EMAIL_SEND = os.environ.get('EMAIL_SEND')
EMAIL_PASS = os.environ.get('EMAIL_PASS')