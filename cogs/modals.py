import discord
from discord.ext import commands
from pymongo import MongoClient

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Registration", emoji = "👌", description = "This is option 1!")
            ]
        super().__init__(placeholder = "Выберите нужное:", options = options)
    async def callback(self, interaction: discord.Interaction):
        while True:
            if self.values[0] == "Registration":
                await interaction.response.edit_message(content="This is the first option from the entire list!")

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class RegModal(discord.ui.Modal, title = "Регистрация аккаунта:"):
    name = discord.ui.TextInput(label = "Имя в игре:", min_length = 2, max_length = 15)
    idgame = discord.ui.TextInput(label = "id в игре:", min_length = 8, max_length = 20)
    async def on_submit(self, interaction: discord.Interaction):
        self.cluster = MongoClient("mongodb+srv://Setroom:CFLrxCSX0fzBIMlA@cluster0.l9fw9.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.colluser = self.cluster.faceit.user
        guild = interaction.guild
        user = interaction.user
        post = {"user_id": user.id, "guild_id": guild.id, "name": self.name, "idgame": self.idgame, "mmr": 0, "qual": 0, "pro": 0, "qualle": 0, "prole": 0, "verify": 0, "kill": 0, "die": 0, "win": 0, "lose": 0}
        await interaction.response.send_message("Вы зарегистрированны!", ephemeral = True)
        self.colluser.insert_one(post)
        
class Buttons(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label = "Регистрация", style = discord.ButtonStyle.green)
    async def click(self, interaction: discord.Interaction, child: discord.ui.Button):
        guild = interaction.guild
        user = interaction.user
        await interaction.response.send_modal(RegModal())
        await interaction.response.send_message("Зарегистрируйтесь!", ephemeral = True)
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def регистрация(self, ctx):
        embed = discord.Embed(title = "Регистрация аккаунта!", description = "Чтобы зарегистрироваться нужно нажать на кнопку ниже и заполнить анкету по примеру ниже!")
        await ctx.send(embed = embed, view = Buttons())
      
async def setup(client):
    await client.add_cog(Modal(client))
