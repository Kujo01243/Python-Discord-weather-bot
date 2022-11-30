import discord
import requests
import json
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

token = "MTA0NzE2MzM4OTkzMzI3NzIyNA.Guxsd6.UTQLlBNYp1boJk41j0bLqGpnRAM7FeHPVHEk1E"
api_key = "a46716a76c270dcc6f0ad9968d7c2eb9"

client.run(token)
