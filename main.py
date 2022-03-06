from sqlite3 import Timestamp
import discord
from discord.ext import commands

from scraper import scraper

bot = commands.Bot(command_prefix='!')
scrape = scraper()
img = "https://eldenring.wiki.fextralife.com" + scraper.image
print(img)
@bot.command()
async def astrologer(ctx):
    embed=discord.Embed(title="Elden Ring", description=scraper.div, color=0xBBA14F, footer = "Soulsborne")
    embed.set_image(url = img)
    await ctx.send(embed=embed)

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

bot.run(token)
