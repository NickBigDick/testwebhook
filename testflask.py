import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__=="__main__":
        app.run(host="192.168.0.2", port=int(os.environ.get("PORT", 80)))

