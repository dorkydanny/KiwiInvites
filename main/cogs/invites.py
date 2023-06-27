import discord  
from discord.ext import commands
from discord import app_commands
import json

class invites(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        f = open("main/invites.json")
        self.data = json.load(f)
    
    @app_commands.command(name="invites", description="Amount of invites a user has.")
    async def invites(self, interaction: discord.Interaction, user: discord.User):
        totalInvites = 0
        for i in await interaction.guild.invites():
            if i.inviter == interaction.message.author:
                totalInvites += i.uses
        embed = discord.Embed(colour=discord.Color.dark_teal(),
                              title="Invites", 
                              description=f"{user.display_name} has {totalInvites} invite(s)")
        embed.set_author(name="Kiwi Invites.")
        self.data[str(user.id)] = totalInvites
        with open("main/invites.json", "w") as outfile:
            json.dump(self.data, outfile)
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(invites(bot))