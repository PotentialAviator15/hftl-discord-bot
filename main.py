import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="~")

@client.slash_command(guild_ids=theServerId)
asyc def test(ctx):
  await ctx.respond("testing successful")
  
 @client.command()
 asyc def testt(ctx):
   await ctx.send("testing successful")
  
  
 token = os.environ.get("TOKEN")
 @client.run(token)
