import requests

url = "http://127.0.0.1:5000/wallet/add"
data = {"amount": 250}

response = requests.post(url, json=data)
print(response.text)
