# init steps in terminal:
# Libraries:
#   `pip install -U discord.py`
#   `pip install -U python-dotenv`
# Command to establish the connection:
#   `python bot.py`


import os

import discord
from dotenv import load_dotenv

from functions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Intents (Perms to access certain actions)
intents = discord.Intents.default()
intents.members = True

# Creating the Client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)


    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        # '\nGuild Members'
    )
    for member in guild.members: 
        print(f"-{member}")

@client.event
async def on_message(message):
    members = []
    guild = discord.utils.get(client.guilds, name=GUILD)

    for member in guild.members:
        members.append(member)

    if message.author == client.user:
        return

    polarity = get_polar(lemma_format(clean(message.content)))
    if polarity < -0.3:
        await message.channel.send(f"Mind your language {message.author.mention}")
        await message.channel.send(f"Because `{message.content}` has `{polarity}` polarity")
        await message.channel.send(f"Cleaned message: `{clean(message.content)}`")
        await message.channel.send(f"Lemmatized message: `{lemma_format(clean(message.content))}`")




client.run(TOKEN)