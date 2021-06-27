from flask import Flask, render_template
import requests
import datetime
# import random

app = Flask(__name__)

@app.route('/')
def index():
    # num = random.randint(1,10)
    yr = datetime.datetime.now().year
    return render_template('index.html', year=yr)


@app.route('/guess/<name>')
def guess(name):
    name_to_show = name.capitalize()
    age_response = requests.get(f'https://api.agify.io/?name={name}')
    age = age_response.json()['age']
    gender_response = requests.get(f'https://api.genderize.io/?name={name}')
    gender = gender_response.json()['gender']
    return render_template('guess.html', name=name_to_show, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5a063bfd9424376c26af"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)    


if __name__ == '__main__':
    app.run(debug=True)