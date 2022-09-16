from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><p><a href='https://github.com/TaylorJadin/hello-world-flask'>More info</a></p>"