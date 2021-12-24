import getpass
from sqlite3.dbapi2 import connect
from typing import Text
from colorama import Fore, Style
from colorama import init, Fore, Back, Style
from discord import channel
from discord.client import Client
init(convert=True)
import os, time, datetime, random, asyncio, aiohttp, json, discord, time, colorama, requests, sqlite3
from itertools import cycle
from discord import Game, File
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure
import random
import string
import tkinter
from tkinter import messagebox

with open('config.json') as f:
    data = json.load(f)
token = data["tokenxxa"]
client = commands.Bot(command_prefix='!')
client.remove_command('help')
os.system('cls')
serverid = data["sevaidyannoo"]
delay = 2
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]
con = sqlite3.connect("Users.db", check_same_thread = False)
cur = con.cursor()

@client.event
async def on_ready():
    print("Bot Online :p")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="OMG CONFIG BOT"))
    import itertools, threading, time, sys
    done = False

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="OMG CONFIG BOT"))
    print(f'{Fore.RED}        Logged in on {Fore.YELLOW}{client.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{client.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "Members")
    await ctx.add_roles(role)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="", color=0x109319)
    embed.set_author(name="autism", url="https://discord.gg/BDDsARavSK", icon_url="https://media.discordapp.net/attachments/915745572953133096/916778786526228500/Cock_1.gif")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/915745572953133096/916778786526228500/Cock_1.gif")
    embed.add_field(name="========= Config Commands ========", value="B1g Pro", inline=False) 
    embed.add_field(name="!redeem {KEY}", value="Redeem keys from the selly to get API access", inline=False) 
    embed.add_field(name="(         Bot Made By Rosee_#1740         )", value="Big Pro", inline=False)
    ctx.author.display_name
    ctx.author.avatar_url    
    await ctx.send(embed=embed)

def keygen(size=20, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def MakeKeysForRedeem(size=27, chars=string.ascii_uppercase + string.digits):
  result = ''.join(random.choice(chars) for _ in range(size))
  with open("keys.txt", "a") as keys:
    keys.write(f"{result}\n")

@client.command(pass_context=True)

@has_permissions(administrator=True)
async def refill(ctx):
  author = ctx.message.author
  for i in range(100):
    MakeKeysForRedeem()
  await author.send(f"Heres All Of The Keys")
  await author.send(file=discord.File(r'keys.txt'))

## random command for u to get config requests into a server
@commands.cooldown(1, 300, commands.BucketType.user)
@client.command(name="request", pass_context=True)
async def request(ctx, arg1, *, text):
  author = ctx.message.author
  channel = client.get_channel() ## put the channel id in here
  embed=discord.Embed(title="Request", description="", color=0x109319)
  embed.set_author(name=f"{author}", url="https://discord.gg/BDDsARavSK", icon_url="https://media.discordapp.net/attachments/915745572953133096/916778786526228500/Cock_1.gif")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/915745572953133096/916778786526228500/Cock_1.gif")
  embed.add_field(name="========= Config Request ========", value=" ", inline=False) 
  embed.add_field(name="Name: ", value=f"{text}", inline=False) 
  embed.add_field(name="URL: ", value=f"{arg1}", inline=False)
  embed.add_field(name="Signiture: ", value="(         Bot Made By Rosee#0452         )", inline=False) 
  await channel.send(embed=embed)
  await ctx.send("you are now on a 5 min cooldown.")

@client.command(pass_context=True)
async def redeem(ctx, arg1):
    author = ctx.author
    with open(r'keys.txt') as file:
      filedata = file.read()
      if arg1 in filedata:
          generatedk = keygen()
          filedata = filedata.replace(arg1, "\n")
          with open('keys.txt', 'w') as file:
            file.write(filedata)
          print(f"{Fore.GREEN}{author} has a cool key lol")
          cur.executescript(f"INSERT INTO Users VALUES('{author}', '{arg1}', 'NULL'")
          print(f"key created user: {author} key: {generatedk} ip: NULL")
          await author.send(f"{generatedk} is your API Key Enjoy! \n the API url is: http://... the ip of where you host the api/api/configs \n THIS WILL LOCK TO THE FIRST IP \n DO NOT SHARE \n YOU WILL BE BANNED!")
          await ctx.send("wow a working key -_-")
      else:
        await ctx.send(f"The Key Given Isnt Correct ): Big Sad \n goto Retard.club to purchase one (: big happy then \n P.S If you dont buy your a nerd like {author} \n you have a cooldown of 5 mins")

client.run(token)

  