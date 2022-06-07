
"""
Time to take a break fr.
Time: 3 days no rest
progress: full working (with several bugs not found prolly)
this took me so long, this file in total of almost 200 (207 with 8kb in size)values.py with 2kb (67 lines) commonfunction.py 1kb with 43 lines
"""

#https://stackoverflow.com/questions/66662756/is-it-possible-to-split-a-discord-py-bot-across-multiple-files
#main entry files for the entire bot
import discord
from discord.ext import commands
import sys
#replit
#sys.path.append("/home/runner/Stuffbhailegit")
#termux
sys.path.append("/data/data/com.termux/files/home/breadbot_major_little_rewrite")
import main
import logging as log
import typing

#replit
#sys.path.append("/home/runner/Stuffbhailegit/commonlib")
#termux
sys.path.append("/data/data/com.termux/files/home/breadbot_major_little_rewrite/commonlib")
import values
from discord import Color as color
import random
import commonfunction as lib

logger = log.getLogger(__name__)
#todo: move embeds setup to values.py
embedhelp = discord.Embed(title=values.EmbedHelp.title,
                          description=values.EmbedHelp.description,
                          color=color.red())
embedhelp.add_field(name=values.EmbedHelp.field1name,
                    value=values.EmbedHelp.field1value,
                    inline=True)
embedhelp.add_field(name=values.EmbedHelp.field2name,
                    value=values.EmbedHelp.field2value,
                    inline=True)
embedhelp.add_field(name=values.EmbedHelp.field3name,
                    value=values.EmbedHelp.field3value,
                    inline=True)
embedhelp.set_footer(
    text=f"{values.EmbedHelp.noprefixchange} | v{values.EmbedHelp.botversion}")
#embedhelp.add_field(name=values.EmbedHelp.noprefixchange, value="", inline=False)


class cmd(commands.Cog):
  def __init__(self, client):
      self.client = client
     
      #spent 2 days on this shit, the reason is the @decorator (@commands.Cog.listener) l used cogs INCORRECTLY making it doesnt register the fucking command error event
      #@client.event
      async def on_command_error(ctx,error):
          commandnotfound=commands.CommandNotFound
          if isinstance(error, commands.MissingRequiredArgument):
               embed=discord.Embed(title="Invalid usage", description=values.Common.cantbeempty, color=color.red())
               await ctx.send(embed=embed)
          elif isinstance(error, commandnotfound):
               #pass #pass to do nothing
               await ctx.send("Command not found.")

def searchusage(commandname):
    #look up in values.py
    isCommand_available = str(commandname) in values.BotStuff.command_list
    #return format is [bool_isAvailable, about, usage, new: alias)
    if isCommand_available == True:
        about = values.HelpUsage.usagelist[f"{str(commandname)}_about"]
        usage = values.HelpUsage.usagelist[f"{str(commandname)}_usage"]
        #any alias?
        if f"{str(commandname)}_aliases" not in values.HelpUsage.usagelist:
            aliases="(No aliases provided)"
        else:
            aliases=values.HelpUsage.usagelist[f"{str(commandname)}_aliases"]
        returnform = [isCommand_available, about, usage, aliases]
        return returnform
    else:
        about = None
        usage = None
        returnform = [isCommand_available, about, usage]
        return returnform


def createembedbase(title, desc, color):
    embedbase = discord.Embed(title=title, description=desc, color=color)
    return embedbase


@commands.command()
async def ping(ctx):
    pongmsg = await ctx.send("Pong! Checking latency")
    ping = round(main.client.latency * 1000)
    await pongmsg.edit(content=f"Pong! Latency: {ping}ms (my internet moment)")
    logger.info(f"Bot latency is: {ping}ms")


@commands.command()
async def help(ctx):
    await ctx.send(embed=embedhelp)


@commands.command()
async def setactivity(ctx, activity):
        str_successactivitychange = values.Common.successfullychangedbot + str(
            activity) + "!"
        embedsuccessact = discord.Embed(title=values.Common.success,
                                        description=str_successactivitychange)
        main.presence = str(activity)
        logger.info("Changed activity to " + str(activity))
        await ctx.send(embed=embedsuccessact)


@commands.command()
async def usage(ctx, commandname):
    looktable = searchusage(commandname)
    if looktable[0]:
        embed = createembedbase(f"About: {looktable[1]}",
                                f"Usage: {looktable[2]}", color.red())
        embed.add_field(name="Aliases", value=f"Aliases: {looktable[3]}")
        embed.set_footer(text="Aliases does not support usage yet!")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Command {commandname} is not available!")
        

@commands.command(aliases=["8ball"])
async def eightball(ctx, *, question):
    answer = random.choice(values.Fun.eightball_answerlist)
    embed = createembedbase("8ball", f"Q: {question}\n:8ball:: {answer}",color.dark_gray())
    await ctx.send(embed=embed)

@commands.command()
async def memes(ctx):
    #search for a meme source and then construct to a embed
    base = lib.get_subreddit("memes", "new", 100, "hours")
    #data=lib.construct_redditjson(base[1])
    if base[0] == True:  #if r/memes data gathering is true
        data = lib.construct_redditjson(base[1])
        result = data
        embed = discord.Embed(title=result["title"],
                              description=result["selftext"],
                              color=color.red(),
                              inline=False)
        embed.set_image(url=result["url"])
        embed.set_author(name=result["subreddit"])
        upvote = f"👍 {result['upvote']} • 👎 {result['downvote']}"
        embed.set_footer(text=upvote)
        await ctx.send(embed=embed)
    else:
        await ctx.send(
            "Failed to gather data from r/memes, it is maybe caused by wrong configuration or blocked access."
        )

#subreddit getter
@commands.command(aliases=["reddit"])
async def subreddit(ctx,subreddit):
   base = lib.get_subreddit(str(subreddit), "new", 100, "hours")
   if base[0]:
       data=lib.construct_redditjson(base[1])
       print(data["url"])
       nsfw_content_notallowed=discord.Embed(title=data["subreddit"]+" (NSFW)",description="This content is NSFW (Not Safe For Work/18+), you can only do this in an NSFW channel.", color=color.red())
       if data["isnsfw"] == True and not ctx.channel.is_nsfw():
           await ctx.send(embed=nsfw_content_notallowed)
       elif data["isnsfw"] == True and ctx.channel.is_nsfw(): #i believe nsfw post or amything like memes is only url no selftext, though im still to recommend no matter what print selftext in the embed.
           embed=discord.Embed(title=data["title"]+" (NSFW)", description=data["selftext"], color=color.red())
           embed.set_image(url=url["url"])
           embed.set_author(name=data["subreddit"])
           ctx.send(embed=embed)
       elif data["isnsfw"] == False and not data["selftext"]: #url only
           embed=discord.Embed(title=data["title"], description=data["selftext"], color=color.red())
           embed.set_image(url=data["url"])
           embed.set_author(name=data["subreddit"])
           await ctx.send(embed=embed)
       elif data["isnsfw"] == False and data["selftext"] is not False: #selftext only 
           embed=discord.Embed(title=data["title"], description=data["selftext"], color=color.red())
           embed.set_author(name=data["subreddit"])
           await ctx.send(embed=embed)
       
   else:
   	    await ctx.send("Cannot get the desired information! This error is common")

@commands.has_permissions(kick_members=True)
@commands.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
       if reason is None:
            reason="No reason provided" 
       if member.top_role > ctx.author.top_role:
            await ctx.send(f"{member} is higher than you!")
            #await ctx.send(f"target role pos: {member.top_role.position} ctx.author: {ctx.author.top_role.position}")
       elif member==ctx.author:
           await ctx.send("You trying to kick yourself? Being an idiot or something...")
       else:
            embed=discord.Embed(title=values.Common.success, description=f"{member} has been kicked beacuse of: {reason}",color=color.red())
            await ctx.guild.kick(member)
            await ctx.send(embed=embed)
    except discord.Forbidden: #discord.Forbidden means not allowed stuff
         await ctx.send("I'm not allowed to do that! Move me higher up on the role hierarchy.")



#local badargument kick error handler
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Member not found")

@commands.command()
async def prefix(ctx):
    embed=discord.Embed(title="Prefix", description="My default prefix is `^`", color=color.red())
    await ctx.send(embed=embed)

@commands.has_permissions(administrator=True)
@commands.command()
async def unban(ctx, member, reason=None):
    if reason == None:
        reason="No reason provided"
    banned_member=await ctx.guild.bans() #when nothing this nothing too
    member_name, member_discrim = member.split("#")

    if (member_name, member_discrim) not in banned_member or not banned_member:
            await ctx.send("Member not found")

    for ban_entry in banned_member:
        user=ban_entry.user     
        if (user.name, user.discriminator) == (member_name, member_discrim):
            embed=discord.Embed(title="Success!", description=f"Successfully unbanned {member_name}#{member_discrim} because: {reason}")
            await ctx.guild.unban(user)
            await ctx.send(embed=embed)

def setup(client):
    client.add_command(ping)
    client.add_command(help)
    client.add_command(setactivity)
    client.add_command(usage)
    client.add_command(eightball)
    client.add_command(memes)
    client.add_command(subreddit)
    client.add_command(kick)
    client.add_command(prefix)
    client.add_command(unban)
    client.add_cog(cmd(client))
