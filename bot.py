import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join')
    channel = bot.get_channel(int(jdata['member-list']))
    await channel.send(f'{member} join ')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave')
    channel = bot.get_channel(int(jdata['member-list']))
    await channel.send(f'{member} leave  ')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])