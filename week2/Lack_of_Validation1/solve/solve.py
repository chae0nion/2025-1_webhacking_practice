import requests

payload = """
***exploit XSS here.***
"""

data = {
    "url":f"/?html={payload}"
}

response = requests.post("http://127.0.0.1:30031/report", data=data)
print(response.text)