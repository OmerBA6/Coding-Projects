from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

COFFEE_RATING = ["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
WIFI_RATING = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER_OUTLET_RATING = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    url = StringField(label='URL', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open Time', validators=[DataRequired()])
    close_time = StringField(label='Close Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=COFFEE_RATING, validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Rating', choices=WIFI_RATING, validators=[DataRequired()])
    power_outlet_rating = SelectField(label='Power Outlet Rating', choices=POWER_OUTLET_RATING, validators=[DataRequired()])
    submit = SubmitField(label='Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as data_file:
            row_to_write = (f"{form.cafe.data},{form.url.data},{form.open_time.data},"
                            f"{form.close_time.data},{form.coffee_rating.data},"
                            f"{form.wifi_rating.data},{form.power_outlet_rating.data}")
            data_file.write(f"\n{row_to_write}")
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
