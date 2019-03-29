import valve.source.a2s

SERVER_ADDRESS = ("185.73.228.158",30219)

async def main(ctx):
    plrs = []
    
    info, players = checkStatus()
    
    msg = ""

    msg += "Aktualna mapa to: " + info["map"] + "\n"
    msg += "Aktualnie jest " + str(info["player_count"]) + " graczy: \n"

    for player in players:
        if player != "":
            plrs.append(player["name"])
    
    for player in plrs:
        msg += "    " + player["name"] + "\n"
        
    await ctx.send(msg)

def checkStatus():
    with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
        info = server.info()
        players = server.players()["players"]
    return(info, players)
