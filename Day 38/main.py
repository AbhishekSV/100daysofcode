import requests
import datetime as dt
import os

APP_ID = os.environ.get('NTX_APP_IDE')
API_KEY = os.environ.get('NTX_AUT_TKN')

args = {
    "query": input("What did you do today?"),
    "gender":"",
    "weight_kg":,
    "height_cm":,
    "age":
    }

nutritionix_auth = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    }

nutritionix_response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', headers=nutritionix_auth, params=args)
nutritionix_response.raise_for_status()
exercises = nutritionix_response.json()["exercises"]

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

sheety_auth = {
    'Authorization': os.environ.get('SHT_AUT_TKN')
    }

for exercise in exercises:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=os.environ.get('SHT_END_PNT'), json=sheety_inputs, headers=sheety_auth)

    print(sheety_response.text)