from pypresence import Presence
import time
import random as r

client_id = "537325185242497036"

RPC = Presence(client_id=client_id)
RPC.connect()
start = time.time().__round__()
RPC.update(start=start)

maps = ('KOTH Redirect','CP Metalworks','CP Process','CTF 2Fort','CP \"Maze\"')
classes = ('Drunk scottish boye','Turtle','haha pootis lol','Pocket med trap gf','Hardest class haHAA','Very fast boye from Boston','Jarman','горшок(жив)','Butterknife weilding baguette','a fucking fish.')
gamemodes = ('Epic 1v1','Super Competitive 4v4','Competitive 6v6','Less Competitive 7v7','9v9 is a fucking joke','Casual')

while True:
    c = r.randint(1,10) #CLASS
    m = r.randint(1,5) #MAP
    g = r.randint(0,len(gamemodes)-1) #GAMEMODE (DETAILS)

    k = r.randint(-1,35) #KILLS
    if k > 0:
        d = r.randint(0,int(100*1/k)) #DEATHS (IF KILLS > 0)
    else:
        d = r.randint(10,50) #DEATHS (IF KILLS <= 0)
    a = r.randint(0,12) #ASSISTS

    print('Rich Presence State Updated!',c,m,g,k,d,a)
    RPC.update(large_image="map"+str(m), large_text=maps[m-1],
                small_image="c"+str(c), small_text=classes[c-1],
                details=gamemodes[g], state=str(k)+'/'+str(d)+'/'+str(a))
    time.sleep(r.randint(15,180))
