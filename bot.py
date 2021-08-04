import discord
import os
from dotenv import load_dotenv
from discord.ext import commands



# Retrieve discord token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Establish prefix (!) for bot commands
client = commands.Bot(command_prefix ='!')


## Bot Events

# Initialize Discord Bot
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# Bot member join event
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

# Bot messaging event
@client.event
async def on_message(message):

    # Ignore if message author is the bot
    if message.author == client.user:
        return

     # do something

    await client.process_commands(message)
        

## Bot commands

@client.command()
async def bot_command(ctx):
    print(f'{client.user} is performing the !bot_command action')
    
    # do something
    
    await ctx.send(f'!bot_command completed')

@client.command()
async def clear(ctx, amount=15):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    
    print(f'{client.user} has performed !clear action')
    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')




client.run(TOKEN)