import discord
import logging as pylog
from discord.ext import commands
from discord.ext import tasks
import os
import keep_alive as web_data

log=pylog.getLogger(__name__)
pylog.basicConfig(level=pylog.INFO) #for discord logging
token = "OTM4NTk4NTIxMDcyOTM5MDg5.GIqchO.Es0GJxcwVOsjB-ge0lhdoJSxawkAtbrHr5ItdQ"
client  = commands.Bot(command_prefix=commands.when_mentioned_or("^"), help=None)
client.remove_command("help")
presence = "breadism"

@tasks.loop(seconds=5.0)
async def changepresence():
    clientactivity=discord.Activity(type=discord.ActivityType.watching, name=presence)
    await client.change_presence(activity=clientactivity, status=discord.Status.online)

@client.event
async def on_ready():
    log.info("Ready!")
    changepresence.start()
    #log.info("Current activity: ",presence)



#https://stackoverflow.com/questions/66662756/is-it-possible-to-split-a-discord-py-bot-across-multiple-files
client.load_extension("commonlib.cmd")
client.load_extension("commonlib.values")

web_data.keep_alive()

#sentpass=web_data.DataUpdate.password
#print(f"Password entered: {sentpass}")
    
client.run(token)
