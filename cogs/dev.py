import discord
from discord.ext import commands
from discord_components import *

class DevCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases =['Developer'])
  #@commands.has_permissions(administrator=False)
  async def dev(self, ctx):
    embed = discord.Embed()
    await ctx.reply(f"‏‏‎Hello, @everyone me and my friends including Chief have been working on a server for closed community people. \n\nWhere people interested in computer science can discuss and share resources about, programming, ctfs, osint, malware exploitation & analysis and being a community of like-minded individuals we all can even take in team members for hackathons, ctfs, even seek out for coding help, or just hang out in our own space. \n\nTherefore i would love to invite you all into this amazing community of people.\nhttps://discord.gg/wg3BQjWsv4",
      components=[
       Button(style=5 ,url="https://discord.gg/wg3BQjWsv4", label="DevCluster Discord Server Invitaion")
       ])

    interaction = await self.client.wait_for("button_clicked", check=lambda i: i.component.label.startswith("Click"))
    await ctx.add_reaction(":link:")
    await interaction.respond(content=f"{ctx.author.discplay_name} Visit your Dot.Chill Dashboard:https://dot.chill.xyz")

def setup(client):
  client.add_cog(DevCog(client))
