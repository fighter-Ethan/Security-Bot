import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import asyncio
from webserver import keep_alive
import os
import json
import requests
import random

client = commands.Bot(command_prefix = "!")
member = discord.Member
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Activity
  (type = discord.ActivityType.watching , name = "for hackers | !help"))
  print("Bot is up.")

@client.event
async def on_guild_join(guild):
   general = find(lambda x: x.name == 'general-chat',  guild.text_channels)
   if general and general.permissions_for(guild.me).send_messages:
     await general.send('Hello {}! Do /setup to set up!'.format(guild.name))

@client.command()
async def setup(ctx):
  await ctx.send("Put the ID of the channel that you want to be your verify channel!")
  verify = await client.wait_for("int")
  verifyy = int(verify)
  channel = client.get_channel(verifyy)
  await channel.send(str("React Here!"))


@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=837701845039710229&permissions=8&scope=bot")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)

