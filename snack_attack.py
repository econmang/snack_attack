#snack_attack.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
if TOKEN is None:
    raise Exception('DISCORD_TOKEN environment variable not set.')
if SERVER is None:
    raise Exception('DISCORD_SERVER environment variable not set.')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(
                        name='Snack Attack',
                        description='Bot to help order snacks for the gang.',
                        owner_id=1234567890,
                        intents=intents
                        )

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

    print(f'{client.user} has encountered an error.')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!'
            ]
    print(f'Content: {message.content}')
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


client.run(TOKEN)
