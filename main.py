import discord
token = "MTA0NzE2MzM4OTkzMzI3NzIyNA.Gbsj8-.8fCeZKmiDjc6P7y5l5qtiIvwIOZpHM8s78hZcg"
from wetterabfrage import *
########################################################################################
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
commandstarter = "weatherbot"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith(commandstarter) and message.author != client.user:
        eingabeort = message.content.replace(commandstarter, "")
        if len(eingabeort) < 1:
            await message.channel.send("Bitte Ort eingeben")
        else:
            sender = ("Das Wetter für: " + getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1]+ ":")
            await message.channel.send("Das Wetter für: " + getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1]+ ":")
            await message.channel.send("Temperatur:" + getWeather(eingabeort)[2] + "")


 
client.run(token)

