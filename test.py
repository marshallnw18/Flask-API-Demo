import requests 

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 41082, "name": "Day at the Zoo", "views": 200431},
        {"likes": 24908, "name": "Hiking the AT", "views": 100951},
        {"likes": 20091, "name": "Flask Web App Development", "views": 192780}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())