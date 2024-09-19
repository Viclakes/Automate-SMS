import requests
from datetime import datetime

API_KEY = "6ecec8366cb1579234291dbfa88c7606"
LAT = 7.802540
LON = 5.412570
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()

now = datetime.now()
weekday = now.weekday()

data = response.json()
weather = data["list"][weekday]["weather"]
# print(data)
print(weather)
