import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import utils



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
async def make_channel(ctx, channel_name=None, category_name=None):
    # !make_channel
    if not channel_name:
        await ctx.send(f'No channel name provided.')
        return

    channel_name = channel_name.replace(' ','-')
    guild = ctx.guild
    if category_name:
        existing_category = utils.get(guild.categories, name = category_name)
        # Create category if none exists
        if not existing_category:
            await guild.create_category(category_name)
            category_name = utils.get(guild.categories, name = category_name)
        else:
            category_name = existing_category
    else:
        # Otherwise add channel to the current category
        category_name = ctx.message.channel.category

    channel = utils.get(category_name.channels, name = channel_name)
    if channel:
        await ctx.send(f'Channel <{channel_name}> already exists')
    else:
        await guild.create_text_channel(channel_name, category=category_name)
        await ctx.send(f'Channel <{channel_name}> created!')



client.run(TOKEN)
