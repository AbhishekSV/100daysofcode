import os
from .InstaFollowerBot import InstaFollower

bot = InstaFollower()
bot.login()
bot.find_and_follow_followers_list()
bot.logout()