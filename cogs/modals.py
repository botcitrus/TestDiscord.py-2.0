import discord
from discord.ext import commands


class Buttons(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label = "Принять", style = discord.ButtonStyle.green)
    async def clicktru(self, interaction: discord.Interaction, buttont: discord.ui.Button):
        for buttont in self.buttonren:
            buttont.disabled = True
        guild = interaction.guild
        channel = discord.utils.get(guild.text_channels, name = "приняты")
        await channel.send(f"{interaction.user}, ваша заявка принята!")
        await interaction.response.edit_message(view = self)
        await interaction.response.send_message("Успешно", ephemeral = True)
        
    @discord.ui.button(label = "Отказать", style = discord.ButtonStyle.red)
    async def clickfalse(self, interaction: discord.Interaction, buttonf: discord.ui.Button):
        for buttonf in self.buttonren:
            buttonf.disabled = True
        user = interaction.user
        await user.send(f"{user}, ваша заявка отклонена!")
        await interaction.response.edit_message(view = self)
        await interaction.response.send_message("Успешно", ephemeral = True)

class StaffModal(discord.ui.Modal, title = "Заявка на пост стаффа!"):
    name = discord.ui.TextInput(label = "Имя?", min_length = 2, max_length = 15)
    age = discord.ui.TextInput(label = "Возвраст?", min_length = 1, max_length = 2)
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?", min_length = 2, max_length = 3)
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.short)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user
        view = Buttons()
        channel = discord.utils.get(guild.text_channels, name = "заявки")
        embed = discord.Embed(title = "Заявка на Staff", description = f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе: {self.yourslf}")
        await channel.send(embed = embed, view = view)
        await interaction.response.send_message("Мы получили вашу заявку!", ephemeral = True)
        
class AdmModal(discord.ui.Modal, title = "Заявка на пост администрации!"):
    name = discord.ui.TextInput(label = "Имя?", min_length = 2, max_length = 15)
    age = discord.ui.TextInput(label = "Возвраст?", min_length = 1, max_length = 2)
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?", min_length = 2, max_length = 3)
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.short)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel = discord.utils.get(guild.text_channels, name = "заявки")
        embed = discord.Embed(title = "Заявка на Administration", description = f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе: {self.yourslf}")
        await channel.send(embed = embed)
        
class EveModal(discord.ui.Modal, title = "Заявка на пост ивентера!"):
    name = discord.ui.TextInput(label = "Имя?", min_length = 2, max_length = 15)
    age = discord.ui.TextInput(label = "Возвраст?", min_length = 1, max_length = 2)
    sentry = discord.ui.TextInput(label = "Часовой пояс от мск?", min_length = 2, max_length = 3)
    whyou = discord.ui.TextInput(label = "Почему именно вы?", style = discord.TextStyle.short)
    yourslf = discord.ui.TextInput(label = "Немного о себе", style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel = discord.utils.get(guild.text_channels, name = "заявки")
        embed = discord.Embed(title = "Заявка на Eventer", description = f"Имя: {self.name}\nВозвраст: {self.age}\nЧасовой поис: {self.sentry}\nПочему именно вы: {self.whyou}\nНемного о себе: {self.yourslf}")
        await channel.send(embed = embed)
        
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
            await interaction.response.send_message("Заявка на роль eventer принята!", ephemeral = True)
        elif self.values[0] == "Administrator":
            await interaction.response.send_modal(AdmModal())
            await interaction.response.send_message("Заявка на роль eventer принята!", ephemeral = True)
        elif self.values[0] == "Eventer":
            await interaction.response.send_modal(EveModal())
            await interaction.response.send_message("Заявка на роль eventer принята!", ephemeral = True)
            
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
