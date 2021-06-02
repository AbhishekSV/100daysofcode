import requests
from datetime import datetime
from files.config import Emailer

MY_LAT = 28.704060 # Your latitude
MY_LONG = 77.102493 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def check_overhead():
    if abs(iss_latitude - MY_LAT) < 10 and abs(iss_longitude - MY_LONG) < 10:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
if check_overhead and (time_now.hour >= sunset or time_now.hour <= sunrise):
    emailer = Emailer()

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.