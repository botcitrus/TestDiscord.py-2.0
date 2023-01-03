import discord
from discord.ext import commands

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = "Blue", emoji = ":blue:", description = "Blue Test"),
            discord.SelectOption(label = "Red", emoji = ":red:", description = "Red Test"),
            discord.SelectOption(label = "Green", emoji = ":green:", description = "Green Test")
        ]
        super().__init__(placeholder = "Выберите цвет:", max_values = 1, min_values = 1, options = options)
        
        async def callback(self, interaction: discord.Interaction):
            user = interaction.user
            guild = interaction.guild
            if self.values[0] == "Blue":
                await interaction.response.send_message(f"Вы выбрали Синий", ephemeral = True)
            elif self.values[0] == "Red":
                await interaction.response.send_message(f"Вы выбрали Красный", ephemeral = True)
            elif self.values[0] == "Green":
                await interaction.response.send_message(f"Вы выбрали Зелёный", ephemeral = True)
                
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout = timeout)
        self.add_item(Select())
        
        
class SelectMenu(commands.cog):
    def __init__(self, client)
        self.client = client
      
    @commands.command()
    async def select(self)
        await ctx.send("Pick Color", view = SelectView(), delete_after = 15)
      
async def setup(client):
    await client.add_cog(SelectMenu(client))
