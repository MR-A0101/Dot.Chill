import discord 
import datetime
from discord.ext import commands

#help.help
class HelpingCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help_help(self, ctx):
    embed = discord.Embed(
        title="🎙️ Dot.Chill **Help** Command List 🎙️",
        url=
        "")

    embed.add_field(name="More Help", value="`.help_help`", inline=True)
    embed.set_footer(text=f"{ctx.author.id} this function is currently under devlopement.")

    await ctx.send(embed=embed)

  @commands.command()
  async def profile_help(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x43cea2)

    embed.set_footer(text=f"{ctx.author.id}", icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=embed)

  @commands.command()
  async def C(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x4568dc)

    embed.set_footer(text=f"{ctx.author.id}", icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=embed)

  @commands.command()
  async def helpxprofile(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x43cea2)

    embed.set_footer(text=f"{ctx.author.id}", icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=embed)

  @commands.command(aliases =['help_timer'])
  async def timer_help(self, ctx):
    embed = discord.Embed(
        description=
        f"*Syntax* = `.timer time(in seconds)` | eg: `.timer 10`",
        color=0x4568dc)

    embed.set_footer(text=f"{ctx.author.id}", icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(HelpingCog(client))
