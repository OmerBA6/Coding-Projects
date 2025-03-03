from flask import Flask, render_template
from post import Post
import requests

FAKE_BLOGS_API = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(FAKE_BLOGS_API).json()
posts_obj_list = []
for post in posts:
    posts_obj_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts_obj_list)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts_obj_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
