import discord
from time import sleep
from globale_variabeln import *
from wetterabfrage import *
pushstarter1 = "/setpush"
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
####################################################

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(pushstarter1):
        loop = 0
        pushort = message.content.replace(pushstarter1, "")
        if len(pushort) < 1:
            await message.channel.send("Bitte Ort eingeben")
        else:
            temp = getWeather(pushort)[8]
            await message.channel.send("Du wirst benachrichtigt, wenn die Temperatur in" + pushort + " Unter 0°C sinkt. Aktuell liegt die Termperatur bei: " + str(temp) + "°C")
            while loop == 0:
                temp = getWeather(pushort)[8]
                if temp < 0:
                    await message.channel.send("Hey, in" + pushort + " ist die Temperatur unter 0°C gesunken. Die Pushmeldung wurde beendet.")
                    loop = 1
                else:
                    sleep(5)
                    await client.get_channel(timeoutchannel()).send("Testy")

client.run(get_token())