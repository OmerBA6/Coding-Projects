import requests
from datetime import datetime

APP_ID = "8ff04350"
API_KEY = "82eecd0379e11000c48b7ee341877ad8"
EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USER_ID = ""
SHEETY_END_POINT = ""
SHETTY_BEARER_CODE = "sfasljkfnasdmlasdjnwedjklmasdm"

GENDER = "male"
WEIGHT_KG = "86"
HEIGHT_CM = "176"
AGE = "24"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

user_exercise = input("Tell me which exercise you did: ")

params = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

respond = requests.post(EXERCISE_END_POINT, json=params, headers=headers)
respond.raise_for_status()


current_time = datetime.now()
date = current_time.strftime("%d/%m/%Y")
time = current_time.strftime("%H:%M:%S")

for exercise_data in respond.json()['exercises']:
    sheet_input = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise_data['name'].title(),
            'duration': round(float(exercise_data['duration_min']), 2),
            'calories': round(float(exercise_data['nf_calories']), 2)
        }
    }
    headers = {
        "Authorization": f"Bearer {SHETTY_BEARER_CODE}"
    }
    respond = requests.post(SHEETY_END_POINT, json=sheet_input, headers=headers)
    print(respond.text)
