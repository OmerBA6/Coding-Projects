import requests


PARAM = {
    'amount': 40,
    'type': 'boolean'
}

response = requests.get("https://opentdb.com/api.php", PARAM)
response.raise_for_status()
question_data = response.json()['results']
