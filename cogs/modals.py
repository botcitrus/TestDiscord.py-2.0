import discord
from discord.ext import commands

class SurveyModal(discord.ui.Modal, title = "Заявка на пост администратора!")
    name = discord.ui.TextInput(label = "Имя?")
    answer = discord.ui.TextInput(label = "Возвраст?")
    invite = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Submission entered", ephemeral = False)
        
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
            await interaction.response.edit_message(content = "This is the first option from the entire list!")
        elif self.values[0] == "Blue":
            await interaction.response.send_message("This is the second option from the list entire wooo!", ephemeral=False)
        elif self.values[0] == "Green":
            await interaction.response.send_message("Third One!", ephemeral=False)
            
        await interaction.response.send_modal(SurveyModal())
        
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def select(self, ctx):
        await ctx.send("Pick Color", view = SelectView())
      
async def setup(client):
    await client.add_cog(Modal(client))
