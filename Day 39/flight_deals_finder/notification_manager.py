from twilio.rest import Client
import os

TWILIO_SID = os.environ.get('TWI_ACC_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWI_AUT_TKN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWI_PHN_NUM')
TWILIO_VERIFIED_NUMBER = os.environ.get('ABI_PHN_NUM')


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
        # Prints if successfully sent.
        print(message.sid)