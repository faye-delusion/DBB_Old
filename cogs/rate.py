import discord
import random
from discord.ext import commands

class Rating(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def rate(self,ctx,*object):

        r1comments = [

            "This is fucking vile.",
            "Yuck.",
            "Disgusting.",
            "🤢",
            "I don't think I've ever seen anything this horrible.",
            "Rancid. Absolutely Rancid.",
            "I wanna throw up."

        ]

        r2comments = [

            "Yeah, no thanks.",
            "It doesn't get much worse than you.",
            "Get away from me.",
            "It *could* be worse, I guess..",
            "Are you aware that you're this bad?"

        ]

        r3comments = [

            "It could be a lot worse, I'll give you that.",
            "If you tried harder, maybe things would be better.",
            "That's.. it?? It has to be better than that, cmon.",
            "Don't flatter yourself.",
            "You're nothing special, just saying."

        ]

        r4comments = [

            "Not terrible, but I wouldn't say good either.",
            "I'd say you're just below average.",
            "Not bad. Not bad.",
            "I don't mind it. It is what it is.",
            "Have you tried working out?"

        ]

        r5comments = [

            "You're about middle of the road.",
            "Not bad. Nice job.",
            "Nice.",
            "Very much average. But that's not a bad thing, right?",
            "Niiiiice."

        ]

        r6comments = [

            "Quite nice. I like this.",
            "It's good.",
            "Sick.",
            "This is good.",
            "Cool. Cool."

        ]

        r7comments = [

            "Metal.",
            "This is great.",
            "Oh my god, I love this!",
            "Something about you, man. Damnn.",
            "You real nice."

        ]

        r8comments = [

            "This is so fucking good, holy shit.",
            "Dude! WHAT!?",
            "This is sick as fuck!",
            "Damnnn.. aha.",
            "😏"

        ]

        r9comments = [

            "Damnnnnnnnnnnn.",
            "Who gave you permission to be this hot?",
            "You boutta make me act up.",
            "Who could possibly compare?",
            "Jesus Christ, you're almost as attractive as me."

        ]

        r10comments = [

            "You look fucking godly.",
            "Are you even sure you're human?!",
            "Holy shit it's so perfect.",
            "Jesus Christ my guy.",
            "DAMNNNNNNNNNNN."

        ]

        if len(object) >= 1:
            fullobject = '{}'.format(' '.join(object))
        else:
            object = None
        

        rating = random.randint(1,10)

        if rating >= 7: 
                
            color = 0x00ff00
            
        elif rating >= 4 and rating <=6: 
            
            color = 0xffff00

        else:

            color = 0xff0000

        if object != None:

            embed = discord.Embed(

                title=f"{ctx.author.name},",
                description=f"I rate **{fullobject}**.. {rating}/10",
                colour= color

            )

        else:

            embed = discord.Embed(

                title=f"{ctx.author.name}, I rate you..",
                description=f"{rating}/10",
                colour=color

            )

        if rating == 1:

            output = random.choice(r1comments)

        elif rating == 2:

            output = random.choice(r2comments)

        elif rating == 3:

            output = random.choice(r3comments)

        elif rating == 4:

            output = random.choice(r4comments)

        elif rating == 5:

            output = random.choice(r5comments)

        elif rating == 6:

            output = random.choice(r6comments)

        elif rating == 7:

            output = random.choice(r7comments)

        elif rating == 8:

            output = random.choice(r8comments)

        elif rating == 9:

            output = random.choice(r9comments)

        elif rating == 10:

            output = random.choice(r10comments)

        

        embed.add_field(name="Additional Comments:", value=output,inline=True)

        await ctx.send(embed= embed)

    # @commands.group(invoke_without_command=True)
    # async def rate(self,ctx):

    #     # Error message
    #     await ctx.send('What am I supposed to be rating? Cmon you cant just tell me to rate something and not tell me what that something is.')


    # @rate.command(aliases=['dick', 'penis'])
    # async def cock(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/cRatings.txt', 'r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

    # @rate.command(aliases=['titties','boobs'])
    # async def tits(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/tRatings.txt', 'r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

    # @rate.command(aliases=['butt','bum','arse'], case_insensitive=True)
    # async def ass(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/aRatings.txt', 'r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

    # @rate.command(case_insensitive=True)
    # async def feet(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/fRatings.txt', 'r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

    # @rate.command(aliases=['myself'])
    # async def me(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/mRatings.txt', 'r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

    # @rate.command(aliases=['vagina','fanny'])
    # async def pussy(self,ctx):

    #     # Generate rating
    #     rating = random.choice(open('./Ratings/pRatings.txt','r').readlines())

    #     # Send rating to user
    #     await ctx.send(rating)

        
def setup(bot):
    bot.add_cog(Rating(bot))