import discord
from discord.ext import commands
import os

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("#"), 
                         intents=discord.Intents().all())
        
        self.cogslist = ["cogs.invites", "cogs.inviteshop"]
    
    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)
    
    async def on_ready(self):
        print(bot.user.name + " is ready.")
        synced = await bot.tree.sync()
           
bot = Client()
bot.run("ODg4NjIyNzQwNjk1ODE4Mjgw.G0o362.hsjc6jA1j5F4qTyM4Cjlj1S5Rx5Ost1Wdf-iTg")
