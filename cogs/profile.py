import discord
from discord.ext import commands
from discord_components import *
from datetime import datetime 

class ProfileCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def profile(self, ctx, member: discord.Member):
    embed = discord.Embed(
        title=f"Profile of {member.name}",
        url=
        f"https://discord.com/users/{member.id}",
        color=0x592bef, timestamp = datetime.utcnow())
    embed.set_thumbnail(url=f"{member.avatar_url}"
    )

    embed.add_field(
      name="Server Nickname", value=f"```{member.nick}```", inline=True)
    embed.add_field(
      name="Joined Discord", value=f"```{member.created_at.strftime('%d.%m.%y, %H:%M Hrs')}```", inline=True)
    embed.add_field(
      name="Permissions", value=f"```{member.guild_permissions}```")
    embed.add_field(
      name="Region", value=f"```{ctx.guild.region}```")
    embed.add_field(
      name="Joined Server", value=f"```{member.joined_at.strftime('%d.%m.%y, %H:%M Hrs')}```", inline=True)
    embed.add_field(
      name="Bot?", value=f"```{member.bot}```")
    embed.add_field(
      name="Activities", value=f"```{member.activities}```", inline=False)
    embed.add_field(
      name="Activity", value=f"```{member.activity}```", inline=False)
#    embed.add_field(
#      name="Top Role", value=f"{member.top_role.mention}", inline=True)  
#    embed.add_field(
#      name="Roles", value=f"{member.top_role.mention}", inline=True)
#    embed.add_field(
#      name="Active Nitro", value=f"```{member.premium_since}```", inline=True)'''
    embed.set_footer(text=f"Requested by {ctx.author.nick}")
    await ctx.send(embed=embed)

#   await ctx.send("‏‏‎ ‎", components=[Button(style=5 ,url="https://google.com", label="Invite")])



def setup(client):
  client.add_cog(ProfileCog(client))
