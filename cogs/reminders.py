import discord
from discord.ext import commands, tasks
from discord.utils import get

class RemindersCog(commands.Cog, name='Reminders'):
    def __init__(self, bot):
        self.bot = bot
        self.reminded_roles = [
            '789641928932720640',
            '1004503459481014354'
        ]
        self.reminder_loop.start()

    @tasks.loop(hours=14 * 24)
    async def reminder_loop(self):
        members = []
        embed = discord.Embed(
            title = 'Reminder',
            description = '''
                This is a reminder to create/update your Tech Team Memoires!
                You can find them here: <https://www.notion.so/aicamp/Tech-Team-Memoires-22062b9c78c64436819e51efda7f8117>
                These are **mandatory** for every person on the team, and are due every 2 weeks.
            ''',
            color = discord.colour.Color.blue()
        )
        # get all members in 1 or more of the reminded_roles
        for role_id in self.reminded_roles:
            role = get(self.bot.guilds[0].roles, id=int(role_id))
            if role is None:
                continue
            for member in role.members:
                members.append(member)
        
        # send a DM to each member
        for member in members:
            try:
                await member.send(embed=embed)
            except discord.errors.Forbidden:
                log_channel = get(self.bot.guilds[0].channels, id=789603989439643669)
                await log_channel.send(f'Failed to send reminder to {member.mention}')
        
def setup(bot):
    '''
    Adds Reminders cog to bot.
    '''
    bot.add_cog(RemindersCog(bot))