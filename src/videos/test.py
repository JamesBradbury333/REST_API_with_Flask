import requests

# Location of API (server it is running on). This is the local host
BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1000, "name": "Cat_video", "views": 1002423},
        {"likes": 50, "name": "Chocolate_rain", "views": 300},
        {"likes": 153, "name": "Music_video", "views": 6526},
        {"likes": 30, "name": "Python_tutorial", "views": 301}]


for i, data_point in enumerate(data):
    print(f"{BASE}video/{str(i)}")
    print("Data point: ", data_point)
    response = requests.put(f"{BASE}video/{str(i)}", data_point)
    print(response.json())

#response = requests.delete(BASE + "")

input()

response = requests.get(BASE + "video/3")
print(response)

