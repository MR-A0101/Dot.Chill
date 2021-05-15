import requests
import discord
import json
import os
from awake import awake
from itertools import cycle
from discord.ext import commands, tasks

status = cycle(['prefix=( . ) | .help', 'Developed with ❤️ & 🧠 by MR-A'])
client = commands.Bot(command_prefix='.')


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " ~" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    change_status.start()
    print('{0.user} is Online!'.format(client))


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('.inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('.help'):
        await message.channel.send(
            '**🎙️ Dot.Chill Command List 🎙️**\n \n *General Commands* \n `.help` General help command.\n `.hello` Just a random Hello! \n `.hidden` See a secret of ours.\n `.inspire` Feeling down just try this command.\n \n *Voice Channel Commands* \n `.record` Voice-Channel Recording command.\n `.play` To play the recorded chat.\n `.log` Display the recording logs.'
        )

    if msg.startswith('.hello'):
        await message.channel.send('Hello')

    if msg.startswith('.hidden'):
        await message.channel.send(
            '**||I am a bot Developed by MR-A, vist him at https://mr-a0101.github.io/||**'
        )


awake()
client.run(os.getenv('TOKEN'))
