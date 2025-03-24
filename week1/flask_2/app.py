from flask import Flask, request, render_template, make_response
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        return "POST!"
    return "Unused method!", 404 # status code

@app.route("/test")
def test():
    cookie = request.cookies.get('test_cookie')
    
    # quiz! 왜 \n을 썼는데 web에서 개행이 되지 않았을까요?
    response = make_response(f"set cookie!\nthis is your cookie : {cookie}")
    response.set_cookie('test_cookie', 'I_love_cookies!')
    return response

app.run(host="0.0.0.0", port=5000)