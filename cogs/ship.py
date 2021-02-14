import discord
from discord.ext import commands

import random
import typing

class Ship(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def ship(self,ctx,u1: typing.Union[discord.Member, str] = None, u2: typing.Union[discord.Member, str] or str = None):

        if u1 == None or u2 == None:

            await ctx.send('Please tag 2 people.')

        else:

            if u1 == u2:

                await ctx.send('Tag 2 **different** people dipshit')

            else:

                compatibility = random.randint(1,100)

                embed = discord.Embed(

                    title= "⛵Ship",
                    description= f"Compatibility: **{compatibility}%**",
                    colour=0x33e18d

                )

                if type(u1) == discord.Member:

                    embed.add_field(

                        name="Input 1",
                        value= u1.mention,
                        inline=True
                    )

                else:

                    embed.add_field(

                        name="Input 1",
                        value=u1,
                        inline=True


                    )

                if type(u2) == discord.Member:

                    embed.add_field(

                        name="Input 2",
                        value= u2.mention,
                        inline=True

                    )

                else:

                    embed.add_field(

                        name="Input 2",
                        value=u2,
                        inline=True

                    )

                await ctx.send(embed= embed)

def setup(bot):
    bot.add_cog(Ship(bot))

