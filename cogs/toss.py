import random
import discord 
from discord.ext import commands

class TossCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.cooldown(3,7,commands.BucketType.user)
  async def toss(self, ctx):
    choices = [f"** Heads**", f"**  Tails**"]
    rancoin = random.choice(choices)
    await ctx.reply(f"🪙")
    await ctx.send(rancoin)  
    
def setup(client):
  client.add_cog(TossCog(client))