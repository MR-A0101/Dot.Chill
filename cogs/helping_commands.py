import discord 
from discord.ext import commands

#help.help
class HelpingCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def A(self, ctx):
    embed = discord.Embed(
        description=
        "```This is an unlist embed (A)```",
        color=0x004e92)

    await ctx.send(embed=embed)

  @commands.command()
  async def B(self, ctx):
    embed = discord.Embed(
        description=
        "This is an unlist embed (B)",
        color=0x43cea2)

    await ctx.send(embed=embed)

  @commands.command()
  async def C(self, ctx):
    embed = discord.Embed(
        description=
        "This is an unlist embed (C)",
        color=0x4568dc)

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(HelpingCog(client))