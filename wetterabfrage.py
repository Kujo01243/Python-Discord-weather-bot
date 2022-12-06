
import datetime
import requests
import json
import time


def getWeather(ort):
    serviceURL = "https://api.openweathermap.org/data/2.5/weather"

    appId = "a46716a76c270dcc6f0ad9968d7c2eb9"


    firstTime = True
    while firstTime == True:
        requestStr = serviceURL + "?q=" + ort + "&units=metric&lang=de&appid=" + appId
        responseStr = requests.get(requestStr)

        jsonResponse = json.loads(responseStr.text)
        ortsname = jsonResponse['name']
        land = jsonResponse['sys']['country']
        temp = jsonResponse['main']['temp']
        pressure = jsonResponse['main']['pressure']
        humidity = jsonResponse['main']['humidity']
        lon = jsonResponse['coord']['lon']
        lat = jsonResponse['coord']['lat']
        cloud = jsonResponse['weather'][0]['description']
        windSpeed = jsonResponse['wind']['speed']
        windDirection = jsonResponse['wind']['deg']
        firstTime = False
        returnwert = [ortsname, land, temp, pressure, humidity, cloud, windSpeed, windDirection]
        return returnwert



