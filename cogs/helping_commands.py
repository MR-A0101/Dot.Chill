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
        f"The function is currently under devlopement.",
        color=0x004e92)

    embed.set_footer(text=f"{ctx.author.id}")

    await ctx.send(embed=embed)

  @commands.command()
  async def B(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x43cea2)

    embed.set_footer(text=f"{ctx.author.id}")

    await ctx.send(embed=embed)

  @commands.command()
  async def C(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x4568dc)

    embed.set_footer(text=f"{ctx.author.id}")

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(HelpingCog(client))
