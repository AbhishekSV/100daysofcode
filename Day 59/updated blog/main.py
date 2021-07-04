from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/26b9e8c41536f5f06765").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/<filename>')
def redirect(filename):
    return render_template(filename)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

