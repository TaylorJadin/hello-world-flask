from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    return "<p>For more info check out: https://github.com/TaylorJadin/hello-world-flask</p>"