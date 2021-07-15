import discord 
from discord.ext import commands

class LeaveCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def leave(self, ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f"I left the voice channel. 🐾")
    else:
        await ctx.send(f"I am not in a voice channel. 😂")

def setup(client):
  client.add_cog(LeaveCog(client))