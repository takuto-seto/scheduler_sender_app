import os
import sys
import logging
import unittest
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from weather import get_tokyo_weather, WeatherAPIError


def send_weather_mail():
    try:
        weather_info, temp = get_tokyo_weather()
        load_dotenv()

        SENDER_MAIL = os.getenv('SENDER_EMAIL')
        SENDER_PASS = os.getenv('SENDER_PASSWORD')
        RECEIVER_MAIL = os.getenv('RECEIVER_EMAIL')

        msg = MIMEText(f"東京の天気は{weather_info} `予想気温は{temp}です", "plain", "utf-8")
        msg["Subject"] = "天気予報のお知らせ"
        msg["From"] = SENDER_MAIL
        msg["To"] = RECEIVER_MAIL

        logging.info("serverへ接続開始")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_MAIL, SENDER_PASS)
            server.sendmail(SENDER_MAIL, RECEIVER_MAIL, msg.as_string())
            logging.info("メール送信完了")

    except WeatherAPIError as e:
        logging.error(f"天気データ取得エラー{e}")
        sys.exit()

