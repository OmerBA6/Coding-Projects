from flask import Flask, render_template
import requests

AGIFY_API_URL = "https://api.agify.io"
GENDERIZE_API_URL = "https://api.genderize.io"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/guess/<name>")
def guess(name):
    params = {
        'name': name
    }
    age_data = requests.get(url=AGIFY_API_URL, params=params).json()
    gender_data = requests.get(url=GENDERIZE_API_URL, params=params).json()

    age = age_data['age']
    gender = gender_data['gender']

    return render_template('guess_page.html', name=name.title(), age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)