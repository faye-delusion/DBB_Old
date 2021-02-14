import discord
from discord.ext import commands,tasks

class Pepega(commands.Cog):

    def __init__(self,bot):
        self.bot= bot

    @commands.Cog.listener("on_message")
    async def pepega(self,ctx):

        if ctx.channel.id == 775030587131691019:

            if ctx.attachments:
                await ctx.add_reaction('✅')
                await ctx.add_reaction('❌')

    @commands.Cog.listener("on_raw_reaction_add")
    async def runMessageCheck(self,ctx):

        if ctx.channel_id == 775030587131691019:

            if ctx.user_id != 659540200053276685:

                if ctx.attachments:

                    if str(ctx.emoji) in ['✅', '❌']:

                        msg = ctx.message_id
                        print(msg)
                        print(ctx.emoji)

    @commands.command()
    async def dl(self,message):

        print()

        # if ctx.content.attachments:

        #     await ctx.save(ctx.content.attachments.filename)

        #     await ctx.send('saved')


def setup(bot):
    bot.add_cog(Pepega(bot))