import discord
from discord.ext import commands
from discord_components import *

class HelpCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
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
    embed.add_field(name="🏓 Ping", value="`.ping`", inline=True)
    embed.add_field(name="‏‏‎🥳 Invite", value="`.invite`", inline=True)
    embed.add_field(name="‏‏‎🤸‍♂️ Profile", value="`.profile`", inline=True)
#   embed.add_field(name="🤩 Inspiration", value="`.inspire`", inline=True)
    embed.set_footer(text="For more help with a command type '.commandxhelp' eg: '.timerxhelp'")
    await ctx.send(embed=embed)

#   await ctx.send("‏‏‎ ‎", components=[Button(style=5 ,url="https://google.com", label="Invite")])



def setup(client):
  client.add_cog(HelpCog(client))
