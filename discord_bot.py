import discord
from twitter_bot import tweets
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Allows for used of commands through discord chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('hello')

# Automatically searches for a post at certain interval and,
# post it in a specific channel.
@tasks.loop(hours=24)
async def my_task():
    channel = client.get_channel('channel ID here')
    for tweet in tweets:
        await channel.send('"https://twitter.com/anyuser/status/" + str(tweet.id)')

@client.event
async def on_ready():
    my_task.start()


client.run('your token here')


