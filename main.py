import requests
from datetime import datetime as dt
import os

APP_ID = "79e5640e"
API_KEY = "ab9dd059ffd6ce3e81cb20c58e50097b"
NLP_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
AGE = 22
HEIGHT = 175
WEIGHT = 73
BEARER_TOKEN = "Bearer 0Uevqywx2kazJBo/oJGvZfngS8LCKUcWJLTsGJ7W05TLq2ae=D9m4Lo?bwE68v2?"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = {
    "query": input("Tell me about today's Workout😄: "),
    "gender": GENDER,
    "age": AGE,
    "height_cm": HEIGHT,
    "weight_kg": WEIGHT,
}
response = requests.post(url=NLP_EXERCISE_ENDPOINT, json=data, headers=headers)
json_data = response.json()

# Sheety


SHEETY_ENDPOINT = "https://api.sheety.co/b558c0a83c8826c9f43a9b910d067df3/workoutTracking/workouts"

today = dt.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

headers = {
    "Authorization": BEARER_TOKEN
}

for exercise in json_data["exercises"]:
    sheety_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data, headers=headers)
    print(response.text)






















