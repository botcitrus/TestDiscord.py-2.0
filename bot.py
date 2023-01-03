import discord
from discord.ext import commands
from nextcord.ext import commands
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
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import traceback
import random
import contextlib
import io
import os

intents = discord.Intents.all()
null_color=discord.Color.from_rgb(47,49,56)

client = commands.Bot(command_prefix="!", intents = intents, fetch_offline_members=True)
slash = SlashCommand(client, sync_commands = True, sync_on_cog_reload=True)

client.load_extension("cogs.faceit")
client.load_extension("cogs.lobby1")

@client.event
async def on_ready():
    while True:
              await client.change_presence(activity=discord.Streaming(name=f'Cyber Faceit', url="https://www.twitch.tv/qrushcsgo"))
              await asyncio.sleep(5)
              await client.change_presence(activity=discord.Streaming(name=f'{len(client.users)} пользователей', url="https://www.twitch.tv/qrushcsgo"))
              await asyncio.sleep(5)
			
@client.command()
@commands.is_owner()
async def files(ctx):
    embed = discord.Embed(title='Список файлов обнаруженных в директории `./cogs`:', color=null_color)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if f"cogs.{filename[:-3]}" in client.extensions:
                switcher = discord.utils.get(client.emojis, name="online")
            else:
                switcher = discord.utils.get(client.emojis, name="dnd")
            embed.add_field(name=filename, value=f'╰〔:page_with_curl:〕- `Размер`: {os.path.getsize(f"./cogs/{filename}") // 1024} Кбайт | `Загружен как ког:` {switcher}', inline=False)
    await ctx.reply(embed=embed, mention_author=False)
	
@client.command()
@commands.is_owner()
async def cog(
    ctx, 
    acti, 
    extension = None
    ):
    if extension == None:
        if acti == 'list':
            list = ", ".join([cog for cog in client.cogs])
            e = discord.Embed(title='Список агруженных когов:', description=f'**{list}**', color=null_color)
            await ctx.send(embed=e)
        else:   
            await ctx.message.add_reaction('⚠️')
    else:
        if acti == 'load':
            client.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'reload':
            client.reload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'unload':
            client.unload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('⚠️')
	
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

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

client.run('MTAyODM2OTQ2MTUwNzUyNjY5Nw.GT0X4g.8fFXB9ez0mZQ8tliBcpYxG3gcYOw33YTowerVw')
