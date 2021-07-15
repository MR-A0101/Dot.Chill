import discord
import asyncio
from discord.ext import commands

class TimerCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.cooldown(2,60,commands.BucketType.user)
  async def timer(self, ctx, seconds):
    try:
      secondsint = int(seconds)
      if secondsint > 420:
        await ctx.send("Not over 7 minutes")
        await ctx.send("""```r
Time️️ ⏲️ Stamps
Seconds    Minutes
060 sec    1 min
120 sec    2 min
180 sec    3 min
240 sec    4 min
300 sec    5 min
360 sec    6 min
420 sec    7 min
```""")
        raise BaseException
      if secondsint <= 0:
        await ctx.send("No negatives")
        await ctx.send("""```r
Time️️ ⏲️ Stamps
Seconds    Minutes
060 sec    1 min
120 sec    2 min
180 sec    3 min
240 sec    4 min
300 sec    5 min
360 sec    6 min
420 sec    7 min
```""")
        raise BaseException

      message = await ctx.send(f"Timer: ``{seconds}`` seconds left!")

      while True:
        secondsint-= 1
        if secondsint == 0:
          await message.edit(content="Timer ⏰ Endded!")
          break

        await message.edit(content=f"Timer: ``{secondsint}`` seconds left!")
        await asyncio.sleep(1)
      await ctx.reply(f"{ctx.author.mention}, Your timer for ``{seconds}`` seconds has ended.")
    except ValueError:
      await ctx.send("Enter an positive numerical value.")
      await ctx.send("""```r
Time️️ ⏲️ Stamps
Seconds    Minutes
060 sec    1 min
120 sec    2 min
180 sec    3 min
240 sec    4 min
300 sec    5 min
360 sec    6 min
420 sec    7 min
```""")

def setup(client):
  client.add_cog(TimerCog(client))
