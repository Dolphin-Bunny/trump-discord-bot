from markov import speak

#speak will generate a Trump quote

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Mr Trump, your covfefe is {}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$trump'):
        print("trump talked to "+message.author.name)
        await message.channel.send(speak())

client.run('Njk3NTQzNzI3MzQ1OTU5MTEy.Xo40PQ.2cPpBrczUk0BeCzYOTtX5FUOf0U')