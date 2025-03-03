from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIES_DATABASE_API_MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie"
MOVIES_DATABASE_API_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIES_DATABASE_IMAGE_URL = "https://image.tmdb.org/t/p/original"
MOVIES_DATABASE_API_KEY = ""
HEADERS = {
    "accept": "application/json",
    "Authorization": ""
}

# ---------------------------- Flask App Creation -------------------------- #
app = Flask(__name__)
# --------------------------------------------------------------------------- #


# ---------------------------- Flask-Bootstrap Initiation ------------------ #
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# --------------------------------------------------------------------------- #


# --------------------------- Flask-SQLAlchemy Initiation ------------------ #
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///favorite_movies.db"
db = SQLAlchemy()
db.init_app(app)
# --------------------------------------------------------------------------- #


# ------------------------------ Table Creation ------------------------------------ #
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()
# ---------------------------------------------------------------------------------- #


# ------------------------------- Forms Declaration -------------------------------- #
class EditForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField(label="Update")


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
# ---------------------------------------------------------------------------------- #


@app.route("/")
def home():
    # result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    # all_movies = [db.get_or_404(Movie, movie.id) for movie in result.scalars()]
    #
    # ranking_index = 1
    # for movie in all_movies:
    #     movie.ranking = ranking_index
    #     ranking_index += 1
    #     db.session.commit()
    #
    # result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    # return render_template("index.html", movies=result.scalars())

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie_to_edit = db.get_or_404(Movie, movie_id)
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        movie_to_edit.rating = float(edit_form.rating.data)
        movie_to_edit.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_edit, edit_form=edit_form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    book_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if request.method == 'GET':
        movie_to_add_id = request.args.get('movie_id')
        if movie_to_add_id:
            response = requests.get(f"{MOVIES_DATABASE_API_MOVIE_DETAILS_URL}/{movie_to_add_id}", headers=HEADERS)
            response.raise_for_status()
            movie_details = response.json()

            new_movie = Movie(title=movie_details['title'],
                              img_url=f"{MOVIES_DATABASE_IMAGE_URL}{movie_details['poster_path']}",
                              description=movie_details['overview'],
                              year=int(movie_details['release_date'].split('-')[0]))
            print(new_movie.img_url)
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('edit', movie_id=new_movie.id))

    elif form.validate_on_submit():
        movie_to_add_title = form.title.data
        params = {
            "query": movie_to_add_title
        }
        response = requests.get(MOVIES_DATABASE_API_SEARCH_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        results = response.json()['results']
        return render_template('select.html', movies=results)

    return render_template('add.html', add_form=form)


if __name__ == '__main__':
    app.run(debug=True)
