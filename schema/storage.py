@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    message = await ctx.send("You need Admin privileges to run this command!")
    await asyncio.sleep(0.1)
  count = 0
  while (count == 0):
    await message.edit(content=f"{ctx.author.mention} tried to use an unauthorised command.", components=[Button(style=5 ,url="https://google.com", label="Invite1")])
    await asyncio.sleep(0.1)
    await message.edit("‏‏‎You need Admin privileges to run this command!", components=[Button(style=5 ,url="https://google.com", label="Invite2")])