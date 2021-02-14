import discord
from discord.ext import commands,tasks
from discord import FFmpegPCMAudio
import asyncio

class voice(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def join(self,ctx):

        channel = ctx.message.author.voice.channel

        if not channel:

            await ctx.send('Join a voice channel dumbass')
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():

            if voice.channel == channel:

                await ctx.send(embed=discord.Embed(title="You are already in a call with me dumbass",colour=0xffff00))

            else:

                await voice.move_to(channel)

                await ctx.send(embed=discord.Embed(title=f"Moved to {channel}.", colour=0xffff00))

        else:

            async with ctx.channel.typing():

                await channel.connect(reconnect=True)

                await ctx.send(embed=discord.Embed(title=f"Joined voice channel {channel}.",colour=0x00ff00))
        
        await ctx.message.delete()

    @commands.command(aliases=['dc','fuckoff'])
    async def leave(self,ctx):

        voicestate = ctx.author.voice

        if voicestate is None:

            return await ctx.send(embed=discord.Embed(title='You are not in a voice channel dumbass',colour=0xffff00))

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected:

            await voice.disconnect()

        else:

            await ctx.send(embed=discord.Embed(title="Not connected to a voice channel", colour=0xffff00))

    @commands.command()
    async def bruh(self,ctx):

        voicestate = ctx.author.voice

        if voicestate is None:

            return await ctx.send(embed=discord.Embed(title='You are not in a voice channel dumbass',colour=0xffff00))


        channel = ctx.message.author.voice.channel

        if not channel:

            await ctx.send('Join a voice channel dumbass')
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        source = FFmpegPCMAudio('./sounds/BruhSoundEffect2.mp3')

        await ctx.message.delete()
        conf = await ctx.send(embed=discord.Embed(title=f"Bruhing in {channel}.",colour=0x00ff00))

        player = voice.play(source)

        await asyncio.sleep(8.0)

        await conf.delete()

    @commands.command()
    async def fart(self,ctx):

        voicestate = ctx.author.voice

        if voicestate is None:

            return await ctx.send(embed=discord.Embed(title='You are not in a voice channel dumbass',colour=0xffff00))


        channel = ctx.message.author.voice.channel

        if not channel:

            await ctx.send('Join a voice channel dumbass')
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        source = FFmpegPCMAudio('./sounds/Fart.mp3')

        await ctx.message.delete()
        conf = await ctx.send(embed=discord.Embed(title=f'Farting in {channel}.', colour=0x00ff00))

        player = voice.play(source)

        await asyncio.sleep(8.0)

        await conf.delete()
        




def setup(bot):
    bot.add_cog(voice(bot))