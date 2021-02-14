import discord
from discord.ext import commands

import typing
import random

class Relations(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['murder', 'gameend'])
    async def kill(self,ctx,user: typing.Union[discord.Member, str], *rest):

        if type(user) == discord.Member:

            if user == ctx.author:

                embed = discord.Embed(

                    title="You cant kill yourself. Kill someone else.",
                    colour=0xff0000

                )

                await ctx.send(embed= embed)

                return

            embed = discord.Embed(

                description=f"{user.mention} was killed by {ctx.author.mention}",
                colour=0x33e18d

            )

        else:

            output = '{}{}'.format(user, ' '.join(rest))

            embed = discord.Embed(

                description=f"{output} was killed by {ctx.author.mention}",
                colour=0x33e18d
                
            )

        await ctx.send(embed= embed)

        

    @commands.command()
    async def kiss(self,ctx,user: typing.Union[discord.Member, str] = None, *rest):

        if user == None:

            await ctx.send('Enter something/someone to kiss dumbass')

        else:

            embed = discord.Embed(

                colour=0x33e18d

            )

            if type(user) == discord.Member:

                if user == ctx.author:

                    embed = discord.Embed(

                        title=f"{ctx.author.name} has kissed themself",
                        description="How the fuck have you done that?",
                        colour=0xff0000

                    )

                    await ctx.send(embed= embed)

                else:

                    embed.add_field(

                        name="Woah!",
                        value=f"{user.mention} has been kissed by {ctx.author.mention}!",
                        inline=True

                    )

                    await ctx.send(embed= embed)

            else:

                obj = '{}'.format(' '.join(rest))

                fobj = f'{user} {obj}'

                embed.add_field(

                    name=f"Woah!",
                    value=f"{ctx.author.mention} has kissed **{fobj}**!",
                    inline=True

                )

                await ctx.send(embed= embed)

    @commands.command()
    async def hug(self,ctx,user: typing.Union[discord.Member, str] = None, *rest):

        if user == None:

            await ctx.send('Enter something/someone to hug dumbass')

        else:

            embed = discord.Embed(

                colour=0x33e18d

            )

            if type(user) == discord.Member:

                if user == ctx.author:

                    embed = discord.Embed(

                        title=f"{ctx.author.name} has hugged themself",
                        description="Aw man. How sad.",
                        colour=0xff0000

                    )

                    await ctx.send(embed= embed)

                else:

                    embed.add_field(

                        name="So soft!",
                        value=f"{user.mention} has been hugged by {ctx.author.mention}!",
                        inline=True

                    )

                    await ctx.send(embed= embed)

            else:

                obj = '{}'.format(' '.join(rest))

                fobj = f'{user} {obj}'

                embed.add_field(

                    name=f"So soft!",
                    value=f"{ctx.author.mention} has hugged **{fobj}**!",
                    inline=True

                )

                await ctx.send(embed= embed)


    @commands.command()
    async def punch(self,ctx,user: typing.Union[discord.Member, str] = None, *rest):

        if user == None:

            embed = discord.Embed(

                title=f"{ctx.author.name} has punched the air!",
                description="Why?",
                colour=0xff0000

            )

            await ctx.send(embed=embed)

        else:

            embed=discord.Embed(

                colour=0x33e18d

            )

            if type(user) == discord.Member:

                if ctx.author == user:

                    embed.add_field(

                        name="Ouch!",
                        value=f"{ctx.author.mention} has punched themself. Did that hurt a little?",
                        inline=True

                    )

                    await ctx.send(embed=embed)

                else:

                    embed.add_field(

                        name="Thwack!",
                        value=f"{ctx.author.mention} has punched **{user.mention}**.",
                        inline=True

                    )

                    await ctx.send(embed=embed)

            else:

                obj = '{}'.format(' '.join(rest))

                fobj = f'{user} {obj}'

                embed.add_field(

                    name="Pow!",
                    value=f"{ctx.author.mention} has punched {fobj}.",
                    inline=True

                )

                await ctx.send(embed=embed)


            

def setup(bot):
    bot.add_cog(Relations(bot))