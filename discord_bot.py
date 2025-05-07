import discord
import tweepy

# Start of discord code

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Whats poppin')

client.run('MTI4MzY4MDQ3MzMzNTQ2Mzk3MA.G9Gxaq.gZ0LLf4GSTGLgym8KVWA0bJolZoJ-vCFwB3l5I')

# End of discord code

# Start of twitter code

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAMda0wEAAAAAbehbtd1ZMqM8dAVfkhlu3xlx9dk%3DhpiS6TooWhPTDjqGzvEh2eQOPI2rCeTioS9sEqlzczZkovApqs")

# End of twitter codes