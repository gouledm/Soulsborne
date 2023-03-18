from sqlite3 import Timestamp
import discord
from discord.ext import commands
from autosearch import autosearch
from scraper import scraper

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)
searcher = autosearch()
scraper = scraper()

@bot.slash_command(name="find", description="Search for Elden Ring information")
async def find(ctx, arg: str):
    link = autosearch.search(arg)
    image = scraper.scrapeImage(link)
    p = scraper.scrapeP(link)
    img = "https://eldenring.wiki.fextralife.com" + image
    embed=discord.Embed(title="Elden Ring", description=p, color=0xBBA14F)
    embed.set_image(url = img)
    await ctx.send(embed=embed)

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

print("Running!")
bot.run(token)

