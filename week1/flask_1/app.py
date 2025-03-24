from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return "my_web"

app.run()