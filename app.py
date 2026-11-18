#Flask file
#This code is from https://github.com/TrainWithShubham/github-actions-zero-to-hero/blob/main/app.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
