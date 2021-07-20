import discord
from discord.ext import commands
from discord_components import *

class RecordCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases =['record', 'tape'])
  async def rec(self, ctx):
    embed = discord.Embed(
        description=
        f"The function is currently under devlopement.",
        color=0x004e92)
    embed.set_footer(text=f"{ctx.author.id}")

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(RecordCog(client))
  {ctx.author.nick}
