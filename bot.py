import discord
from discord.ext import commands
import random
import asyncio
#import stratroulette



description = '''Autisme er en epidemi'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def gay(ctx):
    """
    Says if a user is gay.
   	check for subcommand 
    """
    if ctx.invoked_subcommand is None:
        await bot.say('Yes, {0.subcommand_passed} is very gay'.format(ctx))

@gay.command(name='Latii')
async def _bot():
    """Is the Latii gay?"""
    await bot.say('no u')

@bot.command(pass_context=True)
async def jump():
	places = ["Military Base", "Novorepnoye", "Novorepnoye Containers", "Primorsk", "Gatka", "Georgopol", 
		"Georgopol Containers", "Zharki", "Severny", "Shooting Range", "Yasnaya Polyana", "Pochinki", 
		"Rozhok", "Stalber", "Mylta", "Mylta Powerplant", "Lipovka", "Farm", "Shelter", "Farm",
		"Prison", "Mansion", "Kameshki", "School", "Ruins", "Hospital", "Quarry", "Ferry Pier"]


	await bot.say(random.choice(places))

@bot.command(pass_context=True)
async def jegsutter():
	locations = ["Anarchy Acres", "Dusty Depot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", 
		"Junk Junction", "Lonely Lodge", "Loot Lake", "Lucky Landing", "Moisty Mire", "Pleasant Park", "Retail Row", 
		"Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	await bot.say(random.choice(locations))


#@bot.group(pass_context=True)
#async def strat(ctx):
#	if ctx.invoked_subcommand is None



bot.run('NDI1NzA3NDk5OTU0MzcyNjEw.DZLYMw.eNjsqqUQm6ASpjWCZ6sV_rZipIU')
