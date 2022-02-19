# IMPORTS

import discord
import json
import requests

from private.config import token  # personalized token
from discord.ext import commands, tasks

# read about documentation: https://discordpy.readthedocs.io/en/

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="shrine")
async def get_shrine(ctx):
    shrine = []
    response = requests.get("https://dbd.onteh.net.au/api/shrine")
    print("STATUS (shrine): " + str(response.status_code))

    perks = json.loads(response.text)

    for perk in perks["perks"]:
        shrine.append(perk["id"])

    await ctx.send(", ".join(shrine))


@bot.command(name="m1")
async def m1(ctx):
    await ctx.send("TheBurntCroissant has m1'd more times than there are atoms in the universe.")


@bot.command(name="help")
async def get_shrine(ctx):
    await ctx.send("Valid commands: 'm1', 'shrine'.")


bot.run(token)
