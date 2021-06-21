import os
from .BotClass import InternetSpeedTwitterBot

PROMISED_UP = 100
PROMISED_DOWN = 80

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()