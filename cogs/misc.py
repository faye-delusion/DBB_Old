import discord
from discord.ext import commands
import random

class Misc(commands.Cog):


    def __init__(self,bot):
        self.bot=bot

    
    @commands.command()
    async def foo(self,ctx):

        await ctx.send('bar')

    @commands.command()
    async def invite(self,ctx):

        embed = discord.Embed(

            title= "Wanna add Dick and Balls Bot to your own server?",
            description="Click [here](https://discord.com/api/oauth2/authorize?client_id=659540200053276685&permissions=8&scope=bot) to use this bot in your own server!",
            colour=0x33e18d

        )

        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await ctx.send(embed= embed)

    @commands.group(aliases=['%', 'perc', 'what%'])
    async def percentage(self,ctx, *arg):

        # Generate num between 1 & 100
        perc = int(round(random.uniform(1,100)))

        embedvar=discord.Embed(
            
            title="\U0001F3B2 Percentage",
            description="You are {}% **{}**".format(perc, ' '.join(arg)), 
            colour=0x33e18d
            
        )

        embedvar.set_footer(text=f"Command called by {ctx.author.name}")

        # Send output to user
        await ctx.send(embed=embedvar)

def setup(bot):
    bot.add_cog(Misc(bot))