import discord
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
        self.collection = self.cluster.afraid.afraiduser
        self.collgame = self.cluster.afraid.afraidgame
	
	
    @commands.Cog.listener()
    async def on_ready(self):
        print("Faceit cog loaded.")

    @commands.command()
    async def facts(self, ctx, number):
        response = requests.get(f"http://numbersapi.com/{number}")
        embed = discord.Embed(title = "Information Number", description = response.text)
        await ctx.channel.send(embed = embed)
            
        
async def setup(client):
    await client.add_cog(Faceit(client))
