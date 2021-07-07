from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    credentials = {
        'username': request.form['username'],
        'password': request.form['password']
    }
    return render_template('login.html', cred = credentials)


if __name__ == '__main__':
    app.run(debug=True)