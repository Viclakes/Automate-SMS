import requests

API_KEY = "6ecec8366cb1579234291dbfa88c7606"
LAT = 7.802540
LON = 5.412570
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_lists = weather_data["list"]

will_rain = False
for hour_data in weather_lists:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
else:
    print("Enjoy!")
