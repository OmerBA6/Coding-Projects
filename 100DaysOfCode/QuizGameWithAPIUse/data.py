import requests
import html

PARAM = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get("https://opentdb.com/api.php", PARAM)
response.raise_for_status()
data = response.json()['results']

question_data = [{'text': html.unescape(item['question']), 'answer': item['correct_answer']} for item in data]
