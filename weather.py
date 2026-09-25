import requests

data = requests.get("https://ipapi.co").json()
print(data["city"])