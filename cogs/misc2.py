import discord
import random
from discord.ext import commands
import datetime
import typing
import asyncio
import os

class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self,ctx,*arg):

        message = '{}'.format(' '.join(arg))

        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self,ctx,user: discord.Member,*message):

        try:
            
            message = '{}'.format(' '.join(message))

            await user.send(message)

        except:

            conf = await ctx.send('Could not send DM to user')
            await conf.delete()

        else:

            confirmation = await ctx.send(f"{ctx.author.mention}, DM sent!")
            print(f"{ctx.author}({ctx.author.id}) sent dm `{message}` to {user}({user.id})")
            
            await ctx.message.delete()
            await asyncio.sleep(0.1)
            await confirmation.delete()

    @commands.command(invoke_without_command=True, aliases=['choice','decide'])
    async def choose(self,ctx,*choices: str):

        if len(choices) < 2:

            await ctx.send('You have to enter at least 2 choices dumbass')
        
        else:

            # Choose object
            decision = random.choice(choices)
            
            embed = discord.Embed(

                title='I have chosen...',
                description= decision,
                colour= 0x33e18d

            )

            
            embed.set_footer(text=f"Command called by {ctx.author.name}")
            embed.add_field(name='Potential choices:', value='{}'.format(', '.join(choices)),inline=True)

            await ctx.send(embed= embed)

    @commands.command()
    async def poll(self,ctx,*args):
        
        question = '{}'.format(' '.join(args))
        cdate = datetime.datetime.now().strftime("%a %d %b")

        embed = discord.Embed(

            title = "Poll",
            description = question,
            colour = 0x33e18d

        )

        embed.set_footer(text=f'Poll created by {ctx.author.name} on {str(cdate)}')

        poll = await ctx.send(embed= embed)

        await poll.add_reaction('👍')
        await poll.add_reaction('👎')
        
    @commands.command(aliases=['userinfo'])
    async def whois(self,ctx,member: discord.Member = None):

        if not member:

            member = ctx.author

        embed = discord.Embed(

            title = f"Information for {member}",
            colour = 0x33e18d
        
        )

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Command called by {ctx.author.name}")

        roles = [role for role in member.roles[1:]]

        embed.add_field(name='ID:', value = member.id)
        
        embed.add_field(name='Nickname:', value = member.display_name)

        embed.add_field(name='Account name:', value= member)

        embed.add_field(name='Account creation date:', value= member.created_at.strftime("%a %#d %B %Y, %I:%M%p UTC"))

        embed.add_field(name='Joined on:',value= member.joined_at.strftime("%a %#d %B %Y, %I:%M%p UTC"))

        embed.add_field(name='Roles:', value= "".join([role.mention for role in roles]))

        embed.add_field(name='Is bot:', value= member.bot)

        await ctx.send(embed= embed)

    @commands.command(aliases=['fact'])
    async def funfact(self,ctx,user = typing.Union[discord.Member,str]):

        if type(user) != discord.Member:

            user = ctx.author

        if os.path.exists(f'{os.getcwd}/guildData/{ctx.guild.id}/funFact/{user.id}.txt'):

            await ctx.send('yes')

        else:

            await ctx.send('no')



    @commands.command(aliases=['newfact'])
    async def newfunfact(self,ctx,user: typing.Union[discord.Member, str], *fact):

        # Runs if member is not specified in message
        if type(user) != discord.Member:

            funFact = '{} {}'.format(user, ' '.join(fact))

            user = ctx.author            

        # Runs if member is specified in message
        else:

            funFact = '{}'.format(' '.join(fact))

        # Gets the current working directory and writes path to guildData to pathToGuildData var
        cwd= os.getcwd()

        pathToGuildData = os.path.join(f'{cwd}/guildData/{ctx.guild.id}', "funFacts")

        # Runs if the guildData path does not exist
        if os.path.exists(pathToGuildData) == False:

            try:
                
                # Creates directory
                os.mkdir(pathToGuildData)

            except:

                # Error, something fucked up
                print(f'Could not create directory {pathToGuildData}')

            else:

                # Confirmation message
                print(f'{pathToGuildData} directory created!')

        # Write fun fact to file
        with open(f'./guildData/{ctx.guild.id}/funFacts/{user.id}.txt', 'a') as f:

            f.write(f'{funFact}\n')

    @commands.command(aliases=['dick','penis'])
    async def cock(self,ctx, member = None):

        if member == None:
            user = ctx.author.mention

        else:

            user = member

        length = random.randint(1,13)
        shaft = []

        for i in range(0,length):
            shaft.append('=')

        if length >= 6:
            color = 0x00ff00
            comment = 'Pretty big bud!'
        elif length <6 and length >=4:
            color = 0xffff00
            comment = "Umm.. I've seen worse."
        else:
            color = 0xff0000
            comment = "How???"


        output = discord.Embed(

            description=f"{user}'s cock is {length} inches long!",
            colour=color

        )

        output.add_field(name=comment, value='8{}D'.format(''.join(shaft)),inline=False)

        await ctx.send(embed=output)

        

def setup(bot):
    bot.add_cog(Random(bot))