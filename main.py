# Discord Imports
import discord
from discord.ext import commands
import discord.utils
# Python Imports
import re
import os
# Other Imports

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: The Bot, created by Pointless#1278.', self_bot=False,)
bot.remove_command('help')

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='!help | {} servers'.format(len(bot.servers))), status='online')
    print('Online.')
    print('https://discordapp.com/oauth2/authorize?client_id=431951773159129098&scope=bot&permissions=2146958591')
  
@bot.command(pass_context=True)
async def hithere(ctx):
    bot.say('ohhimark')

if not os.environ.get('TOKEN'):
   print("No tokens!")
bot.run(os.environ.get('TOKEN').strip('"'))
