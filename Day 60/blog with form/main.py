from flask import Flask, render_template, request
import requests
import smtplib
import os

posts = requests.get("https://api.npoint.io/26b9e8c41536f5f06765").json()
EMAIL_ID = os.environ.get('EMAIL_ID')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def redirect():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=EMAIL_ID, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ID, to_addrs=EMAIL_ID, msg=email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

