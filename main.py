import discord
from discord.ext import commands
import os
import time
import asyncio

import cmds

global lastRun, mapChannel, playersChannel, updateChannel
lastRun = time.time()

Token = os.environ["TOKEN"]

bot = commands.Bot(command_prefix='s!')

@bot.command()
async def status(ctx):
    print("CMD: status")
    await cmds.status.main(ctx)

async def status_loop():
    while True:
        info, players = cmds.status.checkStatus()       
        print("LOOP: presence_update")
        game = discord.Game("aktualnie jest " + str(info["player_count"]) + " graczy")
        await bot.change_presence(status=discord.Status.online, activity=game)
        
        await mapChannel.edit(name="Mapa: " + info["map"])
        await playersChannel.edit(name="Ilosc graczy: " + str(info["player_count"]))
        await updateChannel.edit(name="Aktualizacja: " + str(time.localtime()[3]) + ":" + "{:0>2}".format(str(time.localtime()[4])))

        await asyncio.sleep(300)

@bot.event
async def on_ready():
    global mapChannel, playersChannel, updateChannel
    mapChannel = bot.guilds[0].get_channel(559785371655995404)
    playersChannel = bot.guilds[0].get_channel(559785423795257374)
    updateChannel = bot.guilds[0].get_channel(559788077367689271)
    print("FINISH: on_ready")
    bot.loop.create_task(status_loop())
    
bot.run(Token)
