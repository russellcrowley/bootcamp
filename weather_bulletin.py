import keyring
import requests
from datetime import datetime
from emailer import emailer

def weather_bulletin(lat=53.4808, lon=2.2426, location="Your location"):
""" Queries the openweather API, parses the response and provides a personalised weather report for the next week.
Takes latitude (float), longitude (float) and name of location (string) as arguments, or defaults to Manchester.
You need to sign up for an API key at https://home.openweathermap.org/users/sign_up for this function to work"""
    exclude = "current,minutely,hourly,alerts"
    API_key = XXXX # you need to sign up for an openweather API key and put it here
    # get the weather return
    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_key}")
    r = r.json()
    #  parse and save relevant weather predictions
    weather = [[] for i in range(6)]
    for i in range(6):
        day = r["daily"][i]
        weather[i].append(datetime.utcfromtimestamp(day['dt']).strftime('%A %d %B'))
        weather[i].append(day["weather"][0]["main"])
        weather[i].append(day["weather"][0]["description"])
        weather[i].append(int(day['temp']['min'] - 273.15))
        weather[i].append(int(day['temp']['max'] - 273.15))

    bulletin_weather = f"Here's the weather for {location} for the next week:\n"
    for i in range(6):
        bulletin_weather += f"{weather[i][0]} - {weather[i][1]} ({weather[i][2]}), min {weather[i][3]}C, max {weather[i][4]}C\n"
    return bulletin_weather

def main():
    bulletin = weather_bulletin()
    print(bulletin)
    # uncomment the line below to get this as an email insteat
    # emailer("Weather bulletin", bulletin)

if __name__ == "__main__":
    main()
