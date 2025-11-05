import discord
from discord.ext import commands
from music import MusicCog
import json

# Carregar config
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f"Bot iniciado como {bot.user}")

# Carregar módulo de música
bot.add_cog(MusicCog(bot))

bot.run(config["token"])
