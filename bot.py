import os

import discord
from discord.ext import commands, tasks

token = os.environ.get('REMINDER_BOT_DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='%', intents=intents, help_command=None)

cogs = ['reminders']

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, bot.user.id)
    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')

if __name__ == '__main__':
    bot.run(token)