import os
import sys
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SENDER_MAIL = os.getenv('SENDER_EMAIL')
SENDER_PASS = os.getenv('SENDER_PASSWORD')
RECEIVER_MAIL = os.getenv('RECEIVER_EMAIL')

msg = MIMEText("メール本文をここに書き込む", "plain", "utf-8")
msg["Subject"] = "件名"
msg["From"] = SENDER_MAIL
msg["To"] = RECEIVER_MAIL


try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_MAIL, SENDER_PASS)
        server.sendmail(SENDER_MAIL, RECEIVER_MAIL, msg.as_string())
    print("メールを送信しました")

except Exception as e:
    print(f"送信失敗: {e}")
    sys.exit()
