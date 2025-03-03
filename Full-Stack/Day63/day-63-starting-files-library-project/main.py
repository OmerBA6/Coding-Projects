from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books_list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form.get('book_name'),
                        author=request.form.get('book_author'),
                        rating=float(request.form.get('rating')))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    book_to_update = db.get_or_404(Book, book_id)
    if request.method == 'POST':
        book_to_update.rating = request.form.get('updated_rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_to_update)


@app.route("/delete/<book_id>")
def delete_book(book_id):
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

