from classes import *
from sprites import *
import copy

def moveroom():
    global chs,cvs,exits,bg,player1,vescroll,hoscroll
    wf = width/800
    hf = height/600
    e = can.gettags(player1.detect(can,"exit")[0])[2]
    d = exits[e]
    nbg = d[0]
    nex = d[1]
    can.delete("all")
    bg = copy.deepcopy(bgdic[nbg])
    exits = bg.pop()
    dimensions = bg.pop()
    hoscroll = (dimensions[0]-800)*wf
    vescroll = (dimensions[1]-600)*hf
    bg = group(can,bg)
    d = exits[nex]
    move = d[2]
    bg.move(can,move[0],move[1])
    bg.hvscale(can,wf,hf)
    player1.redraw(can,d[3][0]*wf,d[3][1]*hf)
    chs = -move[0]*wf
    cvs = -move[1]*hf

def resize(event):
    global width,height,hoscroll,vescroll,uwl,lwl,uvl,lvl,chs,cvs
    if width/event.width != 2.5 and height/event.height != 5:
        player1.hvscale(can,event.width/width,event.height/height)
        bg.hvscale(can,event.width/width,event.height/height)
        hoscroll *= event.width/width
        vescroll *= event.height/height
        uwl *= event.width/width
        lwl *= event.width/width
        uvl *= event.height/height
        lvl *= event.height/height
        chs *= event.width/width
        cvs *= event.height/height
        height = event.height
        width = event.width

def rotation():
    global player1,direction
    newdir = direction
    for i in [[1,0,0,0,0],[1,0,0,1,1],[0,0,0,1,2],[0,1,0,1,3],[0,1,0,0,4],[0,1,1,0,5],[0,0,1,0,6],[1,0,1,0,7]]:
        if keyset[0] == i[0] and keyset[1] == i[1] and keyset[2] == i[2] and keyset[3]== i[3]:
            newdir = i[4]
    player1.rotate(can,(newdir-direction)*45)
    direction = newdir

def startnewgame():
    bnewgame.destroy()
    bloadgame.destroy()
    bconfig.destroy()
    start()

def loadgame():
    print("not yet implemented")

def config():
    print("not yet implemented")

def mainmenu():
    global bnewgame,bloadgame,bconfig
    bnewgame = tkinter.Button(text="start game",command=startnewgame)
    bnewgame.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.2)
    bloadgame = tkinter.Button(text="load game",command=loadgame)
    bloadgame.place(relx=0.3,rely=0.35,relwidth=0.4,relheight=0.2)
    bconfig = tkinter.Button(text="options",command=loadgame)
    bconfig.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.2)


def start():
    global chs,cvs,exits,bg,player1,vescroll,hoscroll,can,keyset,direction,bgdic,uwl,lwl,uvl,lvl,speed
    speed = 7
    uwl = 320
    lwl = 280
    uvl = 420
    lvl = 380
    can = tkinter.Canvas()
    can.place(relx=0,rely=0,relwidth=1,relheight=1)
    keyset = [0,0,0,0,0,0,0,0,0]
    direction = 0
    bgdic = {"background1":background1,"background2":background2,"background3":background3}
    bg1 = copy.deepcopy(background1)
    exits = bg1.pop()
    dimensions = bg1.pop()
    bg = group(can,bg1)
    player1 = player(can,play1)
    hoscroll = dimensions[0]-800
    vescroll = dimensions[1]-600
    chs = 0
    cvs = 0
    player1.rotate(can,180)
    sword = item(can,copy.deepcopy(sword1))
    sword.move(can,300,300)
    bind()
    main()



def main():
    global chs,cvs,exits,bg,player1,vescroll,hoscroll
    if keyset[0] == 1:
        rotation()
        if player1.detect(can,"exit") != []:
           moveroom()
        elif cvs <= 0 or not(player1.hitbox[1].y<=uwl and player1.hitbox[1].y>=lwl):
             if player1.hitbox[0].y>=0:
                player1.move(can,0,-speed)
        else:
            for i in player1.hitbox:
                i.move(0,-speed)
            if player1.detect(can,"solid") == []:
                bg.move(can,0,speed)
                cvs -= speed
            for i in player1.hitbox:
                i.move(0,speed)
    if keyset[1] == 1:
        rotation()
        if player1.detect(can,"exit") != []:
           moveroom()
        elif cvs >= vescroll or not(player1.hitbox[1].y<=uwl and player1.hitbox[1].y>=lwl):
            if player1.hitbox[1].y<=height:
                player1.move(can,0,speed)
        else:
            for i in player1.hitbox:
                i.move(0,speed)
            if player1.detect(can,"solid") == []:
                bg.move(can,0,-speed)
                cvs += speed
            for i in player1.hitbox:
                i.move(0,-speed)
    if keyset[2] == 1:
        rotation()
        if player1.detect(can,"exit") != []:
           moveroom()
        elif chs <= 0 or not(player1.hitbox[1].x<=uvl and player1.hitbox[1].x>=lvl):
            if player1.hitbox[0].x>=0:
                player1.move(can,-speed,0)
        else:
            for i in player1.hitbox:
                i.move(-speed,0)
            if player1.detect(can,"solid") == []:
                bg.move(can,speed,0)
                chs -= speed
            for i in player1.hitbox:
                i.move(speed,0)
    if keyset[3] == 1:
        rotation()
        if player1.detect(can,"exit") != []:
           moveroom()
        elif chs >= hoscroll or not(player1.hitbox[1].x<=uvl and player1.hitbox[1].x>=lvl):
            if player1.hitbox[1].x<=width:
                player1.move(can,speed,0)
        else:
            for i in player1.hitbox:
                i.move(speed,0)
            if player1.detect(can,"solid") == []:
                bg.move(can,-speed,0)
                chs += speed
            for i in player1.hitbox:
                i.move(-speed,0)
    if keyset[4] == 1:
        player1.scale(can,0.95)
    if keyset[5] == 1:
        player1.scale(can,1.05)
    if keyset[6] == 1:
        player1.rotate(can,3)
    if keyset[7] == 1:
        player1.rotate(can,-3)
    if keyset[8] == 1:
        player1.pickup(can)
    window.after(9,main)



def uppr(key):
    global keyset
    keyset[0] = 1
def upre(key):
    global keyset
    keyset[0] = 0
def downpr(key):
    global keyset
    keyset[1] = 1
def downre(key):
    global keyset
    keyset[1] = 0
def leftpr(key):
    global keyset
    keyset[2] = 1
def leftre(key):
    global keyset
    keyset[2] = 0
def rightpr(key):
    global keyset
    keyset[3] = 1
def rightre(key):
    global keyset
    keyset[3] = 0
def wpr(key):
    global keyset
    keyset[4] = 1
def wre(key):
    global keyset
    keyset[4] = 0
def epr(key):
    global keyset
    keyset[5] = 1
def ere(key):
    global keyset
    keyset[5] = 0
def spr(key):
    global keyset
    keyset[6] = 1
def sre(key):
    global keyset
    keyset[6] = 0
def dpr(key):
    global keyset
    keyset[7] = 1
def dre(key):
    global keyset
    keyset[7] = 0
def vpr(key):
    global keyset
    keyset[8] = 1
def vre(key):
    global keyset
    keyset[8] = 0

def b1(event):
    print(event.x)
    print(event.y)
    print(player1.center.x)
    print(player1.center.y)

def bind():
    window.bind_all("<Button-1>",b1)
    window.bind_all("<Up>",uppr)
    window.bind_all("<KeyRelease-Up>",upre)
    window.bind_all("<Down>",downpr)
    window.bind_all("<KeyRelease-Down>",downre)
    window.bind_all("<Left>",leftpr)
    window.bind_all("<KeyRelease-Left>",leftre)
    window.bind_all("<Right>",rightpr)
    window.bind_all("<KeyRelease-Right>",rightre)
    window.bind_all("<w>",wpr)
    window.bind_all("<KeyRelease-w>",wre)
    window.bind_all("<e>",epr)
    window.bind_all("<KeyRelease-e>",ere)
    window.bind_all("<s>",spr)
    window.bind_all("<KeyRelease-s>",sre)
    window.bind_all("<d>",dpr)
    window.bind_all("<KeyRelease-d>",dre)
    window.bind_all("<v>",vpr)
    window.bind_all("<KeyRelease-v>",vre)
    window.bind_all("<Configure>",resize)


window = tkinter.Tk()
window.geometry("800x600")
width = 800
height = 600

mainmenu()
window.mainloop()
