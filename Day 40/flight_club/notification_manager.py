from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ.get('TWI_ACC_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWI_AUT_TKN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWI_PHN_NUM')
TWILIO_VERIFIED_NUMBER = os.environ.get('ABI_PHN_NUM')
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com:587"
MY_EMAIL = os.environ.get('ABI_EML_IDE')
MY_PASSWORD = os.environ.get('ABI_EML_PWD')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )