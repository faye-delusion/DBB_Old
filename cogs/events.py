import discord
import asyncio
import typing
from discord.ext import commands
from main import get_prefix



class Events(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    

    @commands.Cog.listener()
    async def on_message(self,ctx: typing.Union[discord.User, str]):

        if ctx.author == self.bot.user:

            return

        mentionbot = f'<@!{self.bot.user.id}>'

        if ctx.content.startswith(mentionbot):

            embed = discord.Embed(

                title="The command prefix for this server is:",
                description=f'`{get_prefix(self.bot, ctx)}`',
                colour=0x33e18d

            )

            await ctx.channel.send(embed= embed)

        if str(ctx.guild.id) == "755777991681900585":

            if 'graeme' in ctx.content.lower():

                await ctx.channel.send('😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴😴')


        if 'pog' in ctx.content.lower():
            await ctx.add_reaction("<:pogchamp:745758557202415669>")

        if 'chungus' in ctx.content.lower() or 'reddit' in ctx.content.lower() or 'minecraft good' in ctx.content.lower() or 'fortnite bad' in ctx.content.lower():

            emotes = [

                "<:silver:795647527428423701>",
                "<:gold:795647527160250388>",
                "<:platinum:795647527285293087>",
                "<:F_:795647528120352808>",
                "<:wholesome:795647526833225748>",
                "<:lawyerup:795647527813906483>",
                "<a:bravo:795647525385404428>",
                "<:takemyenergy:795647527772749824>",
                "<:wholesomeapproval:795647528530870302>",
                "<:helpful:795647527655178292>",
                "<:deceased:795647525720817665>",
                "<a:takemypower:795647528494039060>",
                "<:mindblown:795647527721369611>",
                "<:hugz:795647527827144765>",
                "<a:tableslap:795647529680502796>"

            ]

            for emote in emotes:

                await ctx.add_reaction(emote)
                await asyncio.sleep(2)

        if 'awesome' in ctx.content.lower():

            await ctx.add_reaction("<:mario:792394134035103775>")

        if 'gay' in ctx.content.lower():

            await ctx.add_reaction("🏳️‍🌈")

        if 'france' in ctx.content.lower() or 'french' in ctx.content.lower():

            await ctx.add_reaction("<:fry:792524111136948245>")

        if 'kekw' in ctx.content.lower():

            await ctx.add_reaction("<:kekw:795646369091420210>")

        if 'lul' in ctx.content.lower():

            await ctx.add_reaction("<:LUL:795646637199327255>")

        if 'monkas' in ctx.content.lower():

            await ctx.add_reaction("<:monkaS:795646132747108362>")

        if 'haha' in ctx.content.lower():

            await ctx.add_reaction("<:pepelaugh:795647159613521941>")
        
        if 'pepega' in ctx.content.lower():

            if ctx.channel.id == 775030587131691019:
                return

            await ctx.add_reaction("<:pepega:795653356827050014>")

        


def setup(bot):
    bot.add_cog(Events(bot))