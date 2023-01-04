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
	
    #@commands.Cog.listener()
    #async def on_ready(self):
        #print("Faceit cog loaded.")

    @commands.command(name = "number", description = "Факт о числе")
    async def number(self, interaction: discord.Interaction, number: int):
       await interaction.response.send_message(number)
        
async def setup(client):
    await client.add_cog(Faceit(client))
