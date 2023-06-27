import discord
from discord.ext import commands

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
bot.run("ODg4NjIyNzQwNjk1ODE4Mjgw.GPPXx2.FYiGihUhWInBm5PUCPenegQO4NWvY0z0XbH3NE")
