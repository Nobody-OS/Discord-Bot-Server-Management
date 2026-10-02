import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv

# .env laden
load_dotenv()

token = os.getenv("BOT_TOKEN")

if not token:
    raise ValueError("BOT_TOKEN wurde nicht gefunden.")

# Logging
handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="w"
)

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot
bot = commands.Bot(
    command_prefix="/",
    intents=intents
)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot ist online als {bot.user}")

# Command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.tree.command(name="ping", description="Zeigt den Ping des Bots an.")
async def ping(interaction: discord.Interaction):
    ping = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! `{ping}ms`"
    )

# Bot starten
bot.run(
    token,
    log_handler=handler,
    log_level=logging.DEBUG
)