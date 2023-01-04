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
        
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Red", emoji="❤️", description="This is option 1!"),
            discord.SelectOption(label="Blue", emoji="💙", description="This is option 2!"),
            discord.SelectOption(label="Green", emoji="💚", description="This is option 3!")
            ]
        super().__init__(placeholder="Select an option", max_values=1, min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Red":
            await interaction.response.send_modal(SyrveyModal())
            await interaction.response.edit_message(content = "This is the first option from the entire list!")
        elif self.values[0] == "Blue":
            await interaction.response.send_modal(SyrveyModal())
            await interaction.response.send_message("This is the second option from the list entire wooo!", ephemeral=False)
        elif self.values[0] == "Green":
            await interaction.response.send_modal(SyrveyModal())
            await interaction.response.send_message("Third One!", ephemeral=False)
            
class ModalView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def modal(self, ctx):
        await ctx.send("заявка на адм", view = ModalView())
      
async def setup(client):
    await client.add_cog(Modal(client))
