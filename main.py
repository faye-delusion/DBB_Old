import discord
import os
import meta
import asyncio
import json
import datetime
from datetime import date
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()

runInTestVersion = input("Do you wish to run in testing mode? [Leave blank for No]\t")

if len(runInTestVersion) == 0:
    runInTestVersion = None

if runInTestVersion != None:

    token = os.getenv('DISCORD_TESTING_TOKEN')
    print("Running in testing mode..")

else:
    
    token = os.getenv('DISCORD_AUTH_TOKEN')
    print("Running normally..")



# Function locates guild prefix from json file
def get_prefix(bot, message):

    # Opens prefixes.json file and writes contents to prefixes list
    with open('./config/prefixes.json','r') as f:
        prefixes = json.load(f)

    # Returns item from prefixes list with the index of the guild id
    return prefixes[str(message.guild.id)]



bot = commands.Bot(command_prefix=get_prefix, help_command=None, case_insensitive=True)



@bot.event
async def on_ready():

    # Loads all extensions
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} extension loaded.')

    # Startup Confirmation
    print(
        f'Dick and Balls bot Version {meta.version}.\n'
        f'Written by Dolph.\n'
        '{0.user} logged on successfully'.format(bot)
    )

    restartConfirmation = discord.Embed(

        title="⚠️Bot Restarted",
        colour=0xffff00

    )

    restartConfirmation.timestamp = datetime.datetime.now()

    loggingChannel = bot.get_guild(612486154440146944).get_channel(792775145865084948)

    await loggingChannel.send(embed=restartConfirmation)



@bot.event
async def on_guild_join(guild: discord.Guild):

    join_leave_logs = bot.get_channel(805130159795601408)

    join = discord.Embed(

        title="Joined Guild:",
        description=f'{guild.name}',
        colour=0x00ff00

    )

    join.add_field(

        name="Guild Members:",
        value=f'`{guild.member_count}`',
        inline=True

    )

    join.set_thumbnail(url=guild.icon_url)

    await join_leave_logs.send(embed=join)

    # Prints join message to console
    print(f'Joined guild {guild}')

    with open('./config/settings.json','r') as f:
        settings = json.load(f)

    default_prefix = settings['default_prefix']

    # Opens prefixes.json file and writes it to prefixes list
    with open('./config/prefixes.json','r') as f:
        prefixes = json.load(f)

    # Sets default prefix for guild
    prefixes[str(guild.id)] = default_prefix

    # Writes guild's new default prefix to prefixes.json file
    with open('./config/prefixes.json','w') as f:

        json.dump(prefixes,f,indent=4)
        print(f"Added {default_prefix} prefix for new guild {guild}({guild.id})")

    cwd= os.getcwd()

    pathToGuildData = os.path.join(f'{cwd}/guildData/', str(guild.id))

    print(pathToGuildData)

    if os.path.exists(pathToGuildData) == False:
        
        try:
            
            os.mkdir(pathToGuildData)

        except:

            print('didnt work')

        else:

            print('worked')

    else:

        print('path already exists, skipping..')
    


@bot.event
async def on_guild_remove(guild: discord.Guild):

    join_leave_logs = bot.get_channel(805130159795601408)

    leave = discord.Embed(

        title="Left Guild:",
        description=f'{guild.name}',
        colour=0xff0000

    )

    leave.add_field(

        name="Guild Members:",
        value=f'`{guild.member_count}`',
        inline=True

    )

    leave.set_thumbnail(url=guild.icon_url)

    await join_leave_logs.send(embed=leave)


    # Prints leave message to console
    print(f'Left guild {guild}({guild.id})')



@bot.command()
async def help(ctx):

    embed=discord.Embed(
        
        title="Dick and Balls Bot Information & Help", 
        color=0x00ff00
        
    )

    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(text="Everything about this bot was a mistake.")

    embed.add_field(

        name="Information",
        value=f"""
        Command Prefix: `{get_prefix(bot,ctx)}`
        Creator: <@265152100575477760>
        Current bot latency: `{round(bot.latency*1000)}ms`
        Bot version: `{meta.version}`
        """,
        inline=False

    )

    embed.add_field(

        name="Meta Commands",
        value=f"""

        `whois` - Displays information about a user.
        `ping` - Returns the bot's ping (Response time).
        `info` - Sends information about the bot.
        `help` - Displays this message.
        `foo` - Returns `bar`. That's it.
        `invite` - Sends a link to invite Dick and Balls Bot to your own server.
        `prefix` - Update the command prefix for the specified guild.
        `bug` - Report any bugs or issues you encounter with the bot.
        `feature` - Submit feature requests to me to add to the bot.
        
        """,
        inline=False

    )

    embed.add_field(

        name="Fun Commands",
        value=f"""

        `percentage` - Displays a randomised percentage for specified trait.
        `poll` - Create a poll which users can vote upon.
        `rate` - Provides a randomised rating for anything user has inputted, or just for the user if left blank.
        `8ball` - Returns a prediction to a provided stimulus.
        `mentalage` - Determines a mental age for the user. 
        `choose` - Bot chooses between provided objects.
        `quote` - Returns a random saved quote from a file. Can write new quotes with `quote add [quote]`, and can search quotes by id with `quote index [id]`.
        `wyr` - Sends a would you rather question into the chat. Custom scenarios can be added with `wyr add [scenario]`.
        `ship` - Sends a compatability rating for 2 provided people or objects.
        `kiss` - Kiss a user or object of your choice.
        `kill` - Kill a user in whichever way you desire.
        `punch` - Punch any user you want.

        """,
        inline=False

    )

    embed.add_field(

        name="Voice Commands",
        value=f"""

        `join` - Joins your voice channel. That's it.
        `leave` - Leaves current voice channel. Nice.
        `fart` - Plays a fart sound in the voice channel.
        `bruh` - Plays the bruh sound effect.

        """,
        inline=False

    )

    embed.add_field(

        name="Invite Dick and Balls Bot!",
        value="Want Dick and Balls Bot in your own server? Click [here](https://discord.com/api/oauth2/authorize?client_id=659540200053276685&permissions=8&scope=bot)!",
        inline=True

    )

    await ctx.send(embed= embed)



@bot.command()
@commands.is_owner()
async def reload(ctx, extension):

    if extension != "list":

        if len(extension) <1:

            # Logs lack of specified extension
            print('No cog selected.')
            await ctx.send("Enter a cog to reload.")

        else:

            try:

                f=open(f"./cogs/{extension}.py")

            except:

                await ctx.send(f'Cog `{extension}` not found')

            finally:

                f.close()

            # Reloads specified extension
            bot.unload_extension(f'cogs.{extension}')
            await asyncio.sleep(0.5)
            bot.load_extension(f'cogs.{extension}')

            await ctx.send(f'Reloaded cog `{extension}`.')

            # Logs in CMD
            print(f'`{extension}` cog reloaded')

    else:

        list = os.listdir("./cogs")

        outputlist = []

        for item in list:
            
            outputlist.append(item.replace('.py', ''))

        output = '{}'.format('\n'.join(outputlist[:-3]))

        embed = discord.Embed(

            title= "Cogs list:",
            description= output,
            colour= 0x33e18d

        )

        await ctx.send(embed= embed)

@commands.command()
@commands.is_owner()
async def load(ctx,extension):

    if len(extension) <1:

        # Logs lack of specified extension
        print('No cog selected.')
        await ctx.send("Enter a cog to reload.")

    else:

        try:

            f=open(f"./cogs/{extension}.py")

        except:

            await ctx.send(f'Cog `{extension}` not found')

        else:

            f.close()

            bot.load_extension(f'cogs.{extension}')

            await ctx.send(f'`{extension}` cog loaded')


@commands.command()
@commands.is_owner()
async def unload(ctx,extension):

    if len(extension) <1:

        # Logs lack of specified extension
        print('No cog selected.')
        await ctx.send("Enter a cog to reload.")

    else:

        try:

            f=open(f"./cogs/{extension}.py")

        except:

            await ctx.send(f'Cog `{extension}` not found')

        else:

            f.close()

            bot.unload_extension(f'cogs.{extension}')

            await ctx.send(f'`{extension}` cog loaded')



@bot.command()
async def ping(ctx):
    embedvar=discord.Embed(title=f":signal_strength: Ping: {round(bot.latency * 1000)}ms", color=0x00eeff)
    await ctx.send(embed=embedvar)



@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx,prefix = None):

    # Opens prefixes.json file and writes it to prefixes list
        
    with open('./config/prefixes.json','r') as f:
        prefixes = json.load(f)

    # Check for prefix
    # If no prefix present
    if prefix == None:

        # Send error to user
        await ctx.send(f'The command prefix for this server is: `{prefixes[str(ctx.guild.id)]}`')

    # If prefix is present
    else:

        # Sets guild prefix to inputted prefix variable
        prefixes[str(ctx.guild.id)] = prefix

        # Writes changes to prefixes.json file
        with open('./config/prefixes.json','w') as f:

            json.dump(prefixes,f,indent=4)

        # Sends output message to console and user
        print(f'Updated prefix in guild {ctx.guild}({ctx.guild.id}) to "{prefix}"')

        embed = discord.Embed(

            title="Prefix updated.",
            description=f"The new prefix for {ctx.guild} is `{prefix}`",
            colour=0x33e18d

        )
        await ctx.send(embed= embed)



@bot.command()
async def info(ctx):
    embedvar=discord.Embed(color=0x00eeff)
    embedvar.set_author(name=f"Dick and Balls Bot")
    embedvar.add_field(
        name="\n:information_source: Information",
        value=f"Version **{meta.version}**\nRunning Discord.py API Version **{discord.__version__}**\nFor a full list of commands, say `>help`\n ", inline=True
    )
    await ctx.send(embed=embedvar)



@bot.event
async def on_command_completion(ctx):

    dbbLogChannel = bot.get_guild(612486154440146944).get_channel(792775145865084948)

    loginfo = discord.Embed(

        title=f"`{ctx.command.name}` Command successfully executed.",
        description=ctx.message.content,
        colour=0x00ff00

    )

    loginfo.add_field(

        name="User:",
        value=ctx.author,
        inline=True

    )

    loginfo.add_field(

        name="User ID:",
        value=ctx.author.id,
        inline=True

    )

    loginfo.add_field(

        name="Channel:",
        value=ctx.channel.name,
        inline=True

    )

    loginfo.add_field(

        name="Channel ID:",
        value=ctx.channel.id,
        inline=True

    )

    loginfo.add_field(

        name="Guild:",
        value=ctx.guild.name,
        inline=True

    )

    loginfo.add_field(

        name="Guild ID:",
        value=ctx.guild.id,
        inline=True

    )

    loginfo.timestamp = datetime.datetime.now()

    await dbbLogChannel.send(embed=loginfo)


    print(f'{ctx.command.name} command called successfully by {ctx.author}({ctx.author.id}) in guild: {ctx.guild}({ctx.guild.id})')

@bot.event
async def on_command_error(ctx, exception):

    if 'missing' in str(exception) and 'permission(s)' in str(exception) or str(exception) == 'You do not own this bot.':

        channel = ctx.channel

        await ctx.message.delete()

        return await channel.send(embed=discord.Embed(title="You dont have permission to use that command!",colour=0xff0000))


    dbbLogChannel = bot.get_guild(612486154440146944).get_channel(792775145865084948)

    loginfo = discord.Embed(

        title=f"Command failed to execute.",
        description=ctx.message.content,
        colour=0xff0000
        
    )

    loginfo.add_field(

        name="User:",
        value=ctx.author,
        inline=True

    )

    loginfo.add_field(

        name="User ID:",
        value=ctx.author.id,
        inline=True

    )

    loginfo.add_field(

        name="Channel:",
        value=ctx.channel.name,
        inline=True

    )

    loginfo.add_field(

        name="Channel ID:",
        value=ctx.channel.id,
        inline=True

    )

    loginfo.add_field(

        name="Guild:",
        value=ctx.guild.name,
        inline=True

    )

    loginfo.add_field(

        name="Guild ID:",
        value=ctx.guild.id,
        inline=True

    )

    loginfo.add_field(

        name="Error Information",
        value=f"```{exception}```",
        inline=False

    )

    

    if 'Command' in str(exception) and 'not found' in str(exception):

        pass

    else:

        await dbbLogChannel.send(embed=loginfo)

        await ctx.send(embed=discord.Embed(title="Something went wrong", description="Error information has been sent to the dumbass who wrote me.", colour=0xff0000).add_field(name="Exception:",value=f'```{exception}```'))

        await ctx.message.delete()


bot.run(token)