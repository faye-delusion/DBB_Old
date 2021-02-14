import discord
import os
import ast
import random
from discord.ext import commands, tasks
import math
import asyncio

white = 0xfefefe

class Admin(commands.Cog):

    def __init__(self,bot):
        self.bot= bot
        self.cyclestatus.start()

    def cog_unload(self):
        self.cyclestatus.cancel()

    @tasks.loop(minutes=2)
    async def cyclestatus(self):

        with open('./config/statuses.txt','r') as f:

            statuses = f.readlines()

        rstatus = random.randint(0,len(statuses))

        status = statuses[rstatus-1]

        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=f"{status}"))

        print(f'status updated to {status}')

    @commands.command()
    @commands.is_owner()
    async def adminhelp(self,ctx):

        embed = discord.Embed(

            title= f"Admin commands",
            description="""
            
            `listguilds` - Generate a list of all guilds the bot is in.
            `reload` - Reloads specified cog. For debugging purposes.
            `getemote` - Displays detailed information about a specified emote.
            `msgguild` - Sends a message to the general chat of any specified guild which the bot is in.
	        `newstatus` - Adds a new status to the bot's cycle.

            """,
            colour=white
            
        )

        await ctx.send(embed= embed)


    @commands.command(pass_context=True)
    @commands.is_owner()
    async def listguilds(self,ctx):

        l = []

        for guild in self.bot.guilds:

            l.append(f'**{guild}** ({guild.id})')

        embed = discord.Embed(

            title= f"Guilds ({len(l)})",
            description='{}'.format('\n'.join(l)),
            colour=0xffffff

        )

        await ctx.send(embed= embed)


    @commands.command()
    @commands.is_owner()
    async def getemote(self,ctx,emotename):

        try:
            
            for emote in ctx.guild.emojis:

                if emote.name == emotename:
                    
                    embed = discord.Embed(

                        title=str(emote),
                        colour=white

                    )

                    embed.add_field(name="Emote name", value=emote.name, inline=True)
                    embed.add_field(name="ID",value=str(emote.id),inline=True)
                    embed.add_field(name="Embed code",value=f'\{emote}',inline=True)

                    

        except:

            await ctx.send(f'No emote {emotename} found.')

        else:

            await ctx.send(embed= embed)
        

    @commands.command()
    @commands.is_owner()
    async def msgguild(self,ctx,guilddest: str,*message):

        for guild in self.bot.guilds:

            print(guild.id)

            if str(guild.id) == guilddest:

                print("guild found")
                for channel in guild.channels:

                    if channel.name == 'general':

                        await guild.text_channels[int(channel.position)].send('{}'.format(' '.join(message)))
                        break

        await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def reloadall(self,ctx):

        l = []

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.unload_extension(f'cogs.{filename[:-3]}')
                self.bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'{filename} extension reloaded.')
                l.append(filename[:-3])
                

        await ctx.send(embed=discord.Embed(title='__Extensions Reloaded:__',description='{}'.format('\n'.join(l)),colour=white))

    @commands.command()
    @commands.is_owner()
    async def newstatus(self,ctx,*status):

        status = '{}'.format(' '.join(status))

        with open('./config/statuses.txt', 'a') as f:

            f.write(f'\n{status}')

        print(f'Added new status `{status}` to file.')
        out = await ctx.send(f'Added new status `{status}` to file.')
        await asyncio.sleep(0.5)
        await out.delete()

    @commands.command()
    @commands.is_owner()
    async def listcogs(self,ctx):

        l = []

        for filename in os.listdir('./cogs'):

            if filename.endswith('.py'):

                l.append(filename[:-3])

        await ctx.send(embed=discord.Embed(title="__Cogs:__",description="{}".format('\n'.join(l)), colour=white))

def setup(bot):
    bot.add_cog(Admin(bot))