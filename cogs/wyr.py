import discord
import os
from discord.ext import commands

import random

class WouldYouRather(commands.Cog):

    def __init__(self,bot):
        self.bot= bot

    @commands.group(invoke_without_command=True)
    async def wyr(self,ctx):

        questions = []

        with open("./config/wyrquestions.txt","r") as f:

            default = f.readlines()

            for i in default:

                questions.append(i)

            extQuestions = f"./guildData/{ctx.guild.id}/wyrquestions.txt"

            if os.path.exists(extQuestions):

                with open(extQuestions, "r") as f2:

                    ext = f2.readlines()
                    

                    for ii in ext:

                        questions.append(ii)

        print(questions)

        choice1 = random.choice(questions)

        choice2 = random.choice(questions)

        if choice2 == choice1:

            while choice2 == choice1:

                choice2 = random.choice(questions)

        embed = discord.Embed(

            title="Would you rather..",
            description=f"Command called by **{ctx.author}**",
            colour=0x33e18d

        )

        embed.add_field(name="🇦",value=choice1,inline=False)
        embed.add_field(name="__OR__",value="᲼᲼᲼᲼᲼᲼",inline=False)
        embed.add_field(name="🇧",value=choice2,inline=False)

        output = await ctx.send(embed= embed)

        await output.add_reaction("🇦")
        await output.add_reaction("🇧")

    @wyr.command()
    async def add(self,ctx,*message):

        if len(message) < 1:

            await ctx.send(embed=discord.Embed(title="WYR question has to be longer than that numb nuts", color=0xff0000))

        else:

            fm = '{}'.format(' '.join(message))

            with open(f"./guildData/{ctx.guild.id}/wyrquestions.txt","a") as f:

                f.write(f'{fm}\n')

            embed = discord.Embed(

                title="New WYR scenario added:",
                description=fm,
                colour=0x33e18d

            )

            await ctx.send(embed= embed)

def setup(bot):
    bot.add_cog(WouldYouRather(bot))