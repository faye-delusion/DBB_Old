import discord
from discord.ext import commands
import asyncio
import datetime

class Meta(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(aliases= ['bug','reportbug'])
    async def report(self,ctx,*bug):

        if len(bug) < 1:

            return await ctx.send(embed=discord.Embed(title='Send actual bug reports dumbfuck',colour=0xff0000))

        bug = '{}'.format(' '.join(bug))

        bugReportGuild = self.bot.get_guild(612486154440146944)
        bugReportChannel = bugReportGuild.get_channel(792775188722089984)

        bugReport = discord.Embed(

            title= f"Bug Report",
            description=datetime.datetime.now().strftime('Submitted on **%a %d %B, %Y** at **%H:%M:%S**'),
            colour=0xff0000

        )

        bugReport.add_field(

            name="User:",
            value=f"{ctx.author}",
            inline=True

        )

        bugReport.add_field(

            name="User's ID:",
            value=f"{ctx.author.id}",
            inline=True

        )

        bugReport.add_field(

            name="Guild:",
            value=ctx.guild.name,
            inline=True

        )

        bugReport.add_field(

            name="Guild ID:",
            value=ctx.guild.id,
            inline=True

        )

        bugReport.add_field(

            name="Issue:",
            value=bug,
            inline=False

        )

        newBugReport = await bugReportChannel.send(embed=bugReport)

        await ctx.message.delete()

        await ctx.send('Bug report sent!')

        await asyncio.sleep(2.0)

        await newBugReport.delete()

    @commands.command(aliases=['featurerequest','suggest'])
    async def feature(self,ctx,*feature):

        if len(feature) < 1:

            return await ctx.send(embed=discord.Embed(title="Send actual feature requests you fucking dumbass",colour=0xff0000))

        feature = '{}'.format(' '.join(feature))

        featureRequestChannel = self.bot.get_guild(612486154440146944).get_channel(804026670826520586)

        featureRequest = discord.Embed(

            title="New Feature Request",
            description=datetime.datetime.now().strftime('Submitted on **%a %d %B, %Y** at **%H:%M:%S**'),
            colour=0xffff00

        )

        featureRequest.add_field(

            name="User:",
            value=ctx.author,
            inline=True

        )

        featureRequest.add_field(

            name="User ID:",
            value=ctx.author.id,
            inline=True

        )

        featureRequest.add_field(

            name="Guild:",
            value=ctx.guild.name,
            inline=True

        )

        featureRequest.add_field(

            name="Guild ID:",
            value=ctx.guild.id,
            inline=True

        )

        featureRequest.add_field(

            name="Feature Request:",
            value=feature,
            inline=False

        )

        newFeatureRequest = await featureRequestChannel.send(embed=featureRequest)

        await ctx.message.delete()

        confirmation = await ctx.send("Feature request sent!")
        
        await asyncio.sleep(2.0)

        await confirmation.delete()

        await newFeatureRequest.add_reaction('👍')
        await newFeatureRequest.add_reaction('👎')

        def check(reaction, user):

            return reaction.message.id == newFeatureRequest.id and str(reaction.emoji) in ['👍','👎']


        try:

            print('waiting')

            user = discord.Member

            while user.id != 265152100575477760:

                reaction,user = await self.bot.wait_for('reaction_add', check=check)


            if reaction.emoji == '👍' and user.id == 265152100575477760:

                await newFeatureRequest.edit(embed=discord.Embed(title="Feature Request Accepted!",colour=0x00ff00).add_field(name="Requested Feature:",value=feature,inline=False))
                await newFeatureRequest.clear_reactions()

            elif reaction.emoji == '👎' and user.id == 265152100575477760:

                await newFeatureRequest.edit(embed=discord.Embed(title="Feature Request Denied!",colour=0xff0000).add_field(name="Requested Feature:",value=feature,inline=False))
                await newFeatureRequest.clear_reactions()


        except:

            print('wah')
            

def setup(bot):
    bot.add_cog(Meta(bot))