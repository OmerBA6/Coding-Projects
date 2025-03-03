from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'standard-all'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class PostForm(FlaskForm):
    title = StringField(label="Blog Title", validators=[DataRequired()])
    subtitle = StringField(label="Blog Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    image_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content")
    submit = SubmitField(label="Post Blog")


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def add_new_post():
    new_blog_form = PostForm()
    if new_blog_form.validate_on_submit():
        current_time = datetime.datetime.now()
        new_blog_post = BlogPost(title=new_blog_form.title.data,
                                 subtitle=new_blog_form.subtitle.data,
                                 date=f"{current_time.strftime('%B')} "
                                      f"{current_time.strftime('%d')}, "
                                      f"{current_time.strftime('%Y')}",
                                 body=new_blog_form.body.data,
                                 author=new_blog_form.author.data,
                                 img_url=new_blog_form.image_url.data)
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", blog_form=new_blog_form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_blog_form = PostForm(title=post_to_edit.title,
                              subtitle=post_to_edit.subtitle,
                              body=post_to_edit.body,
                              author=post_to_edit.author,
                              image_url=post_to_edit.img_url)
    if edit_blog_form.validate_on_submit():
        current_time = datetime.datetime.now()

        post_to_edit.title = edit_blog_form.title.data
        post_to_edit.subtitle = edit_blog_form.subtitle.data
        post_to_edit.date = (f"{current_time.strftime('%B')} "
                             f"{current_time.strftime('%d')}, "
                             f"{current_time.strftime('%Y')}")
        post_to_edit.body = edit_blog_form.body.data
        post_to_edit.author = edit_blog_form.author.data
        post_to_edit.img_url = edit_blog_form.image_url.data

        db.session.commit()
        return redirect(url_for('show_post', post_id=post_to_edit.id))

    return render_template('make-post.html', blog_form=edit_blog_form)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
