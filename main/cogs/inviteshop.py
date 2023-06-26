import discord  
from discord.ext import commands
from discord import app_commands

class invitesshop(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="inviteshop", description="Buy perks for invites")
    async def inviteshop(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Invite Shop", 
                              description="Buy ranks here!", 
                              colour=discord.Color.dark_teal())
        embed.add_field(name="One Month Premium", value="15 Invites")
        embed.add_field(name="One Month Kiwi", value="30 Invites", inline=1)
        embed.set_footer(text="Property of Kiwi.")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(invitesshop(bot))