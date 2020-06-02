import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 圖片(self, ctx):
        #pic = discord.File('C:\\Users\\a0926\\Source\\Repos\\MeBotTW\\pic\\X.png')
        #await ctx.send(file= pic)
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def 測(self, ctx):
        random_pic = random.choice(jdata['URL_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))