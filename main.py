import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") #you can set a custom prefix

@bot.command()
async def help(ctx):
  await ctx.send("working")
  
bot.run("Your Tocken here")
