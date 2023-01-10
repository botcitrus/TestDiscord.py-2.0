import discord
from discord.ext import commands
from discord import app_commands
from pymongo import MongoClient
from os import listdir as ld
from collections.abc import Sequence
import os
import time
import aeval
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

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix = ".", intents = intents)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")
    await client.change_presence(activity=discord.Streaming(name=f'Cyber Faceit', url="https://www.twitch.tv/qrushcsgo")
    
@client.command()
@commands.is_owner()
async def eval(ctx, *, ucode=None):
    tru = discord.utils.get(client.emojis, name='yes')
    err = discord.utils.get(client.emojis, name='no')
    code = '\n'.join(ucode.split('\n')[1:])[:-3] if ucode.startswith('```') and ucode.endswith('```') else ucode
    libs = {
        'discord': discord,
        'commands': commands,
        'bot': client,
        'client': client,
        'ctx': ctx
    }
    start = time.time()
    try:
        reval = await aeval.aeval(code, libs, {})
        end = time.time() - start
        emb = discord.Embed(title=f'{tru} Успешно:',
            description=f'**Время выполнения** - {end}\n'
                        f'**Входные данные** - \n```py\n{code}\n```\n'
                        f'**Выходные данные** - \n```py\n{reval}\n```\n',
            color=discord.Color.green())
        await ctx.send(embed=emb) 
    except Exception as exception:
        end = time.time() - start
        emb = discord.Embed(title=f'{err} Ошибка:',
            description=f'**Время выполнения** - {end}\n'
                        f'**Входные данные** - \n```py\n{code}\n```\n'
                        f'**Выходные данные** - \n```py\n{exception}\n```\n',
            color=discord.Color.red())
        await ctx.send(embed=emb)
    
async def load():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

async def bot():
    await load()
    await client.start('MTA1OTg4NjM3ODIyMzE2MTM4NA.GStMiN.FbPpxtCwK4PgOE423OPIZ8noyJwQnjKrTPyyC0')
    
asyncio.run(bot())
