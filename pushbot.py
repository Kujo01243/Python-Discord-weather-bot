import discord
from time import sleep
from globale_variabeln import *
from wetterabfrage import *
pushstarter1 = pushbotstarter()
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
            embed = discord.Embed(title="Pushbot acticated",description="Du wirst benachrichtigt, wenn die Temperatur in" + pushort + " unter 0°C sinkt. Aktuell liegt die Termperatur bei: " + str(temp) + "°C" ,color=0x00ff00)
            await message.channel.send(embed=embed)
            while loop == 0:
                temp = getWeather(pushort)[8]
                if temp < 0:
                    embed = discord.Embed(title="Minusgrade!!!",description="Hey, in" + pushort + " ist die Temperatur unter 0°C gesunken. Die Pushmeldung wurde beendet. (aktuelle Temperatur: " + str(temp) + "°C)" ,color=0x0088ff)
                    await message.channel.send(embed=embed)
                    loop = 1
                else:
                    sleep(5)
                    await client.get_channel(timeoutchannel()).send("notimeout")

client.run(get_token())