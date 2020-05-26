# bot.py
import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
TOKEN = "NzE0ODg2OTEwNDI5ODg4NjQz.Xs1Nfw.0jUhl23eeeV76dVbJthtfPtyeRM"
GUILD = "Cansi Crew"
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)