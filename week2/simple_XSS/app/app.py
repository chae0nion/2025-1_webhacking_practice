from flask import Flask, request, render_template, make_response
import os, re
from flask import Flask, render_template, request, render_template_string
import os
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "couldn't find flag"

@app.route("/", methods=["GET"])
def index():
    html = request.args.get("html")
    
    return f"""
    <h1>simple XSS</h1>
    {html}
    
    If you find error, report the URL 
    <a href="/report">here</a>
    """
    
@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("report.html")

    if request.method == "POST":
        url = request.form.get("url")
        
        if not url:
            return "Invalid URL! Try again..."
        if re.match("http://.*", url) and not re.match("^/.*"):
            return "Invalid URL! Try again..."
        
        try:
            bot(url)
            return "report Succeed"
        except:
            return "Failed to visit URL"
    return "Unused Method!" 

def bot(url="/"):
    cookie = {"name": "flag", "value": FLAG}
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless=new",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(20)
        driver.get("http://127.0.0.1:5000/")
        driver.add_cookie(cookie)

        try:
            driver.get("http://127.0.0.1:5000/"+url)
        except:
            pass
    except Exception as e:
        driver.quit()
        print(e)
        return False

    driver.quit()
    return True

app.run(host="0.0.0.0", port=5000)