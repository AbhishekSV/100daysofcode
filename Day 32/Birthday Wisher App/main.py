import datetime as dt
import pandas as pd
import smtplib as sl
import random as r

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')
friends = data.to_dict(orient='records')
current_date = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
birthday_hooman = {hooman['name']:hooman['email'] for hooman in friends if hooman['month'] == current_date.month and hooman['day'] == current_date.day}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person,mailid in birthday_hooman.items():
    file_path = f'/letter_templates/letter_{r.randint(1,3)}.txt'
    with open(file_path, 'r') as f:
        body = ' '.join(f.readlines())
    body = body.replace('[NAME]',person)
    
# 4. Send the letter generated in step 3 to that person's email address.
    email = ''
    paswrd = ''
    with sl.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=email, password=paswrd)
        connection.sendmail(from_addr=email, to_addrs=mailid, msg=f"Subject: Happy Birthday!\n\n{body}")
