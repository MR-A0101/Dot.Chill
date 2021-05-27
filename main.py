import os
import random
import discord
from awake import awake
from itertools import cycle
from discord.ext import commands, tasks


#<--------BotBoot<-------->
client = discord.Client()
client = commands.Bot(command_prefix=".", intents = discord.Intents.default())
client.remove_command('help')
status = cycle(["prefix=(.) | .help", "Developed with ❤️ & 🧠 by\n MR-A "])
#status = cycle(['🚧 Under Construction 🚧', 'We will be functional soon!'])


#<--------Exception-------->
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send("**Chill bruh**, stay in the chill 乙𝔬ղΣ for {:.2f}sec✌️".format(error.retry_after))


#<--------Status-------->
@client.event
async def on_ready():
    change_status.start()
    print('{0.user} is Online!'.format(client))


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#<--------Commands----------->
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="🎙️ Dot.Chill Command List 🎙️",
        url=
        "https://discord.com/api/oauth2/authorize?client_id=818451840399179776&permissions=8&scope=bot",
        description=
        "This list is constantly growing and changing as the bot evolves!",
        color=0x1ed5f2)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/818451840399179776/dc3a8395b2e108ec0849de24b6aaf1b1.png"
    )
    embed.add_field(name="👮 Help", value="`.help`", inline=True)
    embed.add_field(name="🤝 Greet", value="`.hello`", inline=True)
    embed.add_field(name="🥷 Hidden", value="`.hidden`", inline=True)
    embed.add_field(name="🟢 Join VC", value="`.join`", inline=True)
    embed.add_field(name="🔴 Leave VC", value="`.leave`", inline=True)
    embed.add_field(name="📹 Record", value="`.rec`", inline=True)
    embed.add_field(name="⏱️ Timer", value="`.timer`", inline=True)
    embed.add_field(name="🪙 Toss", value="`.toss`", inline=True)
    embed.add_field(name="📒 Rec_Logs", value="`.r_logs`", inline=True)
#   embed.add_field(name="🤩 Inspiration", value="`.inspire`", inline=True)
#   embed.set_footer(text="")
    await ctx.send(embed=embed)


@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}👋")


@client.command()
async def r_logs(ctx):
    await ctx.send(f"``` \nYou do not have any Recording to be displayed. 🤪\n ```")


@client.command()
async def hidden(ctx):
    await ctx.send("||*I'm chilling in " + str(len(client.guilds)) + " servers! 😎*||")


@client.command()
@commands.cooldown(1,7,commands.BucketType.user)
async def toss(ctx):
    choices = ["** Heads**", "**  Tails**"]
    await ctx.send("🪙")
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Nice to see that this channel is active. 🤗")
    else:
        await ctx.send("You are not in a voice channel. 🙁")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel. 🐾")
    else:
        await ctx.send("I am not in a voice channel. 😂")


#<--------End-to-End-------->
awake()
client.run(os.getenv('TOKEN'))