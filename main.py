import discord
import os
from awake import awake
from itertools import cycle 
from discord.ext import commands, tasks

client = discord.Client()
client = commands.Bot(command_prefix=".")
status = cycle(["prefix=(.) | .help", "Developed with ❤️ & 🧠 by MR-A "])
#status = cycle(['🚧 Under Construction 🚧', 'We will be function soon!'])

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
async def hello(ctx):
  await ctx.send("Hello! 👋")

@client.command()
async def hidden(ctx):
  await ctx.send("**||I am a bot Developed by MR-A, vist him at https://mr-a0101.github.io/||**")

@client.command()
async def aid(ctx):
  embed = discord.Embed(
    title = 'Title',
    description = 'This is a description.',
    colour = discord.Colour.blue()
  )
  
  embed.set_footer(text='This is a footer.')
  embed.set_author(name='DotDotChill')
  embed.add_field(name='`Command`', value='Description', inline=True)
  embed.add_field(name='`Command`', value='Description', inline=True)

  await client.say(embed=embed)

#end-to-end
awake()
client.run(os.getenv('TOKEN'))