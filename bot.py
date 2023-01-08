import discord
from discord.ext import commands
from discord import app_commands
from pymongo import MongoClient
from os import listdir as ld
from collections.abc import Sequence
import os
import time
import asyncio
import datetime
import sys
import re
import requests
import traceback
import random
import contextlib
import io
import os

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "!", intents = intents, application_id = "1059886378223161384")

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")
    await client.change_presence(activity=discord.Streaming(name=f'Cyber Faceit', url="https://www.twitch.tv/qrushcsgo"))

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message[0] == "!":
        return
    if message.author == client.user:
        return
    await message.channel.send("Hello friend")
    
async def load():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

async def bot():
    await load()
    await client.start('MTA1OTg4NjM3ODIyMzE2MTM4NA.GStMiN.FbPpxtCwK4PgOE423OPIZ8noyJwQnjKrTPyyC0')
    
asyncio.run(bot())
