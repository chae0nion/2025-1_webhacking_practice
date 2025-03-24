import requests

url = "http://localhost:5000"
cookies = {
    "key":"value"
}
data = {
    "key":"value"
}
response = requests.post(url=url, data=data, cookies=cookies)
print(response.text)
response = requests.head(url=url, params=data, cookies=cookies)
print(response.text, response.status_code)