import discord
from discord.ext import commands
from discord import app_commands

class about(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="questions", description="Send you answers!")
    async def questions(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Hello")