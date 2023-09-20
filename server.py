from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "Hello, Justin!"

@app.route("/blog")
def blog():
    return "these are my thoughts on blogs"

