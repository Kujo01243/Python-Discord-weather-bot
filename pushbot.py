import discord
from time import sleep
from keys import *
from wetterabfrage import *
####################################################
pushstarter1 = "/setpush"
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


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
            while loop == 0:
                temp = getWeather(pushort)[8]
                if temp < 0:
                    await message.channel.send("Hey, in" + pushort + " ist die Temperatur unter 0°C gesunken. Die Pushmeldung wurde beendet.")
                    loop = 1
                else:
                    sleep(2)


client.run(get_token())