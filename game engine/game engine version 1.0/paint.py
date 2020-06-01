import tkinter
from classes import *

def frect():
    global shape,cshape
    if shape != "rectangle":
        shape = "rectangle"
        rectbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = rectbut
def fhitb():
    global shape,cshape
    if shape != "hitbox":
        shape = "hitbox"
        hitbbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = hitbbut
def fpoly():
    global shape,cshape
    if shape!= "polygon":
        shape = "polygon"
        polybut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = polybut
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




def fctag():
    global tags
    tags = ""
    tagtext.config(text="tags = "+tags)

def fname():
    global name
    name = nameent.get()
    nameent.delete(0,"end")
    nametext.config(text="name = "+name)

window = tkinter.Tk()
window.geometry("1000x800")

def start(atype):
    global itype,shape,colour,tags,ltags,name,cbd,oldcl,rectbut,polybut,linebut,centbut,tagbut,ctagbut,tagent,tagtext,nameent,namebut,nametext,e1ent,e2ent,e3ent,e4ent,e5ent,ebut,xent,yent,setbut,cshape,can,center,temp,pcoords,shapelist,cshapelist,boxsize,xoff,yoff
    spritebut.destroy()
    bgbut.destroy()
    itembut.destroy()
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
    centbut = tkinter.Button(window,text="center",command=fcent)
    centbut.place(x=70,y=160,width=60,height=50)
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
    e1ent = tkinter.Entry(window)
    e1ent.place(x=5,y=705,height=35,width=200)
    e2ent = tkinter.Entry(window)
    e2ent.place(x=205,y=705,height=35,width=200)
    e3ent = tkinter.Entry(window)
    e3ent.place(x=410,y=705,height=35,width=200)
    e4ent = tkinter.Entry(window)
    e4ent.place(x=615,y=705,height=35,width=200)
    e5ent = tkinter.Entry(window)
    e5ent.place(x=820,y=705,height=35,width=175)
    ebut = tkinter.Button(window,text="set exit",command=fexits)
    ebut.place(x=400,y=755,width=70,height=40)
    xent = tkinter.Entry(window)
    xent.place(x=421,y=5,height=35,width=40)
    yent = tkinter.Entry(window)
    yent.place(x=421,y=55,height=35,width=40)
    setbut = tkinter.Button(window,text="set width\nand height",command=fset)
    setbut.place(x=470,y=5,width=70,height=80)
    cshape = rectbut
    can = tkinter.Canvas()
    can.place(x=200,y=100,width=800,height=600)
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
    window.bind_all("<Up>",uppr)
    window.bind_all("<KeyRelease-Up>",upre)
    window.bind_all("<Down>",downpr)
    window.bind_all("<KeyRelease-Down>",downre)
    window.bind_all("<Left>",leftpr)
    window.bind_all("<KeyRelease-Left>",leftre)
    window.bind_all("<Right>",rightpr)
    window.bind_all("<KeyRelease-Right>",rightre)
    xoff = 0
    yoff = 0
    main()

exitstring = ",{"
def fexits():
    global exitstring
    exitstring += "\""+e1ent.get()+"\":[\""+e2ent.get()+"\",\""+e3ent.get()+"\",["+e4ent.get()+"],["+e5ent.get()+"]],"

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
    strings += "\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+"),"
    shapelist.append(strings)

def b1press(event):
    global firstx,firsty,pcoords,center,shapelist,hitbox
    if shape == "rectangle" or shape == "line":
        firstx = event.x
        firsty = event.y
    elif shape == "center":
        for i in range(len(shapelist)):
            shapelist[i] += "["+str(event.x)+","+str(event.y)+"]]"
            hitbox = [event.x-boxsize,event.y-boxsize,event.x+boxsize,event.y+boxsize]
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
        strings += "],\""+str(oldcl)+"\",\""+str(oldcl)+"\",(\"\""+nv+tags+"),"
        shapelist.append(strings)
        pcoords = []
        temp = 0

hitbox = [0,0,0,0]
def motion(event):
    global temp
    if shape == "polygon":
        tempcoords = pcoords+[event.x,event.y]
        if temp != 0:
            can.delete(temp)
        temp = can.create_polygon(tuple(tempcoords),fill=oldcl)

def b1rele(event):
    global temp,shapelist
    if shape == "rectangle":
        can.create_rectangle(firstx,firsty,event.x,event.y,fill=oldcl)
        can.delete(temp)
        temp = 0
    elif shape == "line":
        can.create_line(firstx,firsty,event.x,event.y,fill=oldcl)
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

def fprint(key):
    global exitstring
    finalout = name+" = [["
    for i in shapelist:
        finalout += i+","
    if itype == "sprite":
        finalout += str(hitbox)+"]"
    elif itype == "background":
        finalout += str([width,height])
    elif itype == "item":
        print("dunno yet")
    finalout += exitstring
    finalout += "}]"
    print(finalout)
    #file = open("sprites.py","a")
    #file.write(finalout+"\n")
    #file.close()

keyset = [0,0,0,0]
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
        xoff += 5
    if keyset[3]==1:
        for i in cshapelist:
            i.move(can,-5,0)
        xoff -= 5
    window.after(7,main)

spritebut = tkinter.Button(text="draw a sprite",command=lambda i="sprite":start(i))
spritebut.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.2)
bgbut = tkinter.Button(text="draw a background",command=lambda i="background":start(i))
bgbut.place(relx=0.3,rely=0.35,relwidth=0.4,relheight=0.2)
itembut = tkinter.Button(text="draw an item",command=lambda i="item":start(i))
itembut.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.2)

window.mainloop()
