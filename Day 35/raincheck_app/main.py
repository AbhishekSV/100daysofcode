import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('TWI_ACC_SID')
auth_token = os.environ.get('TWI_AUT_TOK')

parameters = {
    'lat': 28.632429,
    'lon': 77.218788,
    'exclude': 'current,minutely,daily',
    'appid': os.environ.get('OWM_API_KEY'),
    }

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly']
rain_check = False
for hour in weather_data[:12]:
    for slice in hour['weather']:
        if slice['id'] < 700:
            rain_check = True
if rain_check:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Get an umbrella",
        from_=os.environ.get('TWI_PHN_NUM'),
        to=os.environ.get('ABI_PHN_NUM')
        )
    print(message.status)