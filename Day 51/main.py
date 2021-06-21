import os
from .BotClass import InternetSpeedTwitterBot

PROMISED_UP = 100
PROMISED_DOWN = 80

TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

bot = InternetSpeedTwitterBot()