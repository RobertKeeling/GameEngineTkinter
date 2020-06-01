import tkinter,copy
import makedictionaries
from classes import *
from backgrounds import *
from sprites import *
from items import *
from dictionaries import *
from items_meta import*

############################################################################
#######BUTTON_CALLBACKS#######BUTTON_CALLBACKS#######BUTTON_CALLBACKS#######
############################################################################

def frect():
    global shape,cshape
    if shape != "rectangle":
        shape = "rectangle"
        rectbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = rectbut

def fpoly():
    global shape,cshape
    if shape!= "polygon":
        shape = "polygon"
        polybut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = polybut

def fbexit():
    global shape,cshape
    if shape!= "exit":
        shape = "exit"
        exitbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = exitbut

def fline():
    global shape,cshape
    if shape != "line":
        shape = "line"
        linebut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = linebut

def fcent():
    global shape,cshape
    if shape != "center":
        shape = "center"
        centbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = centbut

def frh():
    global shape,cshape
    if shape != "right hand":
        shape = "right hand"
        rhbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = rhbut

def flh():
    global shape,cshape
    if shape != "left hand":
        shape = "left hand"
        lhbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = lhbut

def ftags():
    global tags,ltags
    if tags != "":
        tags += ",\""+tagent.get()+"\""
    else:
        tags += "\""+tagent.get()+"\""
    ltags.append(tagent.get())
    tagent.delete(0,"end")
    tagtext.config(text="tags = "+tags)

def changecolour(col):
    global colour,oldcl
    if col != oldcl:
        colour = col
        cbd[oldcl].config(relief="raised")
        cbd[col].config(relief="sunken")
        oldcl = col

def fctag():
    global tags
    tags = ""
    tagtext.config(text="tags = "+tags)

def fname():
    global name
    name = nameent.get()
    nameent.delete(0,"end")
    nametext.config(text="name = "+name)

def fset():
    global height,width
    height = int(yent.get())
    width = int(xent.get())
    cshapelist.append(polygon(can,[[0,0],[int(xent.get()),0]],fill=oldcl,outline=oldcl))
    cshapelist.append(polygon(can,[[int(xent.get()),0],[int(xent.get()),int(yent.get())]],fill=oldcl,outline=oldcl))
    cshapelist.append(polygon(can,[[0,int(yent.get())],[int(xent.get()),int(yent.get())]],fill=oldcl,outline=oldcl))
    cshapelist.append(polygon(can,[[0,0],[0,int(yent.get())]],fill=oldcl,outline=oldcl))
    cshapelist.append(polygon(can,[[0,0],[width,0],[width,height],[0,height]],fill=oldcl,outline=oldcl))
    strings = "[[0,0],["+xent.get()+",0],["+xent.get()+","+yent.get()+"],[0,"+yent.get()+"]],"
    strings += "\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+"),[0,0]]"
    shapelist.append(strings)

############################################################################
########OTHER_FUNCTIONS########OTHER_FUNCTIONS########OTHER_FUNCTIONS#######
############################################################################




def hexrgb(r,g,b):
    rgb = "#"
    for i in [r,g,b]:
        x = str(hex(i))[2:]
        if len(x)==1:
            x = "00" + x
        elif len(x)==2:
            x = "0" + x
        rgb += x
    return(rgb)

def fprint(key):
    global exitstring
    if itype == "sprite":
        sdia()
        return(0)
    elif itype == "background":
        finalout = name+" = [["
        for i in shapelist:
            finalout += i+","
        finalout += str([width,height])
        finalout += exitstring[:-1]
        finalout += "}]"
    elif itype == "item":
        finalout = name + " = ["
        for i in shapelist:
            finalout += i[:-1]+",["+str(center[0])+","+str(center[1])+"]],"
        finalout += "["+str(center[0])+","+str(center[1])+"]]"
    if itype == "background":
        file = open("backgrounds.py","a")
        file.write(finalout+"\n")
        file.close()
        file = open("itemlocales.py","a")
        file.write("il"+name+" = []\n")
        file.close()
    elif itype == "item":
        file = open("items.py","a")
        file.write(finalout+"\n")
        file.close()

############################################################################
######DRAWING_FUNCTIONS#######DRAWING_FUNCTIONS#######DRAWING_FUNCTIONS#####
############################################################################

def b1press(event):
    global firstx,firsty,pcoords,center,rh,lh,shapelist
    if shape == "rectangle" or shape == "line" or shape == "exit":
        firstx = event.x
        firsty = event.y
    elif shape == "center":
        center = [event.x,event.y]
    elif shape == "right hand":
        rh = [event.x,event.y]
    elif shape == "left hand":
        lh = [event.x,event.y]
    else:
        pcoords.append([event.x,event.y])

def b3press(event):
    global pcoords,temp,cshapelist
    if shape == "polygon" and pcoords != []:
        pcoords.append([event.x,event.y])
        can.delete(temp)
        cshapelist.append(polygon(can,pcoords,fill=oldcl,outline=oldcl,tag=ltags))
        strings = "[[["
        for i in pcoords:
            strings += str(i[0]+xoff)+","+str(i[1]+yoff)+"],["
        strings = strings[:-2]
        if tags == "":
            nv = ""
        else:
            nv = ","
        if itype == "background":
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+nv+tags+"),[0,0]]"
        else:
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+nv+"\" \",\"item\""+tags+"),"
        shapelist.append(strings)
        pcoords = []
        temp = 0


def motion(event):
    global temp
    if shape == "polygon":
        tempcoords = pcoords+[event.x,event.y]
        if temp != 0:
            can.delete(temp)
        temp = can.create_polygon(tuple(tempcoords),fill=oldcl)


def b1rele(event):
    global temp,shapelist,cshapelist,wexit,iwexit
    if shape == "rectangle":
        cshapelist.append(polygon(can,[[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]],fill=oldcl,outline=oldcl,tag=ltags))
        can.delete(temp)
        strings = "[[["
        for i in [[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]]:
            strings += str(i[0]+xoff)+","+str(i[1]+yoff)+"],["
        strings = strings[:-2]
        if tags == "":
            nv = ""
        else:
            nv = ","
        if itype == "item":
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\" \",\"item\""+nv+tags+")"
        else:
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+nv+tags+")"
        if itype == "background":
            strings += ",[0,0]]"
        else:
            strings += "]"
        shapelist.append(strings)
        temp = 0
    elif shape == "line":
        cshapelist.append(polygon(can,[[firstx,firsty],[event.x,event.y]],fill=oldcl,outline=oldcl,tag=ltags))
        can.delete(temp)
        strings = "[[["
        for i in [[firstx,firsty],[event.x,event.y]]:
            strings += str(i[0]+xoff)+","+str(i[1]+yoff)+"],["
        strings = strings[:-2]
        if tags == "":
            nv = ""
        else:
            nv = ","
        if itype == "item":
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\" \",\"item\""+nv+tags+")"
        else:
            strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+nv+tags+")"
        if itype == "rectangle":
            strings += ",[0,0]]"
        else:
            strings += "]"
        shapelist.append(strings)
        can.create_line(firstx,firsty,event.x,event.y,fill=oldcl)
        can.delete(temp)
        temp = 0
    elif shape == "exit":
        cshapelist.append(polygon(can,[[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]],fill=oldcl,outline=oldcl,tag=wexit))
        can.delete(temp)
        strings = "[[["
        for i in [[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]]:
            strings += str(i[0]+xoff)+","+str(i[1]+yoff)+"],["
        strings = strings[:-2]
        if tags == "":
            nv = ""
        else:
            nv = ","
        strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\",\"exit\",\""+wexit+"\")"
        if itype == "background":
            strings += ",[0,0]]"
        else:
            strings += "]"
        shapelist.append(strings)
        dia(wexit)
        iwexit += 1
        wexit = "exit"+str(iwexit)
        can.delete(temp)
        temp = 0

def b1motion(event):
    global temp
    if shape == "rectangle" or shape == "hitbox":
        if temp == 0:
            temp = can.create_rectangle(firstx,firsty,event.x,event.y)
        else:
            can.delete(temp)
            temp = can.create_rectangle(firstx,firsty,event.x,event.y)
    elif shape == "line":
        if temp == 0:
            temp = can.create_line(firstx,firsty,event.x,event.y)
        else:
            can.delete(temp)
            temp = can.create_line(firstx,firsty,event.x,event.y)


############################################################################
#######ITEM_PLACEMENT_FUNCTIONS############ITEM_PLACEMENT_FUNCTIONS#########
############################################################################

def loaditem(i):
    global item1,diaopen,ids
    z = True
    while z == True:
        if ids in usedids:
            ids += 1
        else:
            z = False
    nil.append(i.split("=")[0][:-1])
    il.append(["id"+str(ids),item(can,copy.deepcopy(idic[i.split("=")[0][:-1]]),et="id"+str(ids))])
    for x in il[-1][1].items:
        can.tag_bind(x.tk,"<Button-1>",itemclicked)
        can.tag_bind(x.tk,"<B1-Motion>",itemmoved)
        can.tag_bind(x.tk,"<ButtonRelease-1>",setmove)
    wic.destroy()
    ids += 1
    diaopen = False

def deleteitem(event):
    can.delete(tid)
    td = []
    for i in range(len(il)):
        if tid == il[i][0]:
            td.append(i)
    for i in td:
        del(il[i])
    td = []
    for i in range(len(litems)):
        if tid == litems[i][-6:].split("\"")[0]:
            td.append(i)
    for i in td:
        del(litems[i])

def loaditems(bg):
    global ids,litems,usedids
    usedids = []
    x = ildic["il"+bg]
    for i in range(len(x)):
        il.append([x[i][3],item(can,copy.deepcopy(idic[x[i][0]]),et=x[i][3])])
        il[i][1].repos(can,x[i][1],x[i][2])
        ns = "[\""+x[i][0]+"\","+str(x[i][1])+","+str(x[i][2])+",\""+x[i][3]+"\"],"
        nil.append(x[i][0])
        usedids.append(int(x[i][3].split("d")[1]))
        litems.append(ns)
    for x in il:
        for i in x[1].items:
            can.tag_bind(i.tk,"<Button-1>",itemclicked)
            can.tag_bind(i.tk,"<B1-Motion>",itemmoved)
            can.tag_bind(i.tk,"<ButtonRelease-1>",setmove)
    

def itemclicked(event):
    global oldx,oldy,cx,cy,tid
    x = can.find_overlapping(event.x+2,event.y+2,event.x-2,event.y-2)
    for i in x:
        try:
            tid = can.gettags(i)[3]
        except:
            dn = 0
    for i in il:
        cx = i[1].center.x
        cy = i[1].center.y
    oldx = event.x
    oldy = event.y

def itemmoved(event):
    global oldx,oldy,cx,cy
    for i in il:
        for x in i[1].items:
            if can.gettags(x.tk)[3] == tid:
                cx = i[1].center.x
                cy = i[1].center.y
                i[1].move(can,event.x-oldx,event.y-oldy)
                cx += (event.x-oldx)
                cy += (event.y-oldy)
                oldx = event.x
                oldy = event.y

def setmove(event):
    global litems
    for i in il:
        for x in i[1].items:
            y = can.gettags(x.tk)
            if y[3] == tid:
                ns = "[\""+y[2]+"\","+str(cx+xoff)+","+str(cy+yoff)+",\""+str(tid)+"\"],"
                td = []
                for i in range(len(litems)):
                    if ns[-7:] == litems[i][-7:]:
                        td.append(i)
                for i in td:
                    del(litems[i])
    litems.append(ns)

def savelocations(event):
    file = open("itemlocales.py","r")
    c = file.readlines()
    file.close()
    sitems = ""
    for i in litems:
        sitems += i
    out = "il"+bg+" = ["+sitems[:-1]+"]"
    for i in range(len(c)):
        try:
            if c[i].split("=")[0] == out.split("=")[0]:
                del(c[i])
        except:
            dn = 0
    c.append(out)
    file = open("itemlocales.py","w")
    for i in c:
        file.write(i)
    file.close()


############################################################################
#########DIALOGUE_BOX_FUNCTIONS##############DIALOGUE_BOX_FUNCTIONS#########
############################################################################


#############FOR_ITEM_CHOICE################

def fichoice(abg):
    file = open("items.py","r")
    x = file.readlines()
    file.close()
    icdia(x)

def icdia(items):
    global diaopen,wic
    if diaopen == False:
        diaopen = True
        wic = tkinter.Tk()
        wic.geometry("500x500")
        wic.wm_title("Choose Item")
        itembuts = []
        for i in items:
            itembuts.append(tkinter.Button(wic,text=i.split("=")[0][:-1],command=lambda i=i: loaditem(i)))
        x = 5
        y = 5
        for i in itembuts:
            i.place(x=x,y=y,height=50,width=100)
            y += 55
            if y >= 216:
                y = 5
                x += 105

#############FOR_SPRITE_MODE################

def scldia():
    global diaopen
    boxwidth = ebw.get()
    boxheight = ebh.get()
    finalout = name+" = ["
    for i in shapelist:
        finalout += i+","
    finalout += "["+str(lh[0])+","+str(lh[1])+"],["+str(rh[0])+","+str(rh[1])+"],["+str(center[0])+","+str(center[1])+"],"+boxwidth+","+boxheight+"]"
    file = open("sprites.py","a")
    file.write(finalout+"\n")
    file.close()
    gexit.destroy()
    diaopen = False

def sdia():
    global gexit,diaopen,ebh,ebw
    if diaopen == False:
        diaopen = True
        gexit = tkinter.Tk()
        gexit.geometry("280x200")
        gexit.wm_title("Set hitboxes")
        ebw = tkinter.Entry(gexit)
        ebw.place(x=20,y=20,height=40,width=50)
        ebwtext = tkinter.Label(gexit,text="box width")
        ebwtext.place(x=75,y=20,height=40,width=200)
        ebh = tkinter.Entry(gexit)
        ebh.place(x=20,y=70,height=40,width=50)
        ebhtext = tkinter.Label(gexit,text="box height")
        ebhtext.place(x=75,y=70,height=40,width=200)
        ebut = tkinter.Button(gexit,text="enter",command=scldia)
        ebut.place(x=80,y=120,width=120,height=60)

#############FOR_BACKGROUND_MODE################

def cldia(wexit):
    global diaopen,exitstring
    exitstring += "\""+wexit+"\":[\""+bgent.get()+"\",\""+exent.get()+"\",["+xoent.get()+","+yoent.get()+"],["+xpent.get()+","+ypent.get()+"]],"
    gexit.destroy()
    diaopen = False
        

def dia(wexit):
    global gexit,diaopen,bgent,exent,xoent,yoent,xpent,ypent
    if diaopen == False:
        diaopen = True
        gexit = tkinter.Tk()
        gexit.geometry("500x300")
        gexit.wm_title(wexit)
        bgent = tkinter.Entry(gexit)
        bgent.place(x=20,y=20,height=40,width=250)
        bgtext = tkinter.Label(gexit,text="background \nto link to")
        bgtext.place(x=280,y=20,height=40,width=200)
        exent = tkinter.Entry(gexit)
        exent.place(x=20,y=70,height=40,width=250)
        extext = tkinter.Label(gexit,text="exit to link to")
        extext.place(x=280,y=70,height=40,width=200)
        xoent = tkinter.Entry(gexit)
        xoent.place(x=20,y=120,height=40,width=50)
        xotext = tkinter.Label(gexit,text="x offset")
        xotext.place(x=90,y=120,height=40,width=70)
        yoent = tkinter.Entry(gexit)
        yoent.place(x=180,y=120,height=40,width=50)
        yotext = tkinter.Label(gexit,text="y offset")
        yotext.place(x=250,y=120,height=40,width=70)
        xpent = tkinter.Entry(gexit)
        xpent.place(x=20,y=170,height=40,width=50)
        xptext = tkinter.Label(gexit,text="x spawn")
        xptext.place(x=90,y=170,height=40,width=70)
        ypent = tkinter.Entry(gexit)
        ypent.place(x=180,y=170,height=40,width=50)
        yptext = tkinter.Label(gexit,text="y spawn")
        yptext.place(x=250,y=170,height=40,width=70)
        ebut = tkinter.Button(gexit,text="enter",command =lambda i=wexit:cldia(i))
        ebut.place(x=250,y=220,width=200,height=60)


############################################################################
###########KEYBINDINGS###########KEYBINDINGS##########KEYBINDINGS###########
############################################################################

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

############################################################################
##########LOADS_USER_INTERFACES#############LOADS_USER_INTERFACES###########
############################################################################

def start(atype):
    global itype,il,shape,colour,tags,nil,width,height,ltags,name,cbd,oldcl,buttonlist,rectbut,exitbut,polybut,linebut,centbut,lhbut,rhbut,tagbut,ctagbut,tagent,tagtext,nameent,namebut,nametext,e1ent,e2ent,e3ent,e4ent,e5ent,ebut,xent,yent,setbut,cshape,can,center,temp,pcoords,shapelist,cshapelist,boxsize,xoff,yoff,placeitembut
    spritebut.destroy()
    il = []
    width = 800
    height = 600
    xoff = 0
    yoff = 0
    bgbut.destroy()
    itembut.destroy()
    placeitembut.destroy()
    can = tkinter.Canvas()
    can.place(x=200,y=200,width=800,height=600)
    window.bind_all("<Up>",uppr)
    window.bind_all("<KeyRelease-Up>",upre)
    window.bind_all("<Down>",downpr)
    window.bind_all("<KeyRelease-Down>",downre)
    window.bind_all("<Left>",leftpr)
    window.bind_all("<KeyRelease-Left>",leftre)
    window.bind_all("<Right>",rightpr)
    window.bind_all("<KeyRelease-Right>",rightre)
    if atype != "place item":
        shape = "rectangle"
        itype = atype
        colour = "red"
        tags = ""
        ltags = []
        name = ""
        cbd = {}
        x = 5
        y = 290
        c = 0
        for r in range(0,4095,1000):
            for g in range(0,4095,1000):
                for b in range(0,4095,1000):
                    cl = hexrgb(r,g,b)
                    cbd[cl] = tkinter.Button(window,background=cl,foreground=cl,command=lambda i=cl:changecolour(i))
                    cbd[cl].place(x=x,y=y,width=20,height=20)
                    x += 22
                    if x > 170:
                        x = 5
                        y += 22
                    c += 1
        oldcl = hexrgb(0,0,0)
        rectbut = tkinter.Button(window,text="rectangle",command=frect)
        rectbut.place(x=5,y=105,width=60,height=50)
        rectbut.config(relief="sunken")
        polybut = tkinter.Button(window,text="polygon",command=fpoly)
        polybut.place(x=135,y=105,width=60,height=50)
        linebut = tkinter.Button(window,text="line",command=fline)
        linebut.place(x=5,y=160,width=60,height=50)
        tagbut = tkinter.Button(window,text=" add tag",command=ftags)
        tagbut.place(x=135,y=215,width=60,height=50)
        ctagbut = tkinter.Button(window,text="clear tags",command=fctag)
        ctagbut.place(x=5,y=5,width=90,height=40)
        tagent = tkinter.Entry(window)
        tagent.place(x=20,y=220,height=35,width=100)
        tagtext = tkinter.Label(window,text="tags = "+tags)
        tagtext.place(x=200,y=5,height=40,width=200)
        nameent = tkinter.Entry(window)
        nameent.place(x=5,y=50,height=35,width=200)
        namebut = tkinter.Button(window,text="set name",command=fname)
        namebut.place(x=100,y=5,width=70,height=40)
        nametext = tkinter.Label(window,text="name = "+name)
        nametext.place(x=200,y=50,height=40,width=200)
        if itype == "background":
            exitbut = tkinter.Button(window,text="exit",command=fbexit)
            exitbut.place(x=70,y=105,width=60,height=50)
            xent = tkinter.Entry(window)
            xent.place(x=421,y=5,height=35,width=40)
            yent = tkinter.Entry(window)
            yent.place(x=421,y=55,height=35,width=40)
            setbut = tkinter.Button(window,text="set width\nand height",command=fset)
            setbut.place(x=470,y=5,width=70,height=80)
        elif itype == "sprite" or itype == "item":
            centbut = tkinter.Button(window,text="center",command=fcent)
            centbut.place(x=70,y=105,width=60,height=50)
            if itype == "sprite":
                rhbut = tkinter.Button(window,text="right\nhand",command=frh)
                rhbut.place(x=70,y=160,width=60,height=50)
                lhbut = tkinter.Button(window,text="left\nhand",command=flh)
                lhbut.place(x=135,y=160,width=60,height=50)
        cshape = rectbut
        center = [0,0]
        temp = 0
        pcoords = []
        shapelist = []
        cshapelist = []
        boxsize = 50
        can.bind("<Button-1>",b1press)
        can.bind("<ButtonRelease-1>",b1rele)
        can.bind("<B1-Motion>",b1motion)
        can.bind("<Button-3>",b3press)
        can.bind("<Motion>",motion)
        window.bind_all("<KeyPress-Return>",fprint)
        main()
    else:
        file = open("backgrounds.py","r")
        x = file.readlines()
        window.bind_all("<KeyPress-Return>",savelocations)
        window.bind_all("<KeyPress-Delete>",deleteitem)
        file.close()
        bglist = []
        nil = []
        for i in x:
            bglist.append(i.split(" ")[0])
        buttonlist = []
        for i in bglist:
            buttonlist.append(tkinter.Button(text=i,command=lambda i=i:loadbg(i)))
        x = 5
        y = 5
        for i in buttonlist:
            i.place(x=x,y=y,width=90,height=30)
            y += 35
            if y > 970:
                y = 5
                x += 95

def loadbg(sbg):
    global nbg,bg,litems,ids
    ids = 1
    litems = []
    bg = sbg
    for i in buttonlist:
        i.destroy()
    x = copy.deepcopy(bgdic[bg])
    exits = x.pop()
    dimensions = x.pop()
    nbg = group(can,x)
    loaditems(bg)
    ichoice = tkinter.Button(text="Choose Item",command=lambda i=bg:fichoice(sbg))
    ichoice.place(x=450,y=50,width=100,height=50)
    mains()

def mains():
    global xoff,yoff
    if keyset[0]==1:
        for i in il:
            i[1].move(can,0,5)
        nbg.move(can,0,5)
        yoff -= 5
    if keyset[1]==1:
        for i in il:
            i[1].move(can,0,-5)
        nbg.move(can,0,-5)
        yoff += 5
    if keyset[2]==1:
        for i in il:
            i[1].move(can,5,0)
        nbg.move(can,5,0)
        xoff -= 5
    if keyset[3]==1:
        for i in il:
            i[1].move(can,-5,0)
        nbg.move(can,-5,0)
        xoff += 5
    window.after(7,mains)

def main():
    global xoff,yoff
    if keyset[0]==1:
        for i in cshapelist:
            i.move(can,0,5)
        yoff -= 5
    if keyset[1]==1:
        for i in cshapelist:
            i.move(can,0,-5)
        yoff += 5
    if keyset[2]==1:
        for i in cshapelist:
            i.move(can,5,0)
        xoff -= 5
    if keyset[3]==1:
        for i in cshapelist:
            i.move(can,-5,0)
        xoff += 5
    window.after(7,main)





window = tkinter.Tk()
window.geometry("1000x800")
window.wm_title("Paint")

keyset = [0,0,0,0]
hitbox = [0,0,0,0]
iwexit = 1
wexit = "exit"+str(iwexit)
exitstring = ",{"
diaopen = False

spritebut = tkinter.Button(window,text="draw a sprite",command=lambda i="sprite":start(i))
spritebut.place(relx=0.1,rely=0.1,relwidth=0.35,relheight=0.2)
bgbut = tkinter.Button(text="draw a background",command=lambda i="background":start(i))
bgbut.place(relx=0.1,rely=0.35,relwidth=0.35,relheight=0.2)
itembut = tkinter.Button(text="draw an item",command=lambda i="item":start(i))
itembut.place(relx=0.1,rely=0.6,relwidth=0.35,relheight=0.2)
placeitembut = tkinter.Button(text="place items\non background",command=lambda i="place item":start(i))
placeitembut.place(relx=0.55,rely=0.1,relwidth=0.35,relheight=0.2)


window.mainloop()
