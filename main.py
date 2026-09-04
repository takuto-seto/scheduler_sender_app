import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from send_mail import send_weather_mail

logging.basicConfig(
    filename='log/app.log',
    format='%(asctime)s %(levelname)s %(message)s ',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


sched = BlockingScheduler()

def job():
    send_weather_mail()

sched.add_job(job, 'cron', hour=20, minute=34)
sched.start()