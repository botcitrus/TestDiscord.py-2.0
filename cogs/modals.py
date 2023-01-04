import discord
from discord.ext import commands

class StaffModal(discord.ui.Modal, title = "Заявка на пост стаффа!"):
    name = discord.ui.TextInput(label = "Имя?")
    age = discord.ui.TextInput(label = "Возвраст?")
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?")
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.paragraph)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.user.send(f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе")
        
class AdmModal(discord.ui.Modal, title = "Заявка на пост администрации!"):
    name = discord.ui.TextInput(label = "Имя?")
    age = discord.ui.TextInput(label = "Возвраст?")
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?")
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.paragraph)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.user.send(f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе")
        
class EveModal(discord.ui.Modal, title = "Заявка на пост ивентера!"):
    name = discord.ui.TextInput(label = "Имя?")
    age = discord.ui.TextInput(label = "Возвраст?")
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?")
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.paragraph)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.user.send(f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе")
        
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Staff", emoji="🔧", description="Заявка на роль стаффа"),
            discord.SelectOption(label="Administrator", emoji="⚒", description="Заявка на роль администрации"),
            discord.SelectOption(label="Eventer", emoji="🔮", description="Заявка на роль ивентера")
            ]
        super().__init__(placeholder="Выберите нужный пункт:", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Staff":
            await interaction.response.send_modal(StaffModal())
            embed = discord.Embed(title = "STAFF", description = "Заявка на роль staff принята!")
            await interaction.response.send_message(embed = embed)
        elif self.values[0] == "Administrator":
            await interaction.response.send_modal(AdmModal())
            embed = discord.Embed(title = "ADMINISTRATOR", description = "Заявка на роль administrator принята!")
            await interaction.response.send_message(embed = embed)
        elif self.values[0] == "Eventer":
            await interaction.response.send_modal(EveModal())
            embed = discord.Embed(title = "EVENTER", description = "Заявка на роль eventer принята!")
            await interaction.response.send_message(embed = embed)
            
class Buttons(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label = "Red", style = discord.ButtonStyle.red)
    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(SurveyModal())
        await interaction.response.send_message("This is the first option from the entire list!")
            
class ModalView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def набор(self, ctx):
        embed = discord.Embed(title = "Набор на Staff, Administrator, Eventer", description = "Выберите нужную категорию и заполните заявку!")
        await ctx.send(embed = embed, view = ModalView())
      
async def setup(client):
    await client.add_cog(Modal(client))
