import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(719612847021097084)
            while not self.bot.is_closed():
                em = jdata['em']
                await msg.channel.send(em)
                await self.channel.send("Running...")
                await asyncio.sleep(5)#sec

        #async def interval():
        #    await self.bot.wait_until_ready()
        #    self.channel = self.bot.get_channel(719612847021097084)
        #    while not self.bot.is_closed():
        #        await self.chnnel.send("Task Working!")
        #        await asyncio.sleep(10)#sec
        #        now_time = datetime.datetime.now().strftime('%H%M')
        #        with open('setting.json','r',encoding='utf8') as jfile:
        #            jdata = json.load(jfile)
        #        if now_time == jdata['time']:
        #            await self.chnnel.send("Task Working!")
        #            await asyncio.sleep(10)#sec
        #        else:
        #            await asyncio.sleep(10)#sec
        #            pass

        self.bg_task = self.bot.loop.create_task(interval())
    
    @commands.command()
    async def set_channel(self, ctx ,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')

    @commands.command()
    async def set_time(self,ctx,time):
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time']= time
        with open('setting.json','w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)

def setup(bot):
    bot.add_cog(Task(bot))