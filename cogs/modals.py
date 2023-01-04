import discord
from discord.ext import commands

class SurveyModal(discord.ui.Modal, title = "Заявка на пост администратора!"):
    name = discord.ui.TextInput(label = "Имя?")
    age = discord.ui.TextInput(label = "Возвраст?")
    sentry = discord.ui.TextInput(label = "Возвраст?")
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.paragraph)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "Заявка на администратора!", description = f"Имя: {name}\nВозвраст: {age}\nЧасовой поис: {sentry}\nПочему именно вы: {whyou}\nНемного о себе\n")
        await interaction.response.send_message(embed = embed, ephemeral = False)
        
class ModalSend(discord.ui.Select):
    def __init__(self):
        async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_modal(SyrveyModal())
        
class ModalView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(ModalSend())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def modal(self, ctx):
        await ctx.send("Pick Color", view = ModalView())
      
async def setup(client):
    await client.add_cog(Modal(client))
