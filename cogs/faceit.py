import discord
import asyncio
from discord.ext import commands
from discord.ext.commands.core import bot_has_guild_permissions
from Cybernator import Paginator as pag
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
import random
import re
import time
from pymongo import MongoClient
import psutil
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
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
        self.collection = self.cluster.afraid.afraiduser
        self.collgame = self.cluster.afraid.afraidgame
	
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = self.client.get_channel(1028330501112606873)
        cte = self.client.get_channel(1028603724156895272)
        ter = self.client.get_channel(1028603698974306395)
        guild = self.client.get_guild(1028330500579938424)
        test = self.client.get_channel(1028330501112606872)
        rezult = self.client.get_channel(1028330501112606872)
        members = channel.members #finds members connected to the channel

        memids = [] #(list)
        for member in members:
            memids.append(member)

        voice_members_count = len(channel.members)
	
        if after.channel == channel and after.channel!=before.channel:
            if voice_members_count == 10:
                value1 = random.choice(memids)
                memids.remove(value1)
                value2 = random.choice(memids)
                memids.remove(value2)
                value3 = random.choice(memids)
                memids.remove(value3)
                value4 = random.choice(memids)
                memids.remove(value4)
                value5 = random.choice(memids)
                memids.remove(value5)
                value6 = random.choice(memids)
                memids.remove(value6)
                value7 = random.choice(memids)
                memids.remove(value7)
                value8 = random.choice(memids)
                memids.remove(value8)
                value9 = random.choice(memids)
                memids.remove(value9)
                value10 = random.choice(memids)
		
                one1 = self.collection.find_one({'guild_id': guild.id, 'user_id': value1.id})['lvlfaceit']
                one2 = self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['lvlfaceit']
                one3 = self.collection.find_one({'guild_id': guild.id, 'user_id': value3.id})['lvlfaceit']
                one4 = self.collection.find_one({'guild_id': guild.id, 'user_id': value4.id})['lvlfaceit']
                one5 = self.collection.find_one({'guild_id': guild.id, 'user_id': value5.id})['lvlfaceit']
                one6 = self.collection.find_one({'guild_id': guild.id, 'user_id': value6.id})['lvlfaceit']
                one7 = self.collection.find_one({'guild_id': guild.id, 'user_id': value7.id})['lvlfaceit']
                one8 = self.collection.find_one({'guild_id': guild.id, 'user_id': value8.id})['lvlfaceit']
                one9 = self.collection.find_one({'guild_id': guild.id, 'user_id': value9.id})['lvlfaceit']
                one10 = self.collection.find_one({'guild_id': guild.id, 'user_id': value10.id})['lvlfaceit']
		
	
                lvl1 = discord.utils.get(self.client.emojis, name=f'{one1}lvl')
                lvl2 = discord.utils.get(self.client.emojis, name=f'{one2}lvl')
                lvl3 = discord.utils.get(self.client.emojis, name=f'{one3}lvl')
                lvl4 = discord.utils.get(self.client.emojis, name=f'{one4}lvl')
                lvl5 = discord.utils.get(self.client.emojis, name=f'{one5}lvl')
                lvl6 = discord.utils.get(self.client.emojis, name=f'{one6}lvl')
                lvl7 = discord.utils.get(self.client.emojis, name=f'{one7}lvl')
                lvl8 = discord.utils.get(self.client.emojis, name=f'{one8}lvl')
                lvl9 = discord.utils.get(self.client.emojis, name=f'{one9}lvl')
                lvl10 = discord.utils.get(self.client.emojis, name=f'{one10}lvl')
                cap = discord.utils.get(self.client.emojis, name='captain')
		
                await rezult.set_permissions(value1, send_messages=True)
                await rezult.set_permissions(value6, send_messages=True)
	
	
                await channel.set_permissions(guild.default_role, connect = False)
                sandstone = discord.utils.get(self.client.emojis, name='sandstone')
                province = discord.utils.get(self.client.emojis, name='province')
                sakura = discord.utils.get(self.client.emojis, name='sakura')
                rust = discord.utils.get(self.client.emojis, name='rast')
                zone = discord.utils.get(self.client.emojis, name='zone')
                ct = discord.utils.get(self.client.emojis, name='ct')
                t = discord.utils.get(self.client.emojis, name='t_')
                typing = discord.utils.get(self.client.emojis, name='loading')
                captain = discord.utils.get(self.client.emojis, name='captain')
	
	
                gametag = random.randrange(70000)
                gamemap = random.choice(['Sandstone','Sakura','Rust','Province','Zone','Breez'])
			
                if gamemap == "Sandstone":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {sandstone}  {gamemap}",
                        colour=0x00FF00
                    )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
                if gamemap == "Sakura":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {sakura}  {gamemap}",
                        colour=0x00FF00
                        )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
		    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
                if gamemap == "Breez":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {sakura}  {gamemap}",
                        colour=0x00FF00
                        )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
		    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
                if gamemap == "Rust":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {rust}  {gamemap}",
                        colour=0x00FF00
                    )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
                if gamemap == "Province":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {province}  {gamemap}",
                        colour=0x00FF00
                    )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
                if gamemap == "Zone":
                    post = {
                        "guild_id": guild.id,
		        "codegame": gametag,
                        "mapgame": gamemap,
                        "value1": value1.id,
                        "value1k": 0,
                        "value1d": 0,
			"value1kd": 0,
                        "value2": value2.id,
                        "value2k": 0,
                        "value2d": 0,
			"value2kd": 0,
                        "value3": value3.id,
                        "value3k": 0,
                        "value3d": 0,
			"value3kd": 0,
                        "value4": value4.id,
                        "value4k": 0,
                        "value4d": 0,
			"value4kd": 0,
                        "value5": value5.id,
                        "value5k": 0,
                        "value5d": 0,
			"value5kd": 0,
                        "value6": value6.id,
                        "value6k": 0,
                        "value6d": 0,
			"value6kd": 0,
                        "value7": value7.id,
                        "value7k": 0,
                        "value7d": 0,
			"value7kd": 0,
                        "value8": value8.id,
                        "value8k": 0,
                        "value8d": 0,
			"value8kd": 0,
                        "value9": value9.id,
                        "value9k": 0,
                        "value9d": 0,
			"value9kd": 0,
                        "value10": value10.id,
                        "value10k": 0,
                        "value10d": 0,
			"value10kd": 0,
                        "reg": 0
		    }
                    self.collgame.insert_one(post)
                    e = discord.Embed(
                        title = f"#{gametag} | {zone}  {gamemap}",
                        colour=0x00FF00
                    )
                    e.add_field(
                        name=f'COUNTER-TERRORISTS\u200b  {ct}',
                        value=f"{lvl1}  {value1}  {captain}\n{lvl2}  {value2}\n{lvl3}  {value3}\n{lvl4}  {value4}\n{lvl5}  {value5}",
                        inline=False
                    )
                    e.add_field(
                        name=f'TERRORISTS\u200b  {t}',
                        value=f"{lvl6}  {value6}  {captain}\n{lvl7}  {value7}\n{lvl8}  {value8}\n{lvl9}  {value9}\n{lvl10}  {value10}",
                        inline=False
                    )
                    e.add_field(
                        name=f'\u200b',
                        value=f"{value2} хостит {typing}\nМы прислали его игровой ID ниже",
                        inline=False
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await test.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    await rezult.send(f"{self.collection.find_one({'guild_id': guild.id, 'user_id': value2.id})['idgame']}", embed=e)
                    return
		
    @cog_ext.cog_slash(name="game_id", description="Показывает игровой ID", options = [{"name": "member", "description": "Пользователь", "type": 6, "requied": False}])
    async def game_id(self, ctx, member: discord.member = None):
        if member == None:
            member = ctx.author
        await ctx.send(f"{self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['idgame']}")
	
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def blacklist(self, ctx, member: discord.Member = None):
        banlist = self.client.get_channel(1016042483924353135)
        if member is None:
            e = discord.Embed(
                title = "Ошибка",
                description = "Укажите пользователя",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['blacklist'] == 1:
            e = discord.Embed(
                title = "Ошибка",
                description = "Пользователь уже находиться в чёрном списке",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        else:
            addbanlist = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['blacklist'] + 1
            self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'blacklist': addbanlist}})
            role = discord.utils.get(member.guild.roles, id=1017109372654076005)
            await member.add_roles(role)
            e = discord.Embed(
                description = f"{member.mention} добавлен в чёрный список",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await banlist.send(embed=e)
	
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblacklist(self, ctx, member: discord.Member = None):
        banlist = self.client.get_channel(1016042483924353135)
        if member is None:
            e = discord.Embed(
                title = "Ошибка",
                description = "Укажите пользователя",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['blacklist'] == 0:
            e = discord.Embed(
                title = "Ошибка",
                description = "Пользователя нет в чёрном списке",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        else:
            addbanlist = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['blacklist'] - 1
            self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'blacklist': addbanlist}})
            role = discord.utils.get(member.guild.roles, id=1017109372654076005)
            await member.remove_roles(role)
            e = discord.Embed(
                description = f"{member.mention} убран из чёрного списка",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await banlist.send(embed=e)
		
    @cog_ext.cog_slash(name="info", description="информация о пользователе", options = [{"name": "league", "description": "Интересующая вас лига", "type": 3, "required": True, "choices": [{"name": "Default", "value": "def"}, {"name": "Qualifications", "value": "qual"}, {"name": "Pro League", "value": "pro"}]},{"name": "member", "description": "Пользователь", "type": 6, "requied": False}])
    async def info(self, ctx, league: str, member: discord.member = None):
        online = discord.utils.get(self.client.emojis, name='status_online')
        offline = discord.utils.get(self.client.emojis, name='status_offline')
        if member == None:
            member = ctx.author
	
        if league == 'def':	
            if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 300:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 2:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944501808246878)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 600:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 3:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944577326694460)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 900:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 4:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944670268280890)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 1100:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 5:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944770260475986)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 1400:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 6:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944848907882627)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 1600:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 7:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944880084135936)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 1800:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 8:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014944884123246692)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 2000:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 9:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014945267247763466)
                    await member.add_roles(role)
            elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] == 2500:
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 10:
                    pass
                else:
                    lvlr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': member.id}, {'$set':{'lvlfaceit': lvlr}})
                    role = discord.utils.get(member.guild.roles, id=1014945367508394096)
                    await member.add_roles(role)
	
            if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['calibration'] < 10:	
                namegame = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['name']
                image = Image.open("ProfileCalibration.png")
                img = image.resize((1400, 1250))
                idraw = ImageDraw.Draw(img)
                membere = ImageFont.truetype('FiraCode-Light.ttf', size = 25)
                stats = ImageFont.truetype('FiraCode-Light.ttf', size = 75)
                stat = ImageFont.truetype('FiraCode-Light.ttf', size = 50)
                statswn = ImageFont.truetype('FiraCode-Light.ttf', size = 40)
                winratere = ImageFont.truetype('FiraCode-Light.ttf', size = 17)
                mmrer = ImageFont.truetype('FiraCode-Light.ttf', size = 22)
                kder = ImageFont.truetype('FiraCode-Light.ttf', size = 60)
                mgs = f'{namegame}'	
                idraw.text((375, 167), mgs, font = membere, fill = "white")
		
                cal = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['calibration']
                calibration = f'Calibration {str(cal)}/10'	
                idraw.text((170, 825), calibration, font = membere, fill = "salmon")
			
                calibration = f'Calibration 0/10'	
                idraw.text((170, 825), calibration, font = membere, fill = "salmon")
		
                mmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr']
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 300:
                    mmre = f"{str(mmr)}/300"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 300 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 600:
                    mmre = f"{str(mmr)}/600"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 600 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 900:
                    mmre = f"{str(mmr)}/900"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 900 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1100:
                    mmre = f"{str(mmr)}/1100"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1100 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1400:
                    mmre = f"{str(mmr)}/1400"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1400 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1600:
                    mmre = f"{str(mmr)}/1600"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1600 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1800:
                    mmre = f"{str(mmr)}/1800"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1800 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 2000:
                    mmre = f"{str(mmr)}/2000"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 2000 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 2500:
                    mmre = f"{str(mmr)}/2500"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 2500:
                    mmre = f"{str(mmr)}"
                    idraw.text((600, 199), mmre, font = mmrer, fill = "white")
	
                avatar = member.avatar_url_as(size = 128)
                avt = BytesIO(await avatar.read())
                imga = Image.open(avt)
                imguser = imga.resize((250, 250))
	
                lvle = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit']
                lvlfaceit = Image.open(f"facei{lvle}.png")
                imgty = lvlfaceit.resize((68, 50))
                idraw = ImageDraw.Draw(imgty)

                img.paste(imguser, (100, 100))
                img.paste(imgty, (375, 271), imgty)
                img.save("profilet.png")
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['pro_league'] == 0:
                    cyber_stats = "Недоступно"
                    cyber_offliner = f"{offline}"
                else:
                    cyber_stats = "Доступно"
                    cyber_offliner = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['qualification'] == 0:
                    cyber_qual = "Недоступно"
                    cyber_offliner_qual = f"{offline}"
                else:
                    cyber_qual = "Доступно"
                    cyber_offliner_qual = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 1:
                    color = 0x00FF00
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 2:
                    color = 0x00FFFF
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 3:
                    color = 0x000080
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 4:
                    color = 0xDC143C
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 5:
                    color = 0xc301ff
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 6:
                    color = 0xFFFF00
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 7:
                    color = 0xEE82EE
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 8:
                    color = 0xFFD700
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 9:
                    color = 0x00aa36
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 10:
                    color = 0xFF0000
	
                file = discord.File("profilet.png")
                e = discord.Embed(
                    description = f"**DEFAULT LEAGUE** {online} _Активно_\n**QUALIFICATIONS LEAGUE** {cyber_offliner_qual} _{cyber_qual}_\n**CYBER PRO LEAGUE** {cyber_offliner} _{cyber_stats}_",
                    colour=color
                )
                e.set_image(url = 'attachment://profilet.png')
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(f"||{self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['idgame']}||", file=file, embed=e)
            else:
                namegame = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['name']
                image = Image.open("ProfileBack.png")
                img = image.resize((1400, 1250))
                idraw = ImageDraw.Draw(img)
                membere = ImageFont.truetype('FiraCode-Light.ttf', size = 25)
                stats = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                stat = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                statswn = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                winratere = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                mmrer = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                fple = ImageFont.truetype('FiraCode-Light.ttf', size = 30)
                kder = ImageFont.truetype('FiraCode-Light.ttf', size = 20)
                mgs = f'{namegame}'	
                idraw.text((375, 167), mgs, font = membere, fill = "white")
                fpler = "default"
                idraw.text((988, 300), fpler, font = fple, fill = "white")
                rankings = self.collection.find({"guild_id": ctx.guild.id}).sort("mmr", -1)
                i = 0
                for x in rankings:
                    try:
                        i += 1
                    except:
                        pass
		
                place = f"{i}"
                idraw.text((1250, 300), place, font = fple, fill = "white")
		
                killes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'])
                idraw.text((206, 985), killes, font = statswn, fill = "greenyellow")
                deathes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths'])
                idraw.text((369, 985), deathes, font = statswn, fill = "salmon")
                kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                if kd == 0:
                    kd = str(0)
                    idraw.text((301, 945), kd, font = stats, fill = "greenyellow")
                    idraw.text((140, 710), kd, font = stats, fill = "greenyellow")
                else:
                    kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills']/self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                    x = str(float('{:.2f}'.format(kd)))
                    idraw.text((301, 945), x, font = stat, fill = "greenyellow")
                    idraw.text((125, 710), x, font = stats, fill = "greenyellow")

                wins = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'])
                idraw.text((196, 845), wins, font = statswn, fill = "greenyellow")
                loses = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses'])
                idraw.text((351, 845), loses, font = statswn, fill = "salmon")
	
                winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                if winrate == 0:
                    winrate = f"{str(0)}%"
                    idraw.text((265, 805), winrate, font = stats, fill = "greenyellow")
                else:
                    winrater = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] + self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                    winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins']/winrater*100
                    x = f"{str(float('{:.1f}'.format(winrate)))}%"
                    idraw.text((265, 805), x, font = stat, fill = "greenyellow")
		
                mmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr']
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 300:
                    mmre = f"{str(mmr)}/300"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 300 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 600:
                    mmre = f"{str(mmr)}/600"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 600 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 900:
                    mmre = f"{str(mmr)}/900"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 900 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1100:
                    mmre = f"{str(mmr)}/1100"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1100 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1400:
                    mmre = f"{str(mmr)}/1400"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1400 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1600:
                    mmre = f"{str(mmr)}/1600"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1600 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 1800:
                    mmre = f"{str(mmr)}/1800"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 1800 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 2000:
                    mmre = f"{str(mmr)}/2000"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 2000 and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] < 2500:
                    mmre = f"{str(mmr)}/2500"
                    idraw.text((646, 299), mmre, font = mmrer, fill = "white")
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['mmr'] >= 2500:
                    mmre = f"{str(mmr)}"
                    idraw.text((600, 199), mmre, font = mmrer, fill = "white")
	
                avatar = member.avatar_url_as(size = 128)
                avt = BytesIO(await avatar.read())
                imga = Image.open(avt)
                imguser = imga.resize((250, 250))
	
                lvle = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit']
                lvlfaceit = Image.open(f"facei{lvle}.png")
                imgty = lvlfaceit.resize((68, 50))
                idraw = ImageDraw.Draw(imgty)
		
                leaguer = Image.open("default.png")
                league = leaguer.resize((102, 113))
                idraw = ImageDraw.Draw(league)
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['verif'] == 1:
                    verify = Image.open("verify.png")
                    verifyr = verify.resize((248, 50))
                    idraw = ImageDraw.Draw(verifyr)
                    img.paste(verifyr, (527, 40), verifyr)
                else:
                    pass

                img.paste(imguser, (100, 100))
                img.paste(imgty, (375, 271), imgty)
                img.paste(league, (856, 261), league)
                img.save("profilet.png")
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['pro_league'] == 0:
                    cyber_stats = "Недоступно"
                    cyber_offliner = f"{offline}"
                else:
                    cyber_stats = "Доступно"
                    cyber_offliner = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['qualification'] == 0:
                    cyber_qual = "Недоступно"
                    cyber_offliner_qual = f"{offline}"
                else:
                    cyber_qual = "Доступно"
                    cyber_offliner_qual = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 1:
                    color = 0x00FF00
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 2:
                    color = 0x00FFFF
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 3:
                    color = 0x000080
	
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 4:
                    color = 0xDC143C
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 5:
                    color = 0xc301ff
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 6:
                    color = 0xFFFF00
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 7:
                    color = 0xEE82EE
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 8:
                    color = 0xFFD700
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 9:
                    color = 0x00aa36
		
                elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['lvlfaceit'] == 10:
                    color = 0xFF0000
	
                file = discord.File("profilet.png")
                e = discord.Embed(
                    description = f"**DEFAULT LEAGUE** {online} _Активно_\n**QUALIFICATIONS LEAGUE** {cyber_offliner_qual} _{cyber_qual}_\n**CYBER PRO LEAGUE** {cyber_offliner} _{cyber_stats}_",
                    colour=color
                )
                e.set_image(url = 'attachment://profilet.png')
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(f"||{self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['idgame']}||", file=file, embed=e)
        if league == 'qual':
            if self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['afraid_qual'] <= 0:
                e = discord.Embed(
                    description = "Лига QUALIFICATIONS недоступна для данного пользователя! Лигу можно преобрести написав fudge(feat PetuSHOK)#6666 или Afraid Faceit(Corjusper)#3486",
                    colour=0x00FF00
                )
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            else:
                namegame = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['name']
                image = Image.open("profile.png")
                img = image.resize((1461, 573))
                idraw = ImageDraw.Draw(img)
                membere = ImageFont.truetype('Roboto.ttf', size = 25)
                stats = ImageFont.truetype('Roboto.ttf', size = 75)
                stat = ImageFont.truetype('Roboto.ttf', size = 50)
                statswn = ImageFont.truetype('Roboto.ttf', size = 40)
                winratere = ImageFont.truetype('Roboto.ttf', size = 17)
                mmrer = ImageFont.truetype('Roboto.ttf', size = 42)
                kder = ImageFont.truetype('Roboto.ttf', size = 60)
                mgs = f'{namegame}'	
                idraw.text((274, 93), mgs, font = membere, fill = "white")
	
                killes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'])
                idraw.text((1133, 94), killes, font = statswn, fill = "white")
                deathes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths'])
                idraw.text((1133, 147), deathes, font = statswn, fill = "white")
                kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                if kd == 0:
                    kd = str(0)
                    idraw.text((848, 104), kd, font = stats, fill = "white")
                else:
                    kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills']/self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                    x = str(float('{:.2f}'.format(kd)))
                    idraw.text((822, 120), x, font = stat, fill = "white")

                wins = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'])
                idraw.text((1133, 368), wins, font = statswn, fill = "white")
                loses = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses'])
                idraw.text((1133, 421), loses, font = statswn, fill = "white")
	
                winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                if winrate == 0:
                    winrate = f"{str(0)}%"
                    idraw.text((832, 381), winrate, font = stats, fill = "white")
                else:
                    winrater = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] + self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                    winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins']/winrater*100
                    x = f"{str(float('{:.1f}'.format(winrate)))}%"
                    idraw.text((812, 391), x, font = stat, fill = "white")
		
                qual = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['qual']
		
                mmre = f"{str(qual)}"
                idraw.text((600, 199), mmre, font = mmrer, fill = "white")
	
                avatar = member.avatar_url_as(size = 128)
                avt = BytesIO(await avatar.read())
                imga = Image.open(avt)
                imguser = imga.resize((188, 188))
	
                qualfaceit = Image.open(f"qual.jpg")
                imgty = qualfaceit.resize((75, 75))
                idraw = ImageDraw.Draw(imgty)

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] == 1:
                    premium = Image.open("premium.png")
                    imgt = premium.resize((100, 100))
                    idraw = ImageDraw.Draw(imgt)
                    img.paste(imgt, (60, 304), imgt)
                else:
                    pass

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] == 1:
                    tester = Image.open("tester.png")
                    imgq = tester.resize((100, 100))
                    idraw = ImageDraw.Draw(imgq)
                    img.paste(imgq, (180, 304), imgq)
                else:
                    pass

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] == 1:
                    developer = Image.open("developer.png")
                    imge = developer.resize((100, 100))
                    idraw = ImageDraw.Draw(imge)
                    img.paste(imge, (300, 304), imge)
                else:
                    pass

                img.paste(imguser, (55, 57))
                img.paste(imgty, (265, 165))
                img.save("profilet.png")
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] == 0:
                    afraid_stats = "Недоступно"
                    afraid_offliner = f"{offline}"
                else:
                    afraid_stats = "Доступно"
                    afraid_offliner = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] == 0:
                    afraid_qual = "Недоступно"
                    afraid_offliner_qual = f"{offline}"
                else:
                    afraid_qual = "Доступно"
                    afraid_offliner_qual = f"{online}"
	
                file = discord.File("profilet.png")
                e = discord.Embed(
                    description = f"**DEFAULT LEAGUE** {online} _Активно_\n**QUALIFICATIONS LEAGUE** {afraid_offliner_qual} _{afraid_qual}_\n**AFRAID PRO LEAGUE** {afraid_offliner} _{afraid_stats}_",
                    colour=0xFF0000
                )
                e.set_image(url = 'attachment://profilet.png')
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(f"||{self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['idgame']}||", file=file, embed=e)
        if league == 'pro':
            if self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['afraid_qual'] <= 0:
                e = discord.Embed(
                    description = "Лига PRO LEAGUE недоступна для данного пользователя! Лигу можно преобрести написав fudge(feat PetuSHOK)#6666 или Afraid Faceit(Corjusper)#3486",
                    colour=0x00FF00
                )
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            else:
                namegame = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['name']
                image = Image.open("profile.png")
                img = image.resize((1461, 573))
                idraw = ImageDraw.Draw(img)
                membere = ImageFont.truetype('Roboto.ttf', size = 25)
                stats = ImageFont.truetype('Roboto.ttf', size = 75)
                stat = ImageFont.truetype('Roboto.ttf', size = 50)
                statswn = ImageFont.truetype('Roboto.ttf', size = 40)
                winratere = ImageFont.truetype('Roboto.ttf', size = 17)
                mmrer = ImageFont.truetype('Roboto.ttf', size = 42)
                kder = ImageFont.truetype('Roboto.ttf', size = 60)
                mgs = f'{namegame}'	
                idraw.text((274, 93), mgs, font = membere, fill = "white")
	
                killes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'])
                idraw.text((1133, 94), killes, font = statswn, fill = "white")
                deathes = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths'])
                idraw.text((1133, 147), deathes, font = statswn, fill = "white")
                kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                if kd == 0:
                    kd = str(0)
                    idraw.text((848, 104), kd, font = stats, fill = "white")
                else:
                    kd = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['kills']/self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['deaths']
                    x = str(float('{:.2f}'.format(kd)))
                    idraw.text((822, 120), x, font = stat, fill = "white")

                wins = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'])
                idraw.text((1133, 368), wins, font = statswn, fill = "white")
                loses = str(self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses'])
                idraw.text((1133, 421), loses, font = statswn, fill = "white")
	
                winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] and self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                if winrate == 0:
                    winrate = f"{str(0)}%"
                    idraw.text((832, 381), winrate, font = stats, fill = "white")
                else:
                    winrater = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins'] + self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['loses']
                    winrate = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['wins']/winrater*100
                    x = f"{str(float('{:.1f}'.format(winrate)))}%"
                    idraw.text((812, 391), x, font = stat, fill = "white")
		
                pro = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['pro']
		
                mmre = f"{str(pro)}"
                idraw.text((600, 199), mmre, font = mmrer, fill = "white")
	
                avatar = member.avatar_url_as(size = 128)
                avt = BytesIO(await avatar.read())
                imga = Image.open(avt)
                imguser = imga.resize((188, 188))
	
                qualfaceit = Image.open(f"proleague.jpg")
                imgty = qualfaceit.resize((75, 75))
                idraw = ImageDraw.Draw(imgty)

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] == 1:
                    premium = Image.open("premium.png")
                    imgt = premium.resize((100, 100))
                    idraw = ImageDraw.Draw(imgt)
                    img.paste(imgt, (60, 304), imgt)
                else:
                    pass

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] == 1:
                    tester = Image.open("tester.png")
                    imgq = tester.resize((100, 100))
                    idraw = ImageDraw.Draw(imgq)
                    img.paste(imgq, (180, 304), imgq)
                else:
                    pass

                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] == 1:
                    developer = Image.open("developer.png")
                    imge = developer.resize((100, 100))
                    idraw = ImageDraw.Draw(imge)
                    img.paste(imge, (300, 304), imge)
                else:
                    pass

                img.paste(imguser, (55, 57))
                img.paste(imgty, (265, 165))
                img.save("profilet.png")
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] == 0:
                    afraid_stats = "Недоступно"
                    afraid_offliner = f"{offline}"
                else:
                    afraid_stats = "Доступно"
                    afraid_offliner = f"{online}"
		
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] == 0:
                    afraid_qual = "Недоступно"
                    afraid_offliner_qual = f"{offline}"
                else:
                    afraid_qual = "Доступно"
                    afraid_offliner_qual = f"{online}"
	
                file = discord.File("profilet.png")
                e = discord.Embed(
                    description = f"**DEFAULT LEAGUE** {online} _Активно_\n**QUALIFICATIONS LEAGUE** {afraid_offliner_qual} _{afraid_qual}_\n**AFRAID PRO LEAGUE** {afraid_offliner} _{afraid_stats}_",
                    colour=0xFF0000
                )
                e.set_image(url = 'attachment://profilet.png')
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(f"||{self.collection.find_one({'guild_id': ctx.guild.id, 'user_id': member.id})['idgame']}||", file=file, embed=e)
	
    @cog_ext.cog_slash(name="additem", description="Выдать значок", options = [{"name": "member", "description": "Пользователь которому желаете добавить значок:", "required": True, "type": 6},{"name": "item", "description": "Значок:", "required": True, "type": 3},{"name": "action", "description": "Добавить или забрать: add and take:", "required": True, "type": 3}])
    @commands.has_permissions(administrator=True)
    async def additem(self, ctx, member: discord.Member, item: str, action: str):
        if item == 'Премиум':
            if action == 'add':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] == 1:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже есть премиум!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_premium": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно выдали премиум!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
            if action == 'take':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] == 0:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже отсутсвует премиум!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_premium'] - 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_premium": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно забрали премиум!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
        elif item == 'Тестер':
            if action == 'add':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] == 1:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже есть тестре!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_tester": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно выдали тестера!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
            if action == 'take':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] == 0:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже отсутсвует тестер!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_tester'] - 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_tester": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно забрали тестера!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
        elif item == 'Создатель':
            if action == 'add':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] == 1:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже есть создатель!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_developer": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно выдали создателя!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
            if action == 'take':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] == 0:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже отсутсвует создатель!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_developer'] - 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_developer": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно забрали создателя!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
        elif item == 'Pro League':
            if action == 'add':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] == 1:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже есть Pro League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    role = discord.utils.get(member.guild.roles, id=1013840470255869982)
                    await member.add_roles(role)
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_pro_league": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно выдали Pro League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
            if action == 'take':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] == 0:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже отсутсвует Pro League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    role = discord.utils.get(member.guild.roles, id=1013840470255869982)
                    await member.remove_roles(role)
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_pro_league'] - 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_pro_league": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно забрали Pro League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
        elif item == 'Qual League':
            if action == 'add':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] == 1:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже есть Qualifications League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    role = discord.utils.get(member.guild.roles, id=1013840524463046746)
                    await member.add_roles(role)
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] + 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_qual": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно выдали Qualifications League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
            if action == 'take':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] == 0:
                    e = discord.Embed(
                        title = "Ошибка",
                        description = "У пользователя уже отсутсвует Qualifications League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
                else:
                    role = discord.utils.get(member.guild.roles, id=1013840524463046746)
                    await member.remove_roles(role)
                    r = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": member.id})['afraid_qual'] - 1
                    self.collection.update_one({'guild_id': ctx.guild.id, "user_id": member.id}, {"$set": {"afraid_qual": r}})
                    e = discord.Embed(
                        title = "Успешно",
                        description = "Вы успешно забрали Qualifications League!",
                        colour=0x00FF00
                    )
                    e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=e)
		
    @commands.command(aliase = ['setgame'])
    @commands.has_permissions(administrator=True)
    async def game(self, ctx, codegame: int = None, pickedmap: str = None, win: int = None, loses: int = None, memberwin: discord.Member = None, memberwinkill: int = None, memberdie: int = None, memberwintwo: discord.Member = None, memberwinkilltwo: int = None, memberwindietwo: int = None, memberloses: discord.Member = None, memberloseskill: int = None, memberlosesdie: int = None, memberlosestwo: discord.Member = None, memberloseskilltwo: int = None, memberlosesdietwo: int = None):
        if codegame is None:
            e = discord.Embed(
                title = f"Укажите код игры выданный ботом!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif not self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame}):
            e = discord.Embed(
                title = f"Игры с таким кодом несуществует!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] == 1:
            e = discord.Embed(
                title = f"Игра с таким кодом уже зарегистрированна!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif pickedmap is None:
            e = discord.Embed(
                title = f"Укажите карту выбранную ботом!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif win is None:
            e = discord.Embed(
                title = f"Укажите счёт победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif loses is None:
            e = discord.Embed(
                title = f"Укажите счёт проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberwin is None:
            e = discord.Embed(
                title = f"Укажите первого участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberwinkill is None:
            e = discord.Embed(
                title = f"Укажите кол-во килов первого участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberdie is None:
            e = discord.Embed(
                title = f"Укажите кол-во смертей первого участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberwintwo is None:
            e = discord.Embed(
                title = f"Укажите второго участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberwinkilltwo is None:
            e = discord.Embed(
                title = f"Укажите кол-во килов второго участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberwindietwo is None:
            e = discord.Embed(
                title = f"Укажите кол-во смертей второго участника из команды победителей!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberloses is None:
            e = discord.Embed(
                title = f"Укажите первого участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberloseskill is None:
            e = discord.Embed(
                title = f"Укажите кол-во килов первого участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberlosesdie is None:
            e = discord.Embed(
                title = f"Укажите кол-во смертей первого участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberlosestwo is None:
            e = discord.Embed(
                title = f"Укажите второго участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberloseskilltwo is None:
            e = discord.Embed(
                title = f"Укажите кол-во килов второго участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        elif memberlosesdietwo is None:
            e = discord.Embed(
                title = f"Укажите кол-во смертей второго участника из команды проигравших!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        else:
            if pickedmap == 'SandStone':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                onekill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['kills'] + memberwinkill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'kills': onekill}})
                regone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1kill'] + memberwinkill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1kill': regone}})
                onedie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['deaths'] + memberdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'deaths': onedie}})
                regoner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1die'] + memberdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1die': regoner}})
                onewin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'wins': onewin}})
	
                twokill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['kills'] + memberwinkilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'kills': twokill}})
                regtwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2kill'] + memberwinkilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2kill': regtwo}})
                twodie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['deaths'] + memberwindietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'deaths': twodie}})
                regtwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2die'] + memberwindietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2die': regtwor}})
                twowin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'wins': twowin}})
	
	
                onekilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['kills'] + memberloseskill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'kills': onekilloses}})
                reglone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3kill'] + memberloseskill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3kill': reglone}})
                onediloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['deaths'] + memberlosesdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'deaths': onediloses}})
                regloner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3die'] + memberlosesdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3die': regloner}})
                oneloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'loses': oneloses}})
	 
                twokilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['kills'] + memberloseskilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'kills': twokilloses}})
                regltwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4kill'] + memberloseskilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4kill': regltwo}})
                twodiloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['deaths'] + memberlosesdietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'deaths': twodiloses}})
                regltwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4die'] + memberlosesdietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4die': regltwor}})
                twoloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'loses': twoloses}})
		
                regame = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] + 1
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'reg': regame}})
		
		
                e = discord.Embed(
                    title = f"GAME #{codegame}  |  MAP: {pickedmap}",
                    colour=0x00FF00
                )
                e.add_field(name = f"WIN COMMAND: {win}", value = f"{memberwin.mention}: kill: **{memberwinkill}** die: **{memberdie}**\n{memberwintwo.mention}: kill: **{memberwinkilltwo}** die: **{memberwindietwo}**", inline = False)
                e.add_field(name = f"LOSES COMMAND: {loses}", value = f"{memberloses.mention}: kill: **{memberloseskill}** die: **{memberlosesdie}**\n{memberlosestwo.mention}: kill: **{memberloseskilltwo}** die: **{memberlosesdietwo}**", inline = False)
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            elif pickedmap == 'Province':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                onekill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['kills'] + memberwinkill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'kills': onekill}})
                regone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1kill'] + memberwinkill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1kill': regone}})
                onedie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['deaths'] + memberdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'deaths': onedie}})
                regoner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1die'] + memberdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1die': regoner}})
                onewin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'wins': onewin}})
	
                twokill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['kills'] + memberwinkilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'kills': twokill}})
                regtwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2kill'] + memberwinkilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2kill': regtwo}})
                twodie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['deaths'] + memberwindietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'deaths': twodie}})
                regtwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2die'] + memberwindietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2die': regtwor}})
                twowin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'wins': twowin}})
	
	
                onekilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['kills'] + memberloseskill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'kills': onekilloses}})
                reglone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3kill'] + memberloseskill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3kill': reglone}})
                onediloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['deaths'] + memberlosesdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'deaths': onediloses}})
                regloner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3die'] + memberlosesdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3die': regloner}})
                oneloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'loses': oneloses}})
	 
                twokilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['kills'] + memberloseskilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'kills': twokilloses}})
                regltwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4kill'] + memberloseskilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4kill': regltwo}})
                twodiloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['deaths'] + memberlosesdietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'deaths': twodiloses}})
                regltwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4die'] + memberlosesdietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4die': regltwor}})
                twoloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'loses': twoloses}})
		
                regame = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] + 1
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'reg': regame}})
		
		
                e = discord.Embed(
                    title = f"GAME #{codegame}  |  MAP: {pickedmap}",
                    colour=0x00FF00
                )
                e.add_field(name = f"WIN COMMAND: {win}", value = f"{memberwin.mention}: kill: **{memberwinkill}** die: **{memberdie}**\n{memberwintwo.mention}: kill: **{memberwinkilltwo}** die: **{memberwindietwo}**", inline = False)
                e.add_field(name = f"LOSES COMMAND: {loses}", value = f"{memberloses.mention}: kill: **{memberloseskill}** die: **{memberlosesdie}**\n{memberlosestwo.mention}: kill: **{memberloseskilltwo}** die: **{memberlosesdietwo}**", inline = False)
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            elif pickedmap == 'Rust':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                onekill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['kills'] + memberwinkill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'kills': onekill}})
                regone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1kill'] + memberwinkill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1kill': regone}})
                onedie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['deaths'] + memberdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'deaths': onedie}})
                regoner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1die'] + memberdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1die': regoner}})
                onewin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'wins': onewin}})
	
                twokill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['kills'] + memberwinkilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'kills': twokill}})
                regtwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2kill'] + memberwinkilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2kill': regtwo}})
                twodie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['deaths'] + memberwindietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'deaths': twodie}})
                regtwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2die'] + memberwindietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2die': regtwor}})
                twowin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'wins': twowin}})
	
	
                onekilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['kills'] + memberloseskill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'kills': onekilloses}})
                reglone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3kill'] + memberloseskill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3kill': reglone}})
                onediloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['deaths'] + memberlosesdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'deaths': onediloses}})
                regloner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3die'] + memberlosesdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3die': regloner}})
                oneloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'loses': oneloses}})
	 
                twokilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['kills'] + memberloseskilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'kills': twokilloses}})
                regltwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4kill'] + memberloseskilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4kill': regltwo}})
                twodiloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['deaths'] + memberlosesdietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'deaths': twodiloses}})
                regltwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4die'] + memberlosesdietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4die': regltwor}})
                twoloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'loses': twoloses}})
		
                regame = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] + 1
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'reg': regame}})
		
		
                e = discord.Embed(
                    title = f"GAME #{codegame}  |  MAP: {pickedmap}",
                    colour=0x00FF00
                )
                e.add_field(name = f"WIN COMMAND: {win}", value = f"{memberwin.mention}: kill: **{memberwinkill}** die: **{memberdie}**\n{memberwintwo.mention}: kill: **{memberwinkilltwo}** die: **{memberwindietwo}**", inline = False)
                e.add_field(name = f"LOSES COMMAND: {loses}", value = f"{memberloses.mention}: kill: **{memberloseskill}** die: **{memberlosesdie}**\n{memberlosestwo.mention}: kill: **{memberloseskilltwo}** die: **{memberlosesdietwo}**", inline = False)
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            elif pickedmap == 'Sakura':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                onekill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['kills'] + memberwinkill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'kills': onekill}})
                regone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1kill'] + memberwinkill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1kill': regone}})
                onedie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['deaths'] + memberdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'deaths': onedie}})
                regoner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1die'] + memberdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1die': regoner}})
                onewin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'wins': onewin}})
	
                twokill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['kills'] + memberwinkilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'kills': twokill}})
                regtwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2kill'] + memberwinkilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2kill': regtwo}})
                twodie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['deaths'] + memberwindietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'deaths': twodie}})
                regtwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2die'] + memberwindietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2die': regtwor}})
                twowin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'wins': twowin}})
	
	
                onekilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['kills'] + memberloseskill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'kills': onekilloses}})
                reglone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3kill'] + memberloseskill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3kill': reglone}})
                onediloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['deaths'] + memberlosesdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'deaths': onediloses}})
                regloner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3die'] + memberlosesdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3die': regloner}})
                oneloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'loses': oneloses}})
	 
                twokilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['kills'] + memberloseskilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'kills': twokilloses}})
                regltwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4kill'] + memberloseskilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4kill': regltwo}})
                twodiloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['deaths'] + memberlosesdietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'deaths': twodiloses}})
                regltwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4die'] + memberlosesdietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4die': regltwor}})
                twoloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'loses': twoloses}})
		
                regame = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] + 1
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'reg': regame}})
		
		
                e = discord.Embed(
                    title = f"GAME #{codegame}  |  MAP: {pickedmap}",
                    colour=0x00FF00
                )
                e.add_field(name = f"WIN COMMAND: {win}", value = f"{memberwin.mention}: kill: **{memberwinkill}** die: **{memberdie}**\n{memberwintwo.mention}: kill: **{memberwinkilltwo}** die: **{memberwindietwo}**", inline = False)
                e.add_field(name = f"LOSES COMMAND: {loses}", value = f"{memberloses.mention}: kill: **{memberloseskill}** die: **{memberlosesdie}**\n{memberlosestwo.mention}: kill: **{memberloseskilltwo}** die: **{memberlosesdietwo}**", inline = False)
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
            elif pickedmap == 'Zone':
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 1:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 35
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 20
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 15
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['mmr'] + 10
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 1:
                    if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['mmr'] < 50:
                        pass
                    else:
                        addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 20
                        self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 2:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 3:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 4:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 5:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 6:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 7:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 8:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 9:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 25
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
                if self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['lvlfaceit'] == 10:
                    addmmr = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['mmr'] - 30
                    self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'mmr': addmmr}})
                else:
                    pass
	
	
                onekill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['kills'] + memberwinkill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'kills': onekill}})
                regone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1kill'] + memberwinkill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1kill': regone}})
                onedie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['deaths'] + memberdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'deaths': onedie}})
                regoner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value1die'] + memberdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value1die': regoner}})
                onewin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwin.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwin.id}, {'$set':{'wins': onewin}})
	
                twokill = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['kills'] + memberwinkilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'kills': twokill}})
                regtwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2kill'] + memberwinkilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2kill': regtwo}})
                twodie = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['deaths'] + memberwindietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'deaths': twodie}})
                regtwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value2die'] + memberwindietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value2die': regtwor}})
                twowin = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberwintwo.id})['wins'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberwintwo.id}, {'$set':{'wins': twowin}})
	
	
                onekilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['kills'] + memberloseskill
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'kills': onekilloses}})
                reglone = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3kill'] + memberloseskill
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3kill': reglone}})
                onediloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['deaths'] + memberlosesdie
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'deaths': onediloses}})
                regloner = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value3die'] + memberlosesdie
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value3die': regloner}})
                oneloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberloses.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberloses.id}, {'$set':{'loses': oneloses}})
	 
                twokilloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['kills'] + memberloseskilltwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'kills': twokilloses}})
                regltwo = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4kill'] + memberloseskilltwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4kill': regltwo}})
                twodiloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['deaths'] + memberlosesdietwo
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'deaths': twodiloses}})
                regltwor = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['value4die'] + memberlosesdietwo
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'value4die': regltwor}})
                twoloses = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": memberlosestwo.id})['loses'] + 1
                self.collection.update_one({'guild_id': ctx.guild.id, 'user_id': memberlosestwo.id}, {'$set':{'loses': twoloses}})
		
                regame = self.collgame.find_one({"guild_id": ctx.guild.id, "codegame": codegame})['reg'] + 1
                self.collgame.update_one({'guild_id': ctx.guild.id, "codegame": codegame}, {'$set':{'reg': regame}})
		
		
                e = discord.Embed(
                    title = f"GAME #{codegame}  |  MAP: {pickedmap}",
                    colour=0x00FF00
                )
                e.add_field(name = f"WIN COMMAND: {win}", value = f"{memberwin.mention}: kill: **{memberwinkill}** die: **{memberdie}**\n{memberwintwo.mention}: kill: **{memberwinkilltwo}** die: **{memberwindietwo}**", inline = False)
                e.add_field(name = f"LOSES COMMAND: {loses}", value = f"{memberloses.mention}: kill: **{memberloseskill}** die: **{memberlosesdie}**\n{memberlosestwo.mention}: kill: **{memberloseskilltwo}** die: **{memberlosesdietwo}**", inline = False)
                e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=e)
	
    @cog_ext.cog_slash(name="rename", description="Изменяет ваш никнейм на сервере", options = [create_option(name="name", description="Изменяет ваш никнейм на сервере", required=True, option_type=3)])
    async def rename(self, ctx, *, name: str):
        if name is None:
            e = discord.Embed(
                description = f"Укажите новый ник",
                colour=0x00FF00
            )
            e.set_footer(text=f'SLR Rating | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
        else:
            member=ctx.author
            r = self.collection.update_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id}, {"$set": {"name": name}})
            namer = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id})['name']
            await member.edit(nick=name)
            e = discord.Embed(
                description = f"Вы успешно сменили ник!\nНовый ник: `{name}`",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
	
    @cog_ext.cog_slash(name="reidgame", description="Изменяет ваш ID на сервере", options = [create_option(name="idgame", description="Изменяет ваш ID на сервере", required=True, option_type=4)])
    async def reidgame(self, ctx, idgame: int):
        if idgame < 10000000:
            e = discord.Embed(
                  title=f'Ошибка:',
                  description=f'ID не должно быть меньше 10000000',
                  color=discord.Color.red()
	    )
            await ctx.send(embed=e)
        elif idgame > 20000000:
            e = discord.Embed(
                  title=f'Ошибка:',
                  description=f'ID не должно быть больше 20000000',
                  color=discord.Color.red()
	    )
            await ctx.send(embed=e)
        else:
            r = self.collection.update_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id}, {"$set": {"idgame": idgame}})
            namer = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id})['idgame']
            e = discord.Embed(
                description = f"Вы успешно сменили ID!\nНовый ID: `{namer}`",
                colour=0x00FF00
            )
            e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=e)
	
    @cog_ext.cog_slash(name="ranks", description="Все доступные ранги")
    async def ranks(self, ctx):
        lvl10 = discord.utils.get(self.client.emojis, name='10lvl')
        lvl9 = discord.utils.get(self.client.emojis, name='9lvl')
        lvl8 = discord.utils.get(self.client.emojis, name='8lvl')
        lvl7 = discord.utils.get(self.client.emojis, name='7lvl')
        lvl6 = discord.utils.get(self.client.emojis, name='6lvl')
        lvl5 = discord.utils.get(self.client.emojis, name='5lvl')
        lvl4 = discord.utils.get(self.client.emojis, name='4lvl')
        lvl3 = discord.utils.get(self.client.emojis, name='3lvl')
        lvl2 = discord.utils.get(self.client.emojis, name='2lvl')
        lvl1 = discord.utils.get(self.client.emojis, name='1lvl')
        e = discord.Embed(
            title = "Ranks of Afraid Faceit",
            colour=0x00FF00
        )
        e.add_field(name = f"\u200b  {lvl10}  \u200b`2500`  +10 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl9}  \u200b`2000`  +15 / -30", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl8}  \u200b`1800`  +15 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl7}  \u200b`1600`  +20 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl6}  \u200b`1400`  +25 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl5}  \u200b`1100`  +25 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl4}  \u200b`900`  +30 / -30", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl3}  \u200b`600`  +35 / -30", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl2}  \u200b`300`  +35 / -25", value = "\u200b", inline = False)
        e.add_field(name = f"\u200b  {lvl1}  \u200b`50`  +35 / -20", value = "\u200b", inline = False)
        e.set_footer(text=f'Afraid Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=e)
	
    @cog_ext.cog_slash(name="topmmr", description="Топ ммр сервера")
    async def topmmr(self, ctx):
        iters = 10
        rankings = self.collection.find({"guild_id": ctx.guild.id}, limit=iters).sort("mmr", -1)
        lvl10 = discord.utils.get(self.client.emojis, name='10lvl')
        lvl9 = discord.utils.get(self.client.emojis, name='9lvl')
        lvl8 = discord.utils.get(self.client.emojis, name='8lvl')
        lvl7 = discord.utils.get(self.client.emojis, name='7lvl')
        lvl6 = discord.utils.get(self.client.emojis, name='6lvl')
        lvl5 = discord.utils.get(self.client.emojis, name='5lvl')
        lvl4 = discord.utils.get(self.client.emojis, name='4lvl')
        lvl3 = discord.utils.get(self.client.emojis, name='3lvl')
        lvl2 = discord.utils.get(self.client.emojis, name='2lvl')
        lvl1 = discord.utils.get(self.client.emojis, name='1lvl')
	
        place1 = discord.utils.get(self.client.emojis, name='1place')
        place2 = discord.utils.get(self.client.emojis, name='2place')
        place3 = discord.utils.get(self.client.emojis, name='3place')

        i = 1

        embed = discord.Embed(
            title=f"{ctx.guild.name}'s Leaderboard", color=0x00FF00
            )

        for x in rankings:
            try:
                temp = (x["name"])
                tb = x["mmr"]
                lvl = x["lvlfaceit"]
		
                if i == 1:
                    one = f"{place1}"
                elif i == 2:
                    one = f"{place2}"
                elif i == 3:
                    one = f"{place3}"
                else:
                    pass
		
                if lvl == 1:
                    embed.add_field(
                        name=f"{lvl1}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 2:
                    embed.add_field(
                        name=f"{lvl2}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 3:
                    embed.add_field(
                        name=f"{lvl3}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 4:
                    embed.add_field(
                        name=f"{lvl4}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 5:
                    embed.add_field(
                        name=f"{lvl5}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 6:
                    embed.add_field(
                        name=f"{lvl6}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 7:
                    embed.add_field(
                        name=f"{lvl7}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 8:
                    embed.add_field(
                        name=f"{lvl8}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 9:
                    embed.add_field(
                        name=f"{lvl9}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                if lvl == 10:
                    embed.add_field(
                        name=f"{lvl10}  {temp}  {tb} {one}", value="\u200b", inline=False
                    )
                i += 1
            except:
                pass
            if i == 11:
                break

        embed.set_footer(
            text="Cyber Faceit | Standoff 2", icon_url=self.client.user.avatar_url
        )
        await ctx.send(embed=embed)
	
    @cog_ext.cog_slash(name="topqual", description="Топ QUAL сервера")
    async def topqual(self, ctx):
        qual = discord.utils.get(self.client.emojis, name='qual')
        iters = 10
        rankings = self.collection.find({"guild_id": ctx.guild.id}, limit=iters).sort("qual", -1)

        i = 1

        embed = discord.Embed(
            title=f"QUALIFICATIONS LEAGUE", color=0x00FF00
            )

        for x in rankings:
            try:
                temp = (x["name"])
                tb = x["qual"]
                qualleg = x["qualification"]
                if qualleg == 1:
                    embed.add_field(
                        name=f"{qual}   {temp}    {tb}", value=f"\u200b", inline=False
                    )
                else:
                    pass
	
                i += 1
            except:
                pass
            if i == 11:
                break

        embed.set_footer(
            text="Cyber Faceit | Standoff 2", icon_url=self.client.user.avatar_url
        )
        await ctx.send(embed=embed)
	
    @cog_ext.cog_slash(name="toppro", description="Топ PRO сервера")
    async def toppro(self, ctx):
        pro = discord.utils.get(self.client.emojis, name='pro')
        iters = 10
        rankings = self.collection.find({"guild_id": ctx.guild.id}, limit=iters).sort("pro", -1)

        i = 1

        embed = discord.Embed(
            title=f"PRO LEAGUE", color=0x00FF00
            )

        for x in rankings:
            try:
                temp = (x["name"])
                tb = x["pro"]
                proleg = x["pro_league"]
                if proleg == 1:
                    embed.add_field(
                        name=f"{pro}   {temp}    {tb}", value=f"\u200b", inline = False
                    )
                else:
                    pass

                i += 1
            except:
                pass
            if i == 11:
                break

        embed.set_footer(
            text="Cyber Faceit | Standoff 2", icon_url=self.client.user.avatar_url
        )
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="registration", description="Устанавливает ваш игровой ID", options = [create_option(name="idgame", description="Устанавливает ваш игровой ID", required=True, option_type=4)])
    async def registration(self, ctx, idgame: int = None):
        tru = discord.utils.get(self.client.emojis, name='yes')
        err = discord.utils.get(self.client.emojis, name='no')
        if idgame < 10000000:
            e = discord.Embed(
                  title=f'{err} Ошибка:',
                  description=f'ID не должно быть меньше 10000000',
                  color=discord.Color.red()
	    )
            await ctx.send(embed=e)
        elif idgame > 200000000:
            e = discord.Embed(
                  title=f'{err} Ошибка:',
                  description=f'ID не должно быть больше 20000000',
                  color=discord.Color.red()
	    )
            await ctx.send(embed=e)
        elif not self.collection.count_documents({"guild_id": ctx.guild.id, "user_id": ctx.author.id}):
            post = {
                "user_id": ctx.author.id,
                "guild_id": ctx.guild.id,
		"name": ctx.author.name,
		"idgame": 0,
		"lvlfaceit": 1,
		"mmr": 50,
		"qual": 0,
		"pro": 0,
		"wins": 0,
		"loses": 0,
		"kills": 0,
		"deaths": 0,
		"blacklist": 0,
		"pro_league": 0,
		"premium": 0,
		"qualification": 0,
		"verif": 0,
		"calibration": 0
            }

            self.collection.insert_one(post)
        elif self.collection.find_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id})['idgame'] > 0:
            e = discord.Embed(
                  title=f'{err} Ошибка:',
                  description=f'ID вы уже зарегестрированы!',
                  color=discord.Color.red()
	    )
            await ctx.send(embed=e)
        else:
            r = self.collection.update_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id}, {"$set": {"idgame": idgame}})
            idgame = self.collection.find_one({'guild_id': ctx.guild.id, "user_id": ctx.author.id})['idgame']
            role = discord.utils.get(ctx.author.guild.roles, id=1028655711187640400)
            await ctx.author.add_roles(role)
            roles = discord.utils.get(ctx.author.guild.roles, id=1028656096946176102)
            await ctx.author.add_roles(roles)
            e = discord.Embed(
                title = "Успешно",
                description = "Вы успешно зарегистрировались!",
                colour=0x00FF00
            )
            e.set_footer(text=f'Cyber Faceit | Standoff 2', icon_url=self.client.user.avatar_url)
            await ctx.send(f"||{idgame}||", embed=e)
            
        
def setup(client):
    client.add_cog(Faceit(client))
