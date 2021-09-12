# APIs
# https://www.nutritionix.com/business/api
# https://sheety.co/

import requests
import datetime as dt

APP_ID = YOUR APP ID
API_KEY = YOUR API KEY
nlp_exercise_endpoint = YOUR NLP EXERCISE ENDPOINT
sheety_endpoint = YOUR SHHETY ENDPOINT

text_input = input('Tell me which exercises you did: ')
# text_input = 'ran 3 miles'


headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    # 'Content-Type': 'application',
}

nlp_exercise_params = {
    'query': text_input,
    "gender": "male",
    "weight_kg": 53,
    "height_cm": 176,
    "age": 23,
}

response = requests.post(url=nlp_exercise_endpoint, headers=headers, data=nlp_exercise_params)
data = response.json()

time = dt.datetime.now().strftime('%X')
date = dt.datetime.now().strftime('%Y/%m/%d')
exercise = data['exercises'][0]['name'].title()
duration = str(data['exercises'][0]['duration_min']) + ' min'
calories = data['exercises'][0]['nf_calories']

headers_sheety = {
    'Authorization': YOUR AUTHORIZATION
}

sheety_params = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

print(sheety_params)

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers_sheety)
print(response.json())
