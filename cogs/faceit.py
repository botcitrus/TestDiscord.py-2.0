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
            code = random.randrange(10000)
            post = {
                "code": code,
                "owner_id": ctx.author.id,
                "guild_id": ctx.guild.id,
                "name1": name1,
                "name2": name2,
                "tag1": tag1,
                "tag2": tag2,
                "membes1": [],
                "members2": []
            }

            self.collgame.insert_one(post)
            embed = discord.Embed(
                title = f"{tru} Успешно:",
                description = f"**{name1}** vs **{name2}**\n\nТеги команд: {tag1} vs {tag2}\n\nБот готов принимать ставки\n\nКод игры: {code}",
                color = 0x00FFFF
	    )
            await ctx.send(embed = embed)
		
    @commands.command()
    async def find(self, ctx, code: int = None):
        tru = discord.utils.get(self.client.emojis, name='yes')
        err = discord.utils.get(self.client.emojis, name='no')
        if code is None:
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Укажите код игры!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        elif not self.collgame.find_one({'guild_id': ctx.guild.id, "code": code}):
            embed = discord.Embed(
                title = f"{err} Ошибка:",
                description = f"Указаный вами код игры не найден!",
                color = discord.Color.red()
	    )
            await ctx.send(embed = embed)
        else:
            name1 = self.collgame.find_one({'guild_id': ctx.guild.id, "code": code})["name1"]
            name2 = self.collgame.find_one({'guild_id': ctx.guild.id, "code": code})["name2"]
            tag1 = self.collgame.find_one({'guild_id': ctx.guild.id, "code": code})["tag1"]
            tag2 = self.collgame.find_one({'guild_id': ctx.guild.id, "code": code})["tag2"]
            embed = discord.Embed(
                title = f"{name1} vs {name2}",
                description = f"Теги команд: {tag1}, {tag2}",
                color = 0x00FFFF
	    )
            await ctx.send(embed = embed)
		
    @commands.command()
    async def profile(self, ctx, member: discord.User = None):
        if member == None:
            member = ctx.author
	
        if not self.colluser.count_documents({"guild_id": ctx.guild.id, "user_id": member.id}):
            post = {
                "user_id": member.id,
                "guild_id": ctx.guild.id,
                "points": 50
            }
            self.colluser.insert_one(post)
		
        points = self.colluser.find_one({'guild_id': ctx.guild.id, "user_id": member.id})["points"]
        embed = discord.Embed(
            title = f"Профиль: {member}",
            description = f"Имя: {member.name}\nID: {member.id}\nPoints: {points}",
            color = 0x00FFFF
        )
        await ctx.send(embed = embed)
        
		
        
async def setup(client):
    await client.add_cog(Faceit(client))
