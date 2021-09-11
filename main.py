# APIs
# https://www.nutritionix.com/business/api

import requests
import datetime as dt

APP_ID = 'b5cd7f1b'
API_KEY = 'e7a0d177b1cc6ea3dd19d9731b67d502'
nlp_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/aed6762a19a884464545a03871d4c4a9/myWorkouts/workouts'

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
    'Authorization': 'Basic bm96b211eW9zaGlkYTpub3pvMDExNi0='
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
