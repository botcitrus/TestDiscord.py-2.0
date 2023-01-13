import discord
from discord import app_commands
import asyncio
from discord.ext import commands
import json
import asyncio
import random
import re
import time
from pymongo import MongoClient
import psutil
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests
import traceback
from asyncio import sleep
from io import BytesIO
import typing
import os
 
su_color=0x2ecc71
err_color=0xe74c3c
dark_red = 0x99aab5
base_color=0x8A2BE2
null_color=discord.Color.from_rgb(47,49,56)

class Faceit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient("mongodb+srv://Setroom:CFLrxCSX0fzBIMlA@cluster0.l9fw9.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.colluser = self.cluster.faceit.user
        self.collgame = self.cluster.faceit.game
	
    @commands.Cog.listener()
    async def on_ready(self):
        print("Faceit cog loaded.")
	
    @commands.command()
    async def game(self, ctx, name1: str = None, tag1: str = None, name2: str = None, tag2: str = None):
        tru = discord.utils.get(self.client.emojis, name='yes')
        err = discord.utils.get(self.client.emojis, name='no')
        if name1 is None:
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Укажите название первой команды!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        elif tag1 is None:
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Укажите тег первой команды!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        elif name2 is None:
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Укажите название второй команды!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        elif tag2 is None:
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Укажите тег второй команды!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"{tru} Успешно:",
                description = f"Игра команд: {name1} vs {name2} успешно создана!\nБот готов принимать ставки",
                color = 0x00FFFF
	    )
            await ctx.send(embed = embed)
        
async def setup(client):
    await client.add_cog(Faceit(client))
