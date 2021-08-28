from flask import Flask

app = Flask(__name__)

@app.route('/')
def webapp():
    return 'Hello World!'
