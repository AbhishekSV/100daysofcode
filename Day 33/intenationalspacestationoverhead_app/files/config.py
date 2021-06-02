import smtplib

class Emailer():
    
    
    def __init__(self):
        self.emailid = ''
        self.password = ''
        with smtplib.SMTP('smtp.gmail.com:587') as connection:
            connection.starttls()
            connection.login(user=self.emailid, password=self.password)
            connection.sendmail(from_addr=self.emailid, to_addrs=self.emailid,
                                     msg="Subject: International Space Station\n\nLookup it is passing over you!")
    