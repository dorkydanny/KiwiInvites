import discord  
from discord.ext import commands
from discord import app_commands
import json

class invites(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    f = open("main/invites.json")
    data = json.load(f)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(invites(bot))