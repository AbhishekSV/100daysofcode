import requests as r
import datetime as dt

parameters = {
    "lat": 28.704060,
    "lng": 77.102493,
    "formatted": 0,
    }

response = r.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.status_code
data = response.json()
print(data['results']['sunrise'].split('T')[1].split(':'))
print(data['results']['sunset'].split('T')[1].split(':'))

time_now = dt.datetime.now()
print(time_now.hour)