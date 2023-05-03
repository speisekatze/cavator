import discord
from discord import app_commands
from discord import Intents
import time
import asyncio
import locale
from src.config import conf
from src.xml import lookup

intents = Intents.default()

locale.setlocale(locale.LC_ALL, "de_DE")
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

def user_is_owner(ctx):
    return ctx.message.author.id == conf['owner']

@tree.command(name = "hello", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name="bbig")
async def bbig_lookup(interaction, para: str):
    result = lookup('bbig', para=para)
    await interaction.response.send_message(f"```\r\n{result}\r\n```")

@tree.command(name="ausbv")
async def ausbv_lookup(interaction, para: str):
    result = lookup('ausbv', para=para)
    await interaction.response.send_message(f"```\r\n{result}\r\n```")