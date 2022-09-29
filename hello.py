from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><p><a href='https://support.reclaimhosting.com/hc/en-us/articles/9220813439127'>More info</a></p>"
