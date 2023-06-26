import discord

from discord import app_commands
from discord.ext import commands
import os
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot at Kiwi's service!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="invites")
async def invites(interaction: discord.Interaction, user:discord.User):
    total_invites = 0
    for i in await interaction.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    await interaction.response.send_message(total_invites)

bot.run(os.environ.get('TOKEN'))

