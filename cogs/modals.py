import discord
from discord.ext import commands
from pymongo import MongoClient


class Buttons(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label = "Принять", style = discord.ButtonStyle.green)
    async def clicktru(self, interaction: discord.Interaction, child: discord.ui.Button):
        for child in self.children:
            child.disabled = True
        guild = interaction.guild
        channel = discord.utils.get(guild.text_channels, name = "приняты")
        await channel.send(f"{interaction.user}, ваша заявка принята!")
        await interaction.response.edit_message(view = self)
        await interaction.response.send_message("Успешно", ephemeral = True)
        
    @discord.ui.button(label = "Отказать", style = discord.ButtonStyle.red)
    async def clickfalse(self, interaction: discord.Interaction, child: discord.ui.Button):
        for child in self.children:
            child.disabled = True
        user = interaction.user
        await user.send(f"{user}, ваша заявка отклонена!")
        await interaction.response.edit_message(view = self)
        await interaction.response.send_message("Успешно", ephemeral = True)

class RegModal(discord.ui.Modal, title = "Регистрация аккаунта на фейсите!"):
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://Setroom:CFLrxCSX0fzBIMlA@cluster0.l9fw9.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.colluser = self.cluster.faceit.user
        self.game = self.cluster.faceit.game
        
    name = discord.ui.TextInput(label = "Имя в игре:", min_length = 2, max_length = 15)
    age = discord.ui.TextInput(label = "id в игре:", min_length = 8, max_length = 20)
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user
        await interaction.response.send_message("Мы получили вашу заявку!", ephemeral = True)
        
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Registration", emoji="📝", description="Регистрация аккаунта!"),
            ]
        super().__init__(placeholder="Выберите нужный пункт:", options = options) #max_values = 1, min_values = 1,
    async def callback(self, interaction: discord.Interaction):
        while True:
            if self.values[0] == "Registration":
                await interaction.response.send_modal(RegModal())
                await interaction.response.send_message("Вы успешно зарегистрированы!", ephemeral = True)
            
class ModalView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def регистрация(self, ctx):
        embed = discord.Embed(title = "Набор на Staff, Administrator, Eventer", description = "Выберите нужную категорию и заполните заявку!")
        await ctx.send(embed = embed, view = ModalView())
      
async def setup(client):
    await client.add_cog(Modal(client))
