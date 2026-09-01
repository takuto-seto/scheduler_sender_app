import os
from dotenv import load_dotenv

load_dotenv()

SENDER_MAIL = os.getenv('SENDER_EMAIL')
SENDER_PASS = os.getenv('SENDER_PASSWORD')
RECEIVER_MAIL = os.getenv('RECEIVER_EMAIL')

print(SENDER_MAIL)
print(SENDER_PASS)
print(RECEIVER_MAIL)