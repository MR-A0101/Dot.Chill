import os
import json
import discord
from awake import awake
from itertools import cycle
from discord_components import *
from discord.ext import commands, tasks


#<--------BotBoot-------->
client = discord.Client()
client = commands.Bot(command_prefix=".", intents = discord.Intents.default())
client.remove_command('help')
status = cycle(["prefix=(.) | .help", "Developed with ❤️ & 🧠 by\n MR-A "])
#status = cycle(['🚧 Under Construction 🚧', 'We will be functional soon!'])


#<--------Exception-------->
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send("**Chill bruh**, stay in the chill 乙𝔬ղΣ for `{:.2f}`sec✌️".format(error.retry_after))


#<--------Status-------->
@client.event
async def on_ready():
    change_status.start()
    print('''

    --------------------------
    {0.user} is Online!
    --------------------------

    '''.format(client))
    DiscordComponents(client)


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#<--------Commands----------->
@client.command()
async def r_logs(ctx):
    await ctx.send(f"``` \nYou do not have any Recording to be displayed. 🤪\n ```")


@client.command()
async def hidden(ctx):
    await ctx.send(f"||*I'm chilling in " + str(len(client.guilds)) + " servers! 😎*||")


#<--------Cogs-Int----------->
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
   client.load_extension(f'cogs.{filename[:-3]}')


#<--------End-to-End-------->
awake()
client.run(os.getenv('TOKEN'))
