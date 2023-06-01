import requests
from datetime import datetime
from dotenv import dotenv_values

env_values = dotenv_values("../.env")

WEIGHT = 78
HEIGHT = 169
AGE = 27
GENDER = 'male'

headers = {
    'x-app-id': env_values.get("NUTRITION_ID"),
    'x-app-key': env_values.get("NUTRITION_KEY"),
}

query = input('Tell me which exercises you did:')

params = {
 "query": query,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', json=params, headers=headers)


def post_activity_to_sheet(data):
    headers = {
        'Authorization': 'Bearer ' + env_values.get("SHEETY_TOKEN"),
        "Content-Type": "application/json"
    }

    response = requests.post(
        url='https://api.sheety.co/dba10091bfc1ae6449190f47dae2f0a5/myWorkouts (udemy)/workouts',
        json=data,
        headers=headers
    )
    print(response.text)


for exercise in response.json()['exercises']:
    now = datetime.now()
    data = {
        'workout': {
            'date': now.strftime('%d/%m/%Y'),
            'time': now.strftime('%X'),
            'exercise': exercise['user_input'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    post_activity_to_sheet(data)


#
# # response = requests.get(
# #     url='https://api.sheety.co/dba10091bfc1ae6449190f47dae2f0a5/myWorkouts (udemy)/workouts',
# #     headers=headers
# # )
#
#
# response = requests.post(
#     url='https://api.sheety.co/dba10091bfc1ae6449190f47dae2f0a5/myWorkouts (udemy)/workouts',
#     headers=headers
# )
# print(response.text)

