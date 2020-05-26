# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    xingamento = [
        'Nossa que tune manjado',
        'Música merda',
        'Toca aquela do Israel Vibrations agora',
        'Não não não, next tune my selectah',
        'Cansaaaaaaaaaaaado',
        'Finalmente acertou uma!'
    ]

    if '!play' in message.content:
    #if message.content == '!play': 
        response = random.choice(xingamento)
        await message.channel.send(response)


client.run(TOKEN)