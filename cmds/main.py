import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def botsay(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://github.com/shanglin10/MeBotTW", description="This bot is for distance learning on discord.", color=0xff8000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mez", url="https://github.com/shanglin10", icon_url="https://media.discordapp.net/attachments/666616748916867095/717821262780432526/image0.jpg")
        embed.add_field(name="指令介紹", value="Instruction list", inline=True)
        embed.add_field(name="!圖片", value="sent a picture from file.", inline=False)
        embed.add_field(name="!web", value="sent a picture from url.", inline=False)
        embed.add_field(name="!em", value="about this bot.", inline=False)
        embed.add_field(name="!ping", value="show the ping.", inline=False)
        embed.add_field(name="!purge", value="purge message.", inline=False)
        embed.add_field(name="!botsay", value="let bot replace your message", inline=False)
        embed.add_field(name="!toss", value="random toss an number in range you define.", inline=False)
        embed.add_field(name="!set_channel", value="set your channel by copy your channel ID", inline=False)
        embed.set_footer(text="Hope you enjoy it!")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))