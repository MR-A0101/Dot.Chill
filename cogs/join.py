import discord 
from discord.ext import commands

class JoinCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def join(self, ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send(f"Nice to see that this channel is active. 🤗")
    else:
        await ctx.send(f"You are not in a voice channel. 🙁")

def setup(client):
  client.add_cog(JoinCog(client))