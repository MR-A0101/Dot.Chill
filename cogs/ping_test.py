import discord 
from discord.ext import commands

class Ping_testCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    latency = self.client.latency
    trueLatency = latency * 1000

    embed = discord.Embed(
        description=
        f"It takes me **{round(trueLatency)}** milliseconds to respond.🚀",
        color=0x00cdac)

    await ctx.reply(embed=embed)
    
def setup(client):
  client.add_cog(Ping_testCog(client))