import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient

import character_generation
import explore_dungeon


cluster = MongoClient("mongodb+srv://Ujju:1q23AC3NENMO@cluster0.raj2u.mongodb.net/discordrpg?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster["discordrpg"]
collection = db["characters"]

# post = {"_id": 0, "name": "George", "score": 5}
#
# collection.insert_one(post)

mha_threats = [
    'Are you talking shit about my hero, bro?',
    'I\'ll kiss your sister.',
    'You gay.',
    'https://media1.tenor.com/images/ca901e5e61c484795bbfd1becee21361/tenor.gif?itemid=13260423',
]

mha_insults = [
    ' bad',
    'bad ',
    ' filler',
    'filler ',
    ' fillers',
    'fillers ',
    ' slow',
    'slow ',
    ' shit',
    'shit ',
    ' sucks',
    'sucks ',
    ' i hate',
    'i hate ',
]

mha_titles = [
    ' mha',
    'mha ',
    ' my hero',
    'my hero ',
    ' my hero academia',
    'my hero academia ',
    ' boku no hero',
    'boku no hero ',
    ' boku no hero academia',
    'boku no hero academia ',
]

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
    mha_insult = False
    mha_title = False

    for i in mha_insults:
        if i in message.content.lower():
            mha_insult = True

    for i in mha_titles:
        if i in message.content.lower():
            mha_title = True

    if mha_insult and mha_title is True:
        response = random.choice(mha_threats)
        await message.channel.send(response)

    await client.process_commands(message)


# Bot commands
@client.command()
async def bot_command(ctx):
    print(f'{client.user} is performing the !bot_command action')
    # do something

    await ctx.send(ctx.author)


@client.command()
async def new_character(ctx):
    characterName, hp, mp, strength, dexterity, intelligence, experience = character_generation.character_generation()
    randomID = random.randrange(99999999999)
    user = ctx.author

    # fail safe for creating a character with the same ID as another
    while randomID is collection.find({"_id": randomID}):
        randomID = random.randrange(99999999999)

    # post request to put the randomly generated character into the DB
    post = {"_id": randomID,
            "user": str(user),
            "name": characterName,
            "hp": hp,
            "mp": mp,
            "strength": strength,
            "dexterity": dexterity,
            "intelligence": intelligence,
            "experience": experience}
    collection.insert_one(post)

    await ctx.send("ID: " + str(randomID) +
                   ", Name: " + characterName +
                   ", HP: " + str(hp) +
                   ", MP: " + str(mp) +
                   ", STR: " + str(strength) +
                   ", DEX: " + str(dexterity) +
                   ", INT: " + str(intelligence) +
                   ", EXP: " + str(experience))


@client.command()
async def lookup_characters(ctx):
    results = collection.find({"user": str(ctx.author)})

    for result in results:
        await ctx.send(result)

    await ctx.send("done.")


@client.command()
async def explore(ctx, ID, dungeon_level):
    selected_character = []
    results = collection.find({"_id": int(ID)})

    # iterates through the cursor object and places it into a dictionary
    for result in results:
        selected_character.append(result)
        # await ctx.send(result)


    character_experience_gained, character_alive = explore_dungeon.explore_selected_dungeon(selected_character, dungeon_level)

    updated_experience = selected_character[int('experience')] + character_experience_gained

    if character_alive is True:
        # update character
        collection.update({"_id": int(ID)}, {"$set": {"experience": str(updated_experience)}})
    else:
        # delete character
        # collection.delete_one({"_id": int(ID)})
        await ctx.send("Character has died.")

    await ctx.send("Combat cleared.  Experience Gained:  " + character_experience_gained)

client.run(TOKEN)
