import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.file(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(jdata['URL_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))