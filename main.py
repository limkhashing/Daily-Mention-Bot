import asyncio
import os
import random

from apscheduler.schedulers.blocking import BlockingScheduler

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = int(os.getenv('DISCORD_SERVER_ID'))
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
YING_DISCORD_ID = os.getenv('YING_DISCORD_ID')

bot = commands.Bot(command_prefix='!')
client = discord.Client()
schedule = BlockingScheduler()


class FuckYouCategory(commands.Cog):
    @commands.command(name='fuckyouall', help="Want to know how I develop this Bot? Suck my dick first")
    # @commands.has_role('admin')
    async def mention_everyone(self, ctx):
        await ctx.send(ctx.guild.default_role)

    @commands.command(name='fuckyouying', help="Want to know how I develop this Bot? Suck my dick first")
    # @commands.has_role('admin')
    async def mention_ying(self, ctx):
        await ctx.send(YING_DISCORD_ID)

    @commands.command(name='roll', help='Simulates rolling dice.')
    async def roll(self, ctx):
        dice = [
            str(random.choice(range(1, 6 + 1)))
            for _ in range(1)
        ]
        await ctx.send(', '.join(dice))


@client.event
async def on_ready():
    print("Discord Bot running!")
    client.loop.create_task(schedule_mention_ying())  # best to put it in here


async def schedule_mention_ying():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        await channel.send("FUCK YOU " + YING_DISCORD_ID)
        await asyncio.sleep(300)  # or 300 if you wish for it to be 5 minutes


# @client.event
# async def on_message(message):
#     guild = client.get_guild(SERVER_ID)
#     # message.author == client.user
#     if '!fuckyouall' in message.content.lower():
#         await message.channel.send("Hi")
#     elif message.content == "!users":
#         await message.channel.send(f"""# of Members: {guild.member_count}""")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        await ctx.send('LANJIAO, SEE !HELP LA')


bot.add_cog(FuckYouCategory())
client.run(TOKEN)
bot.run(TOKEN)
