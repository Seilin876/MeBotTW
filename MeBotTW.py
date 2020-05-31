import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join')
    channel = bot.get_channel(716689928553103380)
    await channel.send(f'{member} join ')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave')
    channel = bot.get_channel(716689928553103380)
    await channel.send(f'{member} leave  ')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('NzE0ODM4NTc4NTg4Mjg3MTE3.XtPPLg.oHlKz5uS35DkGKsZQYRIII16dfw')