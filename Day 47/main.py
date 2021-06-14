from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.mime.text import MIMEText
import os

head = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    }
# 'https://www.flipkart.com/marq-flipkart-innoview-108-cm-43-inch-ultra-hd-4k-led-smart-android-tv/p/itmb05467f4bd72c'
tv_link = 'https://www.flipkart.com/iffalcon-tcl-108-cm-43-inch-ultra-hd-4k-led-smart-android-tv/p/itm3f760494090b0'

response = requests.get(url=tv_link, headers=head)
soup = BeautifulSoup(response.text, 'lxml')
click_to_buy = soup.find_all(name='button')
if click_to_buy[1].getText() != 'NOTIFY ME':
    msg = MIMEText(f'{tv_link}', 'html')
    email = os.environ.get('SMTP_MAIL_IDE')
    paswrd = os.environ.get('SMTP_MAIL_PWD')
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=email, password=paswrd)
        connection.sendmail(from_addr=email, to_addrs='abhisabnives@gmail.com', msg=f"Subject: iffalcon TV is now on sale!\n\n{msg}")
