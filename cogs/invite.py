import discord 
from discord.ext import commands
from discord_components import *

class InviteCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases =['i'])
  #@commands.has_permissions(administrator=False)
  async def invite(self, ctx):
    embed = discord.Embed()
    await ctx.reply(f"‏‏‎🥳Hey, **{ctx.author.display_name}** invite me into your server too!🎉",
      components=[
       Button(style=5 ,url="https://discord.com/api/oauth2/authorize?client_id=818451840399179776&permissions=8&scope=bot", label="Invite")
       ])

    interaction = await self.client.wait_for("button_clicked", check=lambda i: i.component.label.startswith("Click"))
    await interaction.respond(content=f"{ctx.author.discplay_name} Visit your Dot.Chill Dashboard:https://dot.chill.xyz")

def setup(client):
  client.add_cog(InviteCog(client))