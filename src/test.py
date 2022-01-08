import requests

# Location of API (server it is running on). This is the local host
BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "helloworld/Jorge/7")

print(response.json())
