import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    fastfood_choices = [
        'Chick-fil-A! best choice if you want somthing delicous and fast!',
        'Subway. Best choice if you want something that is said to be healthier and you can design your own sandwitch!',
        'Taco Bell. Best choice if you wanna be gassy',
        'McDonalds! Best choice if you want something somewhat affordable and quick and easy!',
    ]
    if message.content == 'fast food!':
    #if message.content.startswith('$fast food'):
        response = random.choice(fastfood_choices)
        await message.channel.send(response)

client.run(TOKEN)
