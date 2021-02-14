import ast
import discord
import os
import datetime
import asyncio
import tracemalloc
import io
import textwrap
import contextlib

from discord.ext import commands


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class Evaluate(commands.Cog):

    def __init__(self,bot):
        self.bot=bot
    

    @commands.command(aliases=['eval','evaluate'])
    @commands.is_owner()
    async def eval_fn(self,ctx, *, cmd):

        fn_name = "_eval_expr"

        cmd = cmd.strip('` ')

        # add a layer of indentation
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
        

        # wrap in async def body
        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            'os': os,
            'asyncio': asyncio,
            '__import__': __import__
        }
        

        try:
            
            exec(compile(parsed, filename="<ast>", mode="exec"), env)
            result = (await eval(f"{fn_name}()", env))

        except Exception as exc:

            outputEmbed = discord.Embed(
                
                title='Dumbass.', 
                description="You're an idiot.", 
                colour=0xff0000
                
            )

            outputEmbed.add_field(
                
                name="__Input:__", 
                value= f'''```py\n{textwrap.dedent(cmd)}```''',
                inline=False)

            outputEmbed.add_field(name="__Exception:__",value=f"```{exc}```",inline=False)

            await ctx.send(embed=outputEmbed)
            with open('evalOutput.txt', 'w') as f:
                f.write(cmd)

        finally:

            await ctx.message.delete()


        


def setup(bot):
    bot.add_cog(Evaluate(bot))