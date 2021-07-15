import discord 
from discord.ext import commands

class HelloCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def hello(self, ctx):
    await ctx.reply(f"Hello, {ctx.author.mention}👋",)  

  @commands.Cog.listener()
  async def on_message(self, message):
    print(f"{message.author}----> *{message.content}* over {message.guild} on {message.channel}")

def setup(client):
  client.add_cog(HelloCog(client))