import discord
from wetterabfrage import *
from abra

########################################################################################
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
commandstarter1 = "/weather"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(commandstarter1) and message.author != client.user:       #in eine funktion packen und dann auf weitere Eingabemöglichkeiten überprüfen
        eingabeort = message.content.replace(commandstarter1, "")
        eingabeort = eingabeort.lower()
        if len(eingabeort) < 1:
            await message.channel.send("Bitte Ort eingeben")
        else:
            sender = ("Das Wetter für: " + getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1]+ ":")
            await message.channel.send("Das Wetter für: " + getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1]+ ":" + "\nTemperatur: " + getWeather(eingabeort)[2] + "°C" +"\nLuftdruck: "+ getWeather(eingabeort)[3] + "mBar" + "\nLuftfäuchtigkeit: " + getWeather(eingabeort)[4] + "%" + "\nHimmel: " + getWeather(eingabeort)[5] + "\nWindgeschwindigkeit: " + getWeather(eingabeort)[6] + "m/s" + "\nWindrichtung: " + getWeather(eingabeort)[7] + "°")
        


 
client.run(gettoken())

# todo: token und api in seperates File!!!