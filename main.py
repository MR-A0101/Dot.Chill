import os
import json
import discord
import asyncio
from awake import awake
from itertools import cycle
from discord_components import *
from discord.ext import commands, tasks


#<--------BotBoot-------->
client = discord.Client()
client = commands.Bot(command_prefix=".", intents = discord.Intents.default())
client.remove_command('help')
status = cycle(["prefix=(.) | .help", "Developed with â¤ï¸ & ð§  by\n MR-A "])
#status = cycle(['ð§ Under Construction ð§', 'We will be functional soon!'])


#<--------Exception-------->
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send("**Chill bruh**, stay in the chill ä¹ð¬Õ²Î£ for `{:.2f}`secâï¸".format(error.retry_after))

  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Missing Argument Required for more help type:")
    await ctx.send("`.help_command name` | `eg: .help_help`ð.")

  if isinstance(error, commands.MissingPermissions):
    message = await ctx.send("You need Admin privileges to run this command!")
    await asyncio.sleep(0.1)
  count = 0
  while (count == 0):
    await message.edit(content=f"{ctx.author.mention} tried to use an unauthorised command.")
    await asyncio.sleep(0.1)
    await message.edit("âââYou need Admin privileges to run this command!")


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
    await ctx.send(f"``` \nYou do not have any Recording to be displayed. ð¤ª\n ```")


@client.command()
async def hidden(ctx):
    embed = discord.Embed(
        description=
        f"||*I'm chilling in " + str(len(client.guilds)) + " servers! ð*||",
        color=0x1d2333)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def bye(ctx):
  await ctx.send("This server is costing me an inrogranic growth therefore I will be leaving this server!")
  await ctx.guild.leave()

#<--------Cogs-Int----------->
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
   client.load_extension(f'cogs.{filename[:-3]}')
  if filename.endswith('.js'):
    client.load_extension(f'cogs.{filename[:-3]}')


#<--------End-to-End-------->
awake()
client.run(os.getenv('TOKEN'))
