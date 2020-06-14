import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):  
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} join')
        channel = self.bot.get_channel(int(jdata['member-list']))
        await channel.send(f'{member} join ')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave')
        channel = self.bot.get_channel(int(jdata['member-list']))
        await channel.send(f'{member} leave  ')

    @commands.Cog.listener() 
    async def on_message(self, msg):
        keyword = jdata['keyword']
        em = jdata['em']
        if msg.content in keyword and msg.author != self.bot.user:
            random_msg = random.choice(jdata['keyword'])
            await msg.channel.send(random_msg)
        elif msg.content in em:
            await msg.channel.send("!em")

def setup(bot):
    bot.add_cog(Event(bot))