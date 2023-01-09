import discord
from discord.ext import commands
from pymongo import MongoClient


class RegModal(discord.ui.Modal, title = "Регистрация аккаунта на фейсите!"):
    name = discord.ui.TextInput(label = "Имя в игре:", min_length = 2, max_length = 15)
    age = discord.ui.TextInput(label = "id в игре:", min_length = 8, max_length = 20)
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        cluster = MongoClient("mongodb+srv://Setroom:CFLrxCSX0fzBIMlA@cluster0.l9fw9.mongodb.net/ecodb?retryWrites=true&w=majority")
        colluser = cluster.faceit.user
        guild = interaction.guild
        user = interaction.user
        await interaction.response.send_message("Вы зарегистрированны!", ephemeral = True)
        
class Buttons(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label = "Регистрация", style = discord.ButtonStyle.green)
    async def click(self, interaction: discord.Interaction, child: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        await interaction.response.send_modal(RegModal())
        await interaction.response.send_message("Зарегистрируйтесь!", ephemeral = True)
            
#class ModalView(discord.ui.View):
    #def __init__(self, *, timeout = 180):
        #super().__init__(timeout=timeout)
        #self.add_item(())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def регистрация(self, ctx):
        embed = discord.Embed(title = "Регистрация аккаунта!", description = "Чтобы зарегистрироваться нужно нажать на кнопку ниже и заполнить анкету по примеру ниже!")
        await ctx.send(embed = embed, view = Buttons())
      
async def setup(client):
    await client.add_cog(Modal(client))
