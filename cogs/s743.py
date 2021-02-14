import discord
from discord.ext import commands, tasks
import random
import os

class S743(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.gandhi.start()

    def cog_unload(self):
        self.gandhi.stop()

    

    @tasks.loop(hours=48.0)
    async def gandhi(self):

        channel = self.bot.get_channel(748264375332372544)

        pictures = [f for f in os.listdir('./custom/server743/')]

        choice = random.choice(pictures)

        fl, exten = os.path.splitext(choice)

        print(fl)
        print(exten)

        try:

            with open(f'./custom/server743/{choice}', 'rb') as f:

                file= discord.File(f, f'gandhi.{exten}')

                output = await channel.send(file= file)

        except Exception:

            print(Exception)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def togglegandhi(self,ctx,toggle):

        pos = ['yes','on','y','enable','enabled']
        neg = ['no','off','n','disable','disabled']

        if toggle.casefold() in pos:

            self.gandhi.start()
            await ctx.send('gandhi is now on')

        elif toggle.casefold() in neg:

            self.gandhi.stop()
            await ctx.send('gandhi is off')

        else:

            await ctx.send(f"invalid input. accepted inputs:\n{pos}\n{neg}")

        

def setup(bot):
    bot.add_cog(S743(bot))