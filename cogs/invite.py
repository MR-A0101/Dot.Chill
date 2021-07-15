import discord 
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

class InviteCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def invite(self, ctx):
    embed = discord.Embed(
        description=
        "This list is constantly growing and changing as the bot evolves!",
        color=0x1ed5f2)

    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(InviteCog(client))