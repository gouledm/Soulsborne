from sqlite3 import Timestamp
import discord
from discord.ext import commands
from autosearch import autosearch
from scraper import scraper

bot = commands.Bot(command_prefix='!')
searcher = autosearch()
scraper = scraper()

@bot.command()
async def find(ctx, *, arg):
    link = autosearch.search(arg)
    image = scraper.scrapeImage(link)
    p = scraper.scrapeP(link)
    img = "https://eldenring.wiki.fextralife.com" + image
    embed=discord.Embed(title="Elden Ring", description=p, color=0xBBA14F, footer = "Soulsborne")
    embed.set_image(url = img)
    await ctx.send(embed=embed)

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

bot.run(token)
print("Running!")