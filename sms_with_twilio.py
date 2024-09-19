import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Openweathermap
API_KEY = "6ecec8366cb1579234291dbfa88c7606"
LAT = 7.802540
LON = 5.412570
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio
account_sid = "AC65483ce40f97d55572c7a8ff0ce84b20"
auth_token = "4a9f87d68f20d3e9ef3f82eb0435d97a"

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ.get('HTTP_PROXY')}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                         body="It's going to rain today. You might want to take an umbrella along...",
                         from_='+18456533120',
                         to='+2348030842088'
                     )

    # print(message.sid)
    print(message.status)
