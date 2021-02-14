import discord
import random
from discord.ext import commands

class Prediction(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    responses = [

        "Definitely not",
        "Probably not",
        "Nope",
        "No",
        "I guess so",
        "Yes",
        "Definitely a possibility",
        "Potentially",
        "Perhaps yes",
        "100%"
    ]

    @commands.command(aliases=['8ball', 'predict'])
    async def _8ball(self, ctx, *args):

        userinput = '{}'.format(' '.join(args))
        embedvar=discord.Embed(
            
            title=" " , 
            description=f'**{ctx.message.author.name} asked "{userinput}"**', 
            color=0x33e18d
            
        )
        embedvar.set_author(name='\U0001F3B1 8Ball')
        embedvar.add_field(name="Dick and Balls Bot says..", value=f"{random.choice(Prediction.responses)}" , inline=True)

        await ctx.send(embed=embedvar)
        

        

def setup(bot):
    bot.add_cog(Prediction(bot))
