import discord
from discord.ext import commands
from pymongo import MongoClient

class ModModal(discord.ui.Modal, title = "Заявка на модератора:"):
    age = discord.ui.TextInput(label = "Возвраст:", min_length = 1, max_length = 2, placeholder = "14")
    time = discord.ui.TextInput(label = "Время на сервере:", min_length = 8, max_length = 20, placeholder = "1-2 месяца")
    experions = discord.ui.TextInput(label = "Опыт работы:", placeholder = "2 года, был на серверах: Saints, PTO, STO и т.д.")
    active = discord.ui.TextInput(label = "Активность:", placeholder = "5-6 часов в день")
    FA2 = discord.ui.TextInput(label = "2FA:", placeholder = "есть/нет")
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel = discord.utils.get(guild.channels, id = "1060262034496815176")
        embed = discord.Embed(title = "Заявка на Moderator", description = f"Пользователь: {interaction.user}\nВозвраст: {self.age}\nВремя на сервере: {self.time}\nОпыт работы: {self.experions}\nАктивность: {self.active}\n2FA: {self.FA2}")
        await interaction.response.send_message("Заявка получена и будет рассмотрена в ближайщее время!", ephemeral = True)
        await channel.send(embed = embed)
        
class PMModal(discord.ui.Modal, title = "Заявка на пиар-менеджера:"):
    age = discord.ui.TextInput(label = "Возвраст:", min_length = 1, max_length = 2, placeholder = "14")
    time = discord.ui.TextInput(label = "Время на сервере:", min_length = 8, max_length = 20, placeholder = "1-2 месяца")
    experions = discord.ui.TextInput(label = "Опыт работы:", placeholder = "2 года, был на серверах: Saints, PTO, STO и т.д.", style=discord.TextStyle.short)
    active = discord.ui.TextInput(label = "Количество партнёрок:", placeholder = "20-30 в день", style=discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel = discord.utils.get(guild.channels, id = "1060262034496815176")
        embed = discord.Embed(title = "Заявка на Piar Manager", description = f"Пользователь: {interaction.user}\nВозвраст: {self.age}\nВремя на сервере: {self.time}\nОпыт работы: {self.experions}\nКоличество партнёрок: {self.active}")
        await channel.send(embed = embed)

class DesModal(discord.ui.Modal, title = "Заявка на дизайнера:"):
    age = discord.ui.TextInput(label = "Возвраст:", min_length = 1, max_length = 2, placeholder = "14")
    time = discord.ui.TextInput(label = "Время на сервере:", min_length = 8, max_length = 20, placeholder = "1-2 месяца")
    experions = discord.ui.TextInput(label = "Опыт работы:", placeholder = "2 года, был на серверах: Saints, PTO, STO и т.д.")
    device = discord.ui.TextInput(label = "Устройство:", placeholder = "телефон/пк")
    rob = discord.ui.TextInput(label = "Готовы работать бесплатно, за пиар:", placeholder = "да/нет")
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel = discord.utils.get(guild.channels, id = "1060262034496815176")
        embed = discord.Embed(title = "Заявка на Designer", description = f"Пользователь: {interaction.user}\nВозвраст: {self.age}\nВремя на сервере: {self.time}\nОпыт работы: {self.experions}\nДевайс: {self.device}\nГотовы работать бесплатно, за пиар: {self.rob}")
        await interaction.response.send_message("Заявка получена и будет рассмотрена в ближайщее время!", ephemeral = True)
        await channel.send(embed = embed)
        
class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = "Moderator", emoji = "⚒", description = "Заявка на модератора!"),
            discord.SelectOption(label = "Request-PM", emoji = "🔎", description = "Заявка на пиар-менеджера!"),
            discord.SelectOption(label = "Designer", emoji = "🖌", description = "Заявка на дизайнера!")
            ]
        super().__init__(placeholder = "Выберите нужное:", options = options)
    async def callback(self, interaction: discord.Interaction):
        while True:
            if self.values[0] == "Moderator":
                await interaction.response.send_modal(ModModal())
                await interaction.response.send_message("Заполните заявку!", ephemeral = True)
            elif self.values[0] == "Request-PM":
                await interaction.response.send_modal(PMModal())
                await interaction.response.send_message("Заполните заявку!", ephemeral = True)
            elif self.values[0] == "Designer":
                await interaction.response.send_modal(DesModal())
                await interaction.response.send_message("Заполните заявку!", ephemeral = True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout = timeout)
        self.add_item(Select())
        
class Modal(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def reg(self, ctx):
        embed = discord.Embed(title = "Регистрация аккаунта!", description = "Чтобы зарегистрироваться нужно нажать на кнопку ниже и заполнить анкету по примеру ниже!")
        await ctx.send(embed = embed, view = SelectView())
      
async def setup(client):
    await client.add_cog(Modal(client))
