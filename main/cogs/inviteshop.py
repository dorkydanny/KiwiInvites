import discord  
from discord.ext import commands
from discord import app_commands
import json

class invitesshop(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        f = open("main/invites.json")
        self.data = json.load(f)
    
    @app_commands.command(name="inviteshop", description="Buy perks for invites")
    async def inviteshop(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Invite Shop", 
                              description="Buy ranks here!", 
                              colour=discord.Color.dark_teal())
        embed.add_field(name="One Month Premium", value="15 Invites")
        embed.add_field(name="One Month Kiwi", value="30 Invites", inline=1)
        embed.set_footer(text="Property of Kiwi.")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="buy", description="Buy a rank for invites.")
    @app_commands.describe(ranks="Ranks to choose from")
    
    @app_commands.choices(ranks=[ 
        discord.app_commands.Choice(name="Premium", value="premium"),
        discord.app_commands.Choice(name="Kiwi", value="kiwi")
    ])
    async def buy(self, interaction: discord.Interaction, ranks: discord.app_commands.Choice[str]):
        ranks = ranks.value
        prices = {"premium" : 15, "kiwi" : 30}
        if self.data[str(interaction.user.id)] >= prices[ranks]:
            self.data[str(interaction.user.id)] -= prices[ranks]
            with open("main/invites.json", "w") as outfile:
                json.dump(self.data, outfile)
            await interaction.response.send_message(f"Succesfuly brought {ranks} for {prices[ranks]} invites.")
        await interaction.response.send_message("You do not have enough invites.\n" +
                                                f"You have: {self.data[str(interaction.user.id)]}\n" +
                                                f"You need: {prices[ranks]}")
        
    @app_commands.command(name="gift", description="Gift a rank for invites.")
    @app_commands.describe(ranks="Ranks to choose from")
    
    @app_commands.choices(ranks=[ 
        discord.app_commands.Choice(name="Premium", value="premium"),
        discord.app_commands.Choice(name="Kiwi", value="kiwi")
    ])
    async def gift(self, interaction: discord.Interaction, user: discord.User, ranks: discord.app_commands.Choice[str]):
        ranks = ranks.value
        prices = {"premium" : 15, "kiwi" : 30}
        if self.data[str(interaction.user.id)] >= prices[ranks]:
            self.data[str(interaction.user.id)] -= prices[ranks]
            with open("main/invites.json", "w") as outfile:
                json.dump(self.data, outfile)
            await interaction.response.send_message(f"Succesfuly gifted {ranks} for {prices[ranks]} invites.")
        await interaction.response.send_message("You do not have enough invites.\n" +
                                                f"You have: {self.data[str(interaction.user.id)]}\n" +
                                                f"You need: {prices[ranks]}")
    

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(invitesshop(bot))