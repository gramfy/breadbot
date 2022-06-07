#All bot values used in commonlib

import discord
from discord.ext import commands

class value(commands.Cog):
    def __init__(self, client):
        self.client = client

        
####EMBED MESSAGE####

class BotStuff():
    command_list=["ping", "setactivity", "usage", "8ball", "memes", "subreddit","help","kick", "prefix"]
    bot_prefix="^"

class EmbedHelp():
    title="Help"
    description=f"Prefix:{BotStuff.bot_prefix}"
    field1name="🍞Common"
    field1value=f"`{BotStuff.bot_prefix}ping, {BotStuff.bot_prefix}setactivity, {BotStuff.bot_prefix}usage, {BotStuff.bot_prefix}prefix`"
    field2name="🎉Fun"
    field2value=f"`{BotStuff.bot_prefix}8ball, {BotStuff.bot_prefix}memes, {BotStuff.bot_prefix}reddit`"
    field3name="🔨Moderation (Later)"
    field3value=f"\u200b"
    field4name="🎧Music"
    field4value="`^join, ^leave`"
    
    noprefixchange="Prefix change are soon supported!"
    botversion="1.0.1"

####COMMON####
class Common():
    success = "Success!"
    successfullychangedbot = "Successfully changed the bot activity to "
    cantbeempty="Use `{BotStuff.bot_prefix}usage [commandname]` to see how to use it."

#HOW TO ADD COMMAND:
"""
go to the class HelpUsage below, in usagelist add your command like this
"yourcommandname_about":"about command",
"yourcommandname_usage":"usage of command",
make sure to add comma in the end of every line
now go to BotStuff class, and add your command like array there, simple
"""
class HelpUsage():
    usagelist={
        "setactivity_about":"Set the activity of the bot",
        "setactivity_usage":f'{BotStuff.bot_prefix} setactivity ["activity"]. \n Example: `{BotStuff.bot_prefix}setactivity "help me plzzz"`',
        "ping_about":"Get the bot latency",
        "ping_usage":"Basically ping.",
        "usage_about":"bro?",
        "usage_usage":"you use usage in a usage?",
        "8ball_about":"The 8ball",
        "8ball_usage":f"{BotStuff.bot_prefix}8ball [questions]",
        "memes_about":"Memes",
        "memes_usage":"source: ~~trust me~~ reddit",
        "subreddit_about":"Get random stuff from an subreddit",
        "subreddit_usage":f"`{BotStuff.bot_prefix}reddit [subredditname]`",
        "kick_about":"Kick a member",
        "kick_usage":f"`{BotStuff.bot_prefix}kick [member] [reason (optional)]`",
        "reddit_about":"Get an subreddit post.",
        "subreddit_usage":f"`{BotStuff.bot_prefix}subreddit [subreddit]`",
        "subreddit_aliases":f"`{BotStuff.bot_prefix}reddit`",
        "prefix_about":"Show the prefix of the bot or set it.",
        "prefix_about":f"`{BotStuff.bot_prefix}prefix [botprefix (optional)]`"
    }
    
class Fun():
    eightball_answerlist=[
    ###yes answer
    "Yes",
     "Probably yes",
     "It is a yes!",
     "I have no idea so i'll choose yes lol",
     "no but yes",
      ###neutral answer
      "Umm I dont know",
      "idk seriously dude dont ask me",
      "||ur gay|| idk basically",
      "legit i didnt care about your question",
      "didnt ask + ratio 😂🍞",
      ###no answer
      "no",
      "nope",
      "no obviously",
      "haha no",
      "no no no no no no no no no no no no no no"
    ]
    
def setup(client):
    client.add_cog(value(client))