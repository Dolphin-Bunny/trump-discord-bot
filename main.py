from markov import speak

#speak will generate a Trump quote

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Mr Trump, your covfefe is {}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="FOX News"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$trump'):
        print("trump talked to "+message.author.name)
        await message.channel.send(speak())

client.run('token')
