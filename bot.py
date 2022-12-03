import discord
import requests
token = "MTA0NzE2MzM4OTkzMzI3NzIyNA.Gbsj8-.8fCeZKmiDjc6P7y5l5qtiIvwIOZpHM8s78hZcg"
api_key = "a46716a76c270dcc6f0ad9968d7c2eb9"

########################################################################################
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
client.run(token)
