import os
import sys
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

from weather import get_tokyo_weather

weather_info, temp = get_tokyo_weather()
load_dotenv()

SENDER_MAIL = os.getenv('SENDER_EMAIL')
SENDER_PASS = os.getenv('SENDER_PASSWORD')
RECEIVER_MAIL = os.getenv('RECEIVER_EMAIL')

msg = MIMEText(f"東京の天気は{weather_info} `予想気温は{temp}です", "plain", "utf-8")
msg["Subject"] = "天気予報のお知らせ"
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
