import datetime
import requests
import json
import time
from globale_variabeln import *
####################################################

def getWeather(ort):
    serviceURL = "https://api.openweathermap.org/data/2.5/weather"
    firstTime = True
    while firstTime == True:
        requestStr = serviceURL + "?q=" + ort + "&units=metric&lang=de&appid=" + get_api()
        responseStr = requests.get(requestStr)

        jsonResponse = json.loads(responseStr.text)
        ortsname = jsonResponse['name']
        land = jsonResponse['sys']['country']
        temp = jsonResponse['main']['temp']
        pressure = str(jsonResponse['main']['pressure'])
        humidity = str(jsonResponse['main']['humidity'])
        lon = str(jsonResponse['coord']['lon'])
        lat = str(jsonResponse['coord']['lat'])
        cloud = jsonResponse['weather'][0]['description']
        windSpeed = str(jsonResponse['wind']['speed'])
        windDirection = str(jsonResponse['wind']['deg'])
        firstTime = False
        returnwert = [ortsname, land, str(temp), pressure, humidity, cloud, windSpeed, windDirection, temp]
        return returnwert



