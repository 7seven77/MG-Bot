import config
import dynamo
from discord.ext import commands
from discord import MemberCacheFlags
import discord

intents = discord.Intents.default()
intents.members = True

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

initial_extensions = ['cogs.moderation', 'cogs.misc', 'cogs.suggestions', 'cogs.eventlogging',
                      'cogs.autoroles', 'cogs.trello', 'cogs.tekken', 'cogs.questions']

bot = commands.Bot(command_prefix='$', case_insensitive=False, description="MG Bot", intents=intents,
                   member_cache_flags=MemberCacheFlags.from_intents(intents))
for extension in initial_extensions:
    bot.load_extension(extension)
dynamo.init()

bot.run(TOKEN)
