import smtplib
import datetime as dt
import random


current_date = dt.datetime.now()
day_of_week = current_date.weekday()

emailid = ""
passwrd = ""

if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
    body = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=emailid, password=passwrd)
        connection.sendmail(from_addr=emailid, to_addrs="",
                            msg=f"Subject: Motivation\n\n{body}")
