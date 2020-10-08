from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Our New World!'


@app.route('/blog')
def blog():
    return 'wow this is a new Blog page'
