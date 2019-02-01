import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='b!')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------')

   
bot.run('NTQwNzM4MTQ0ODE1ODA4NTI3.DzZIHA.0gW_mr3AL_omCxV9VX_XQAk7PmY')
