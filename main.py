import discord
import os
import random
from awake import awake
from itertools import cycle 
from discord.ext import commands, tasks

client = discord.Client()
client = commands.Bot(command_prefix=".")
client.remove_command('help')
status = cycle(["prefix=(.) | .help", "Developed with ❤️ & 🧠 by MR-A "])
#status = cycle(['🚧 Under Construction 🚧', 'We will be functional soon!'])

#status
@client.event

async def on_ready():
  change_status.start()
  print('{0.user} is Online!'.format(client))

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

#commands
@client.command()
async def help(ctx):
  embed = discord.Embed(title="🎙️ Dot.Chill Command List 🎙️", url="https://github.com/MR-A0101", description="This list is constantly growing and changing as the bot evolves!", color=0x1ed5f2)
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/818451840399179776/dc3a8395b2e108ec0849de24b6aaf1b1.png")
  embed.add_field(name="👮 Help", value="`.help`", inline=True)
  embed.add_field(name="🤝 Greet", value="`.hello`", inline=True)
  embed.add_field(name="🥷 Hidden", value="`.hidden`", inline=True)
  embed.add_field(name="🟢 Join VC", value="`.join`", inline=True)
  embed.add_field(name="🔴 Leave VC", value="`.leave`", inline=True)
  embed.add_field(name="📹 Record", value="`.rec`", inline=True)
  embed.add_field(name="⏱️ Timer", value="`.timer`", inline=True)
  embed.add_field(name="🪙 Toss", value="`.toss`", inline=True)
  embed.add_field(name="📒 Rec_Log", value="`.log`", inline=True)
#  embed.set_footer(text="")
  await ctx.send(embed=embed)

#Commands----------->
@client.command()
async def hello(ctx):
  await ctx.send("Hello! 👋")

@client.command()
async def hidden(ctx):
  await ctx.send("**||I would love to be invited to your server!||**")

@client.command()
async def toss(ctx):
  choices = ["Heads", "Tails"]
  await ctx.send("https://tenor.com/view/coin-flip-flip-coin-gif-19747326")
  rancoin = random.choice(choices)
  await ctx.send(rancoin)

@client.command(pass_context = True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("Nice to see that this channel is active. 🤗")
  else:
    await ctx.send("You are not in a voice channel. 🙁")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I left the voice channel. 🐾")
  else: 
    await ctx.send("I am not in a voice channel. 😂")

#end-to-end
awake()
client.run(os.getenv('TOKEN'))