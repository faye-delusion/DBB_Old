import discord
from discord.ext import commands
import random
import datetime
import json

class Quotes2(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def quote(self,ctx):

        f = open(f"./guildData/{ctx.guild.id}/quotes.txt", "r")

        data = f.readlines()

        randnum = random.randint(1,len(data)-1)

        output = data[randnum]

        Embed=discord.Embed(description=f"**{output}**", color=0x33e18d)
        Embed.set_author(name=f"Quote {randnum} of {len(data)-1}")
        await ctx.send(embed=Embed)

    @quote.command()
    async def add(self,ctx,*quote):

        msg = str('{}'.format(' '.join(quote)))

        if len(msg) > 400:

            await ctx.send("Quote too long. Max 400 characters.")

        else:

            msgauthor = ctx.author.mention

            cdtime = datetime.datetime.now().strftime("%A %d %B %Y *(%H:%M:%S GMT)*")

            payload = f'"{msg}" - **{msgauthor}**, {cdtime}'

            with open(f"./guildData/{ctx.guild.id}/quotes.txt","a") as f:

                f.write(f"{payload}\n")
                
            with open(f"./guildData/{ctx.guild.id}/quotes.txt","r") as f:

                data = f.readlines()

            await ctx.send(f'New quote added. Quote ID: `{len(data)-1}`')

    @quote.command() 
    async def index(self,ctx,index: int = None): 

        with open(f'./guildData/{ctx.guild.id}/quotes.txt','r') as f: 

            data = f.readlines() 

        if index == None:

            await ctx.send(f'Enter a number dipshit. There are `{len(data)-1}` quotes registered in this server.')

        embed = discord.Embed( 

            title= f'Quote #{index} of {len(data)-1}', 
            description= f'{data[index]}', 
            colour=0x33e18d 

        )

        await ctx.send(embed= embed) 


def setup(bot):
    bot.add_cog(Quotes2(bot))