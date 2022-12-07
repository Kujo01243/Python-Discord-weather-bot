import discord
from wetterabfrage import *
from globale_variabeln import *
########################################################################################
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
commandstarter1 = weatherbotstarter()


@client.event

async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(commandstarter1) and message.author != client.user:       #in eine funktion packen und dann auf weitere Eingabemöglichkeiten überprüfen
        eingabeort = message.content.replace(commandstarter1, "")
        eingabeort = eingabeort.lower()
        if len(eingabeort) < 1:
            embed = discord.Embed(title="Error", description="Bitte Ort eingeben", color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Wetter:", color=0x00ff00)
            embed.add_field(name="Ort und Land:", value=getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1], inline=False)
            embed.add_field(name="Temperatur:", value=getWeather(eingabeort)[2] + "°C", inline=False)
            embed.add_field(name="Luftdruck:", value=getWeather(eingabeort)[3] + "mBar", inline=False)
            embed.add_field(name="Luftfäuchtigkeit:", value=getWeather(eingabeort)[4] + "%", inline=False)
            embed.add_field(name="Himmel:", value=getWeather(eingabeort)[5], inline=False)
            embed.add_field(name="Windgeschwindigkeit:", value=getWeather(eingabeort)[6] + "m/s", inline=False)
            embed.add_field(name="Windrichtung:", value=getWeather(eingabeort)[7] + "°", inline=False)
            await message.channel.send(embed=embed)

client.run(get_token())
