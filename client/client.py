import requests

res = requests.get("http://0.0.0.0:5000/buy")
print(res.json())