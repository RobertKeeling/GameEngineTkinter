import tkinter,copy,time,os,makedictionaries,importlib,dictionaries
from classes import *
from paintclasses import *
from PIL import Image,ImageTk

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

def foval():
    global shape,cshape
    if shape!= "ovalbut":
        shape = "oval"
        ovalbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = ovalbut

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

def fselect():
    global shape,cshape
    if shape != "select":
        shape = "select"
        selectbut.config(relief="sunken")
        cshape.config(relief="raised")
        cshape = selectbut

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
    
def fsolid():
    global ltags
    ltags.append("solid")
    sbut.config(relief="sunken")
    nsbut.config(relief="raised")

def fnsolid():
    global ltags
    for i in range(len(ltags)):
        if ltags[i] == "solid":
            del(ltags[i])
    nsbut.config(relief="sunken")
    sbut.config(relief="raised")


############################################################################
########OTHER_FUNCTIONS########OTHER_FUNCTIONS########OTHER_FUNCTIONS#######
############################################################################

def createinterface(d,rel=True,colsel=False,colselx=10,colsely=10):
    global interfacelist,cbd,oldcl
    if rel == False:
        data = []
        for i in d:
            data.append([i[0],i[1],i[2],i[3]/1060,i[4]/840,i[5]/1060,i[6]/840])
    else:
        data = d
    for t,text,command,x,y,width,height in data:
        if t == "b":
            interfacelist.append(tkinter.Button(text=text,command=command))
        elif t == "e":
            interfacelist.append(tkinter.Entry())
        elif t == "l":
            interfacelist.append(tkinter.Label(text=text))
        interfacelist[-1].place(relx=x,rely=y,relwidth=width,relheight=height)
    if colsel == True:
        cbd = {}
        oldcl = hexrgb(0,0,0)
        for r in range(0,4095,1000):
            for g in range(0,4095,1000):
                for b in range(0,4095,1000):
                    cl = hexrgb(r,g,b)
                    cbd[cl] = tkinter.Button(window,background=cl,foreground=cl,command=lambda i=cl:changecolour(i))
                    cbd[cl].place(x=colselx,y=colsely,width=20,height=20)
                    colselx += 22
                    if colselx > 170:
                        colselx = 10
                        colsely += 22

def destroyinterface(colsel=False):
    global interfacelist
    for i in interfacelist:
        i.destroy()
    if colsel == True:
        for i in cbd:
            cbd[i].destroy()
    interfacelist = []

def validate(x):
    try:
        t = float(x)
        return(True)
    except:
        return(False)

def bgp(i):
    file = open("backgrounds.py","a")
    file.write(i)
    file.close()
    file = open("itemlocales.py","a")
    file.write("il" + name + " = []\n")
    file.close()

def sp(i):
    file = open("items.py","a")
    file.write(i+"\n")
    file.close()


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

def fprint():
    if itype == "sprite":
        if rh != [0,0] and lh != [0,0] and center != [0,0]:
            sdia()
            return(0)
        else:
            err = ""
            if rh == [0,0]:
                err += "Right Hand not set\n"
            if lh == [0,0]:
                err += "Left Hand not set\n"
            if center == [0,0]:
                err += "Center not set\n"
            errorbox(err)
    elif itype == "background":
        ssl = csltossl()
        for i in ssl:
            i.append([0,0])
        ssl.append(imagename[2:][:-1])
        ssl.append([width,height])
        if exitstring != "":
            ssl = name + " = " + str(ssl)[:-1] + exitstring[:-1] + "}]\n"
        else:
            ssl = name + " = " + str(ssl)[:-1] + "]\n"
        bgp(ssl)
    elif itype == "item":
        if center != [0,0]:
            ssl = csltossl()
            for i in ssl:
                i.append(center)
            ssl.append(center)
            ssl = name + " = " + str(ssl)
            sp(ssl)
        else:
            errorbox("Center not set.")

def csltossl():
    out = []
    for i in range(len(cshapelist)):
        coords = can.coords(cshapelist[i].tk)
        nc = []
        ac = []
        fc = []
        for x in range(len(coords)):
            if x%2 == 0:
                ac.append(int(coords[x]+xoff))
            else:
                ac.append(int(coords[x]+yoff))
                nc.append(ac)
                ac = []
        fc.append(nc)
        fc.append(can.itemconfig(cshapelist[i].tk)["fill"][4])
        fc.append(can.itemconfig(cshapelist[i].tk)["fill"][4])
        f1 = [""]
        for x in can.gettags(cshapelist[i].tk):
            if x != "current":
                f1.append(x)
        if f1 == [""]:
            f1.append("")
        fc.append(tuple(f1))
        out.append(fc)
    return(out)

############################################################################
######DRAWING_FUNCTIONS#######DRAWING_FUNCTIONS#######DRAWING_FUNCTIONS#####
############################################################################

def resize(event):
    global ww,wh
    ww = window.winfo_width()
    wh = window.winfo_height()

def inselarea(coords):
    if ((coords[0] >= selarea[0] and coords[0] <= selarea[2]) or (coords[0] <= selarea[0] and coords[0] >= selarea[2])) and ((coords[1] >= selarea[1] and coords[1] <= selarea[3]) or (coords[1] <= selarea[1] and coords[1] >= selarea[3])):
        return(True)
    else:
        return(False)

def selmove1(event):
    global sfirstx,sfirsty
    sfirstx = event.x
    sfirsty = event.y

def selmove2(event):
    global selarea,sfirstx,sfirsty
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.move(can,event.x-sfirstx,event.y-sfirsty)
    for i in tempbox:
        i.move(can,event.x-sfirstx,event.y-sfirsty)
    selarea[0] += event.x-sfirstx
    selarea[1] += event.y-sfirsty
    selarea[2] += event.x-sfirstx
    selarea[3] += event.y-sfirsty
    sfirstx = event.x
    sfirsty = event.y

def b1press(event):
    global firstx,firsty,pcoords,center,rh,lh,shapelist,toff,selarea,tempbox,ppos,ang,cshapelist
    cd = {"center":"blue","right hand":"red","left hand":"green"}
    firstx = event.x
    firsty = event.y
    if inselarea([event.x,event.y]):
        toff = True
    else:
        for i in tempbox:
            i.destroy(can)
        tempbox = []
        toff = False
        selarea = [0,0,0,0]
        ang = True
        can.dtag("selected","selected")
        for i in cshapelist:
            i.dtag("selected")
        if shape == "center":
            center = [event.x,event.y]
            if ppos["centerx"] != 0:
                can.delete(ppos["centerx"])
                can.delete(ppos["centery"])
            ppos["centerx"] = can.create_line(0,event.y,800,event.y,dash = (4,4),fill = "blue")
            ppos["centery"] = can.create_line(event.x,0,event.x,600,dash = (4,4),fill = "blue")
        elif shape == "right hand":
            rh = [event.x,event.y]
            if ppos["rhx"] != 0:
                can.delete(ppos["rhx"])
                can.delete(ppos["rhy"])
            ppos["rhx"] = can.create_line(0,event.y,800,event.y,dash = (4,4),fill = "green")
            ppos["rhy"] = can.create_line(event.x,0,event.x,600,dash = (4,4),fill = "green")
        elif shape == "left hand":
            lh = [event.x,event.y]
            if ppos["lhx"] != 0:
                can.delete(ppos["lhx"])
                can.delete(ppos["lhy"])
            ppos["lhx"] = can.create_line(0,event.y,800,event.y,dash = (4,4),fill = "red")
            ppos["lhy"] = can.create_line(event.x,0,event.x,600,dash = (4,4),fill = "red")
        elif shape == "polygon":
            pcoords.append([event.x,event.y])

def b3press(event):
    global pcoords,temps,cshapelist
    if shape == "polygon" and pcoords != []:
        pcoords.append([event.x,event.y])
        can.delete(temp)
        cshapelist.append(polygon(can,pcoords,fill=oldcl,outline=oldcl,tag=ltags,acenter=point(pcoords[0][0],pcoords[0][1])))
        pcoords = []
        if temps != []:
            for i in temps:
                can.delete(i)
        temps = []

def motion(event):
    global temps
    if shape != "select" and tempbox != []:
        for i in tempbox:
            can.delete(i)
    if temps != []:
        for i in temps:
            can.delete(i)
            temps = []
    if shape == "polygon":
        tempcoords = copy.copy(pcoords)
        tempcoords.append([event.x,event.y])
        if len(tempcoords) >= 2:
            for i in range(len(tempcoords)-1):
                temps.append(can.create_line(tempcoords[i][0],tempcoords[i][1],tempcoords[i+1][0],tempcoords[i+1][1]))
    elif shape == "select":
        l1 = can.find_withtag("current")
        if l1 != ():
            for i in l1:
                if "selectl" in can.gettags(i) or "selectr" in can.gettags(i):
                    can.config(cursor="sb_h_double_arrow")
                elif "selectt" in can.gettags(i) or "selectb" in can.gettags(i):
                    can.config(cursor="sb_v_double_arrow")
                else:
                    can.config(cursor="arrow")
        else:
            can.config(cursor="arrow")
    elif shape == "center" or shape == "right hand" or shape == "left hand":
        temps.append(can.create_line([event.x,0,event.x,600],dash=(4,4)))
        temps.append(can.create_line([0,event.y,800,event.y],dash=(4,4)))
            
def b1rele(event):
    global temp,shapelist,cshapelist,wexit,iwexit,selarea
    if toff == False:
        if shape == "rectangle":
            cshapelist.append(polygon(can,[[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]],fill=oldcl,outline=oldcl,tag=ltags,acenter=point(firstx,firsty)))
            can.delete(temp)
            temp = 0
        elif shape == "line":
            cshapelist.append(polygon(can,[[firstx,firsty],[event.x,event.y]],fill=oldcl,outline=oldcl,tag=ltags,acenter=point(firstx,firsty)))
            can.delete(temp)
            temp = 0
        elif shape == "oval":
            cshapelist.append(ovalpol([firstx,firsty,event.x,event.y],fill=oldcl,outline=oldcl,tags=ltags))
            can.delete(temp)
            temp = 0
        elif shape == "exit":
            cshapelist.append(polygon(can,[[firstx,firsty],[event.x,firsty],[event.x,event.y],[firstx,event.y]],fill=oldcl,outline=oldcl,tag=("exit",wexit),acenter=point(firstx,firsty)))
            can.delete(temp)
            temp = 0
            dia(wexit)
            iwexit += 1
            wexit = "exit"+str(iwexit)
        elif shape == "select":
            can.addtag_enclosed("selected",firstx,firsty,event.x,event.y)
            can.delete(temp)
            addtagtocsl([firstx,firsty,event.x,event.y])
            makeselectbox(firstx,firsty,event.x,event.y)

def addtagtocsl(coords):
    global cshapelist
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.tags.append("selected")

def b1motion(event):
    global temp
    if toff == False:
        if shape == "rectangle" or shape == "hitbox" or shape == "select" or shape == "exit":
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
        elif shape == "oval":
            if temp == 0:
                temp = can.create_oval(firstx,firsty,event.x,event.y)
            else:
                can.delete(temp)
                temp = can.create_oval(firstx,firsty,event.x,event.y)

############################################################################
#######SELECT_FUNCTIONS######SELECT_FUNCTIONS#######SELECT_FUNCTIONS########
############################################################################

def makeselectbox(x1,y1,x2,y2):
    global tempbox,selarea
    tempbox = []
    tempbox.append(polygon(can,[[x1,y1],[x1,y2]],tag="selectl",fill="black",outline="black"))
    tempbox.append(polygon(can,[[x1,y1],[x2,y1]],tag="selectt",fill="black",outline="black"))
    tempbox.append(polygon(can,[[x2,y1],[x2,y2]],tag="selectr",fill="black",outline="black"))
    tempbox.append(polygon(can,[[x1,y2],[x2,y2]],tag="selectb",fill="black",outline="black"))
    selarea = [x1,y1,x2,y2]
    can.tag_bind("selectl","<Button-1>",lscale1)
    can.tag_bind("selectr","<Button-1>",rscale1)
    can.tag_bind("selectt","<Button-1>",tscale1)
    can.tag_bind("selectb","<Button-1>",bscale1)
    can.tag_bind("selectl","<B1-Motion>",lscale2)
    can.tag_bind("selectr","<B1-Motion>",rscale2)
    can.tag_bind("selectt","<B1-Motion>",tscale2)
    can.tag_bind("selectb","<B1-Motion>",bscale2)
    can.tag_bind("selected","<Button-1>",selmove1)
    can.tag_bind("selected","<B1-Motion>",selmove2)

def nc(coords):
    newcoords = []
    for i in range(int(len(coords)/2)):
        newcoords.append([coords[i*2]+50,coords[i*2+1]+50])
    return(newcoords)

def findbbox(cop):
    lx = cop[0][0][0][0]
    hx = cop[0][0][0][0]
    ly = cop[0][0][0][1]
    hy = cop[0][0][0][1]
    for x in cop:
        for i in x[0]:
            if i[0] <= lx:
                lx = i[0]
            elif i[0] >= hx:
                hx = i[0]
            if i[1] <= ly:
                ly = i[1]
            elif i[1] >= hy:
                hy = i[1]
    return([lx,ly,hx,hy])

def fcopy(event):
    global copied
    copied = []
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            coords = nc(can.coords(i.tk))
            tags = can.gettags(i.tk)
            fill = can.itemconfig(i.tk)["fill"][4]
            copied.append([coords,tags,fill])

def paste(event):
    global tempbox,selarea
    can.dtag("selected","selected")
    for i in tempbox:
        i.destroy(can)
    for i in copied:
        cshapelist.append(polygon(can,i[0],fill=i[2],outline=i[2],tag=i[1],acenter=point(i[0][0][0],i[0][0][1])))
    l1 = findbbox(copied)
    if tempbox != []:
        for i in tempbox:
            can.delete(i)
        tempbox = []
    selarea = l1
    makeselectbox(l1[0]-20,l1[1]-20,l1[2]+20,l1[3]+20)

def deleteselected(event):
    td = []
    for i in range(len(cshapelist)):
        if "selected" in can.gettags(cshapelist[i].tk):
            td.append(i)
    td.sort()
    td = td[::-1]
    for i in td:
        can.delete(cshapelist[i].tk)
        del(cshapelist[i])
    for i in tempbox:
        can.delete(i)

############################################################################
#######SCALING_FUNCTIONS#####SCALING_FUNCTIONS#####SCALING_FUNCTIONS#######
############################################################################

def lscale1(event):
    global sfirstx,width
    sfirstx = event.x
    for i in can.find_withtag("selectt"):
        l1 = can.coords(i)
        width = l1[0]-l1[2]
    if width <= 0:
        width *= -1

def lscale2(event):
    global sfirstx,width
    for i in can.find_withtag("selectl"):
        can.move(i,event.x-sfirstx,0)
    for i in can.find_withtag("selectt"):
        l1 = can.coords(i)
        newwidth = l1[0]-l1[2]
        can.coords(i,l1[0]+(event.x-sfirstx),l1[1],l1[2],l1[3])
    for i in can.find_withtag("selectb"):
        l1 = can.coords(i)
        can.coords(i,l1[0]+(event.x-sfirstx),l1[1],l1[2],l1[3])
        l1 = can.coords(i)
    if newwidth <= 0:
        newwidth *= -1
    l2 = newwidth/width
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.hvscale(can,l2,1,point(l1[0],l1[1]))
            i.move(can,event.x-sfirstx,0)
    sfirstx = event.x
    width = newwidth

def rscale1(event):
    global sfirstx,width
    sfirstx = event.x
    for i in can.find_withtag("selectt"):
        l1 = can.coords(i)
        width = l1[0]-l1[2]
    if width <= 0:
        width *= -1

def rscale2(event):
    global sfirstx,width
    for i in can.find_withtag("selectr"):
        can.move(i,event.x-sfirstx,0)
    for i in can.find_withtag("selectt"):
        l1 = can.coords(i)
        newwidth = l1[0]-l1[2]
        can.coords(i,l1[0],l1[1],l1[2]+(event.x-sfirstx),l1[3])
    for i in can.find_withtag("selectb"):
        l1 = can.coords(i)
        can.coords(i,l1[0],l1[1],l1[2]+(event.x-sfirstx),l1[3])
        l1 = can.coords(i)
    if newwidth <= 0:
        newwidth *= -1
    if width == 0:
        width += 0.1
    l2 = newwidth/width
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.hvscale(can,l2,1,point(l1[2],l1[3]))
            i.move(can,event.x-sfirstx,0)
    sfirstx = event.x
    width = newwidth

def tscale1(event):
    global sfirsty,height
    sfirsty = event.y
    for i in can.find_withtag("selectl"):
        l1 = can.coords(i)
        height = l1[1]-l1[3]
    if height <= 0:
        height *= -1

def tscale2(event):
    global sfirsty,height
    for i in can.find_withtag("selectt"):
        can.move(i,0,event.y-sfirsty)
    for i in can.find_withtag("selectr"):
        l1 = can.coords(i)
        newheight = l1[1]-l1[3]
        can.coords(i,l1[0],l1[1]+(event.y-sfirsty),l1[2],l1[3])
    for i in can.find_withtag("selectl"):
        l1 = can.coords(i)
        can.coords(i,l1[0],l1[1]+(event.y-sfirsty),l1[2],l1[3])
        l1 = can.coords(i)
    if newheight <= 0:
        newheight *= -1
    if height == 0:
        height += 0.1
    l2 = newheight/height
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.hvscale(can,1,l2,point(l1[0],l1[1]))
            i.move(can,0,event.y-sfirsty)
    sfirsty = event.y
    height = newheight

def bscale1(event):
    global sfirsty,height
    sfirsty = event.y
    for i in can.find_withtag("selectl"):
        l1 = can.coords(i)
        height = l1[1]-l1[3]
    if height <= 0:
        height *= -1

def bscale2(event):
    global sfirsty,height
    for i in can.find_withtag("selectb"):
        can.move(i,0,event.y-sfirsty)
    for i in can.find_withtag("selectr"):
        l1 = can.coords(i)
        newheight = l1[1]-l1[3]
        can.coords(i,l1[0],l1[1],l1[2],l1[3]+(event.y-sfirsty))
    for i in can.find_withtag("selectl"):
        l1 = can.coords(i)
        can.coords(i,l1[0],l1[1],l1[2],l1[3]+(event.y-sfirsty))
        l1 = can.coords(i)
    if newheight <= 0:
        newheight *= -1
    if height == 0:
        height += 0.1
    l2 = newheight/height
    for i in cshapelist:
        if "selected" in can.gettags(i.tk):
            i.hvscale(can,1,l2,point(l1[2],l1[3]))
            i.move(can,0,event.y-sfirsty)
    sfirsty = event.y
    height = newheight

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
    nil.append(i)
    il.append(["id"+str(ids),item(can,copy.deepcopy(dictionaries.idic[i]),et="id"+str(ids))])
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
    savebut = tkinter.Button(text="save",command=savelocations)
    savebut.place(x=500,y=50,width=60,height=50)
    backbut = tkinter.Button(text="Back",command=backtomenu)
    backbut.place(x=800,y=20,width=200,height=100)
    usedids = []
    x = dictionaries.ildic["il"+bg]
    for i in range(len(x)):
        il.append([x[i][3],item(can,copy.deepcopy(dictionaries.idic[x[i][0]]),et=x[i][3])])
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
            if tid in can.gettags(x.tk):
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
            if tid in can.gettags(x.tk):
                ns = "[\""+y[2]+"\","+str(cx+xoff)+","+str(cy+yoff)+",\""+str(tid)+"\"],"
                td = []
                for i in range(len(litems)):
                    if ns[-7:] == litems[i][-7:]:
                        td.append(i)
                for i in td:
                    del(litems[i])
    litems.append(ns)

def savelocations():
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
    if list(c[-1])[-1] != "\n":
        c[-1] += "\n"
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
    for i in range(len(x)):
        x[i] = x[i].split(" ")[0]
    icdia(x)

def icdia(items):
    global diaopen,wic
    if diaopen == False:
        diaopen = True
        wic = tkinter.Tk()
        wic.geometry("500x500")
        wic.wm_title("Choose Item")
        itembuts = []
        itemchoice = CHOICE(wic,items,20,20,460,460,loaditem)

#############FOR_SPRITE_MODE################

def pvalidate(p):
    if p != [0,0]:
        return(True)
    else:
        return(False)

def scldia():
    global diaopen
    boxwidth = ebw.get()
    boxheight = ebh.get()
    if pvalidate(center) and pvalidate(rh) and pvalidate(lh) and validate(boxwidth) and validate(boxheight):
        ssl = csltossl()
        ssl.append(lh)
        ssl.append(rh)
        ssl.append(center)
        ssl.append(int(boxwidth))
        ssl.append(int(boxheight))
        finalout = name +" = " +str(ssl)
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

#############To_Display_Error_Messages##########

def cleb():
    global diaopen
    errorb.destroy()
    diaopen = False

def errorbox(errors):
    global errorb,diaopen
    if diaopen == False:
        diaopen = True
        errorb = tkinter.Tk()
        errorb.geometry("300x300")
        errorb.wm_title("Error")
        errort = tkinter.Label(errorb,text=errors)
        errort.place(x=10,y=10,width=280,height=220)
        okay = tkinter.Button(errorb,text="Okay",command=cleb)
        okay.place(x=120,y=250,width=60,height=30)

#############FOR_BACKGROUND_MODE################

def cldia(wexit):
    global diaopen,exitstring
    nx = xoff
    ny = yoff
    if nx <= 0:
        nx = 0
    elif nx >= width-800:
        nx = width-800
    if ny <= 0:
        ny = 0
    elif ny >= height-600:
        ny = height-600
    nx *= -1
    ny *= -1
    exitstring += "\""+wexit+"\":[\""+bgent.get()+"\",\""+exent.get()+"\",["+str(nx)+","+str(ny)+"],"+str(expos.get())+"],"
    gexit.destroy()
    diaopen = False

def dia(wexit):
    global gexit,diaopen,bgent,exent,expos
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
        xtext = tkinter.Label(gexit,text="Spawn:")
        xtext.place(x=40,y=180,height=30,width=100)
        expos = tkinter.IntVar()
        expos.set(0)
        x = tkinter.Radiobutton(gexit,text="above",variable=expos,value=0)
        x.place(x=20,y=220,width=70,height=30)
        x = tkinter.Radiobutton(gexit,text="below",variable=expos,value=1)
        x.place(x=100,y=220,width=70,height=30)
        x = tkinter.Radiobutton(gexit,text="left",variable=expos,value=2)
        x.place(x=20,y=260,width=70,height=30)
        x = tkinter.Radiobutton(gexit,text="right",variable=expos,value=3)
        x.place(x=100,y=260,width=70,height=30)
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
def ovalpol(c,steps=50,fill="red",outline="",tags=""):
    xc = c[0] + (c[2]-c[0])/2
    yc = c[1] + (c[3]-c[1])/2
    p1 = point(c[0],c[1])
    center = point(xc,yc)
    pointlist = []
    dx = c[0]-c[2]
    dy = c[1]-c[3]
    xscale = 1
    yscale = 1
    if dx < 0:
        dx*=-1
    if dy < 0:
        dy*=-1
    if dx>dy:
        yscale *= dy/dx
        nx = c[0]
        ny = yc
    else:
        xscale *= dx/dy
        nx = xc
        ny = c[1]
    for i in range(steps):
        p2 = point(nx,ny)
        p2.rotate(center,i/steps*360)
        p2.hvscale(hfactor=xscale,vfactor=yscale,center=point(xc,yc))
        pointlist.append([round(p2.x),round(p2.y)])
    x = polygon(can,pointlist,fill=fill,outline=outline,tag=tags,acenter=p1)
    return(x)


def start(atype,image=False):
    global itype,il,shape,colour,tags,nil,width,height,ltags,name,cbd,oldcl,buttonlist,selectbut,rectbut,exitbut,polybut,linebut,centbut,lhbut,rhbut
    global tagbut,ctagbut,tagent,tagtext,nameent,namebut,nametext,e1ent,e2ent,e3ent,e4ent,e5ent,ebut,xent,yent,setbut,cshape,can,center,temp,pcoords
    global shapelist,cshapelist,boxsize,xoff,yoff,placeitembut,selarea,toff,sbut,nsbut,lo,ro,uo,bo,tempbox,copied,temps,lh,rh,keyset,hitbox,iwexit,wexit
    global exitstring,diaopen,ppos,choose,rvn,stop,ovalbut,ang,bgimage
    stop = False
    ang = True
    ppos = {"centerx":0,"centery":0,"lhx":0,"lhy":0,"rhx":0,"rhy":0}
    rh = [0,0]
    lh = [0,0]
    keyset = [0,0,0,0]
    hitbox = [0,0,0,0]
    iwexit = 1
    wexit = "exit"+str(iwexit)
    exitstring = ",{"
    diaopen = False
    temps = []
    tempbox = []
    copied = []
    toff = False
    il = []
    xoff = 0
    selarea = [0,0,0,0]
    yoff = 0
    if atype == "background":
        dunnoyet = 0
    else:
        oldcl = hexrgb(0,0,0)
        destroyinterface()
    window.bind_all("<Up>",uppr)
    window.bind_all("<KeyRelease-Up>",upre)
    window.bind_all("<Down>",downpr)
    window.bind_all("<KeyRelease-Down>",downre)
    window.bind_all("<Left>",leftpr)
    window.bind_all("<KeyRelease-Left>",leftre)
    window.bind_all("<Right>",rightpr)
    window.bind_all("<KeyRelease-Right>",rightre)
    window.bind_all("<Control-c>",fcopy)
    window.bind_all("<Control-v>",paste)
    if atype != "place item":
        backbut = tkinter.Button(text="Back",command=backtomenu)
        backbut.place(x=800,y=20,width=200,height=100)
        can = tkinter.Canvas()
        can.place(x=220,y=180,width=800,height=600)
        lo = tkinter.Button()
        lo.place(x=200,y=160,height=640,width=20)
        ro = tkinter.Button()
        ro.place(x=1020,y=160,height=640,width=20)
        uo = tkinter.Button()
        uo.place(x=200,y=160,height=20,width=840)
        bo = tkinter.Button()
        bo.place(x=200,y=780,height=20,width=840)
        savebut = tkinter.Button(text="save",command=fprint)
        savebut.place(x=500,y=50,width=60,height=50)
        shape = "rectangle"
        itype = atype
        colour = "red"
        tags = ""
        ltags = []
        cbd = {}
        x = 5
        cshapelist = []
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
        rectbut = tkinter.Button(window,text="rectangle",command=frect)
        rectbut.place(x=5,y=105,width=60,height=50)
        rectbut.config(relief="sunken")
        polybut = tkinter.Button(window,text="polygon",command=fpoly)
        polybut.place(x=5,y=50,width=60,height=50)
        ovalbut = tkinter.Button(window,text="oval",command=foval)
        ovalbut.place(x=70,y=50,width=60,height=50)
        linebut = tkinter.Button(window,text="line",command=fline)
        linebut.place(x=5,y=160,width=60,height=50)
        if itype == "background":
            cshapelist.append(polygon(can,[[0,0],[width,0],[width,height],[0,height]],fill=oldcl,outline=oldcl))
            exitbut = tkinter.Button(window,text="exit",command=fbexit)
            exitbut.place(x=70,y=105,width=60,height=50)
            selectbut = tkinter.Button(window,text="Select",command=fselect)
            selectbut.place(x=70,y=160,width=60,height=50)
            sbut = tkinter.Button(window,text="Solid",command=fsolid)
            sbut.place(x=5,y=215,width=60,height=50)
            nsbut = tkinter.Button(window,text="Walkable",command=fnsolid)
            nsbut.place(x=70,y=215,width=60,height=50)
            nsbut.config(relief="sunken")
        elif itype == "sprite" or itype == "item":
            centbut = tkinter.Button(window,text="center",command=fcent)
            centbut.place(x=70,y=105,width=60,height=50)
            selectbut = tkinter.Button(window,text="Select",command=fselect)
            selectbut.place(x=5,y=215,width=60,height=50)
            if itype == "sprite":
                rhbut = tkinter.Button(window,text="right\nhand",command=frh)
                rhbut.place(x=70,y=160,width=60,height=50)
                lhbut = tkinter.Button(window,text="left\nhand",command=flh)
                lhbut.place(x=70,y=215,width=60,height=50)
            elif itype == "item":
                ltags = ["item",name]
        cshape = rectbut
        center = [0,0]
        temp = 0
        pcoords = []
        shapelist = []
        boxsize = 50
        window.bind_all("<KeyPress-Delete>",deleteselected)
        can.bind("<Button-1>",b1press)
        can.bind("<ButtonRelease-1>",b1rele)
        can.bind("<B1-Motion>",b1motion)
        can.bind("<Button-3>",b3press)
        can.bind("<Motion>",motion)
        if image == True:
            bgimage = can.create_image(0,0,image=im,anchor="nw")
        selarea = [0,0,0,0]
        main()
    else:
        file = open("backgrounds.py","r")
        x = file.readlines()
        window.bind_all("<KeyPress-Delete>",deleteitem)
        file.close()
        backbut = tkinter.Button(text="Back",command=backtomenu)
        backbut.place(x=800,y=20,width=200,height=100)
        bglist = []
        nil = []
        for i in x:
            bglist.append(i.split(" ")[0])
        choose = CHOICE(window,bglist,50,50,600,500,loadbg,bw=100)

def loadbg(sbg):
    global nbg,bg,litems,ids,can
    choose.destroy()
    can = tkinter.Canvas()
    can.place(x=220,y=180,width=800,height=600)
    lo = tkinter.Button()
    lo.place(x=200,y=160,height=640,width=20)
    ro = tkinter.Button()
    ro.place(x=1020,y=160,height=640,width=20)
    uo = tkinter.Button()
    uo.place(x=200,y=160,height=20,width=840)
    bo = tkinter.Button()
    ids = 1
    litems = []
    bg = sbg
    x = copy.deepcopy(dictionaries.bgdic[bg])
    exits = x.pop()
    dimensions = x[-1]
    nbg = background(can,x)
    loaditems(bg)
    ichoice = tkinter.Button(text="Choose Item",command=lambda i=bg:fichoice(sbg))
    ichoice.place(x=650,y=50,width=100,height=50)
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
    global xoff,yoff,ang,xg,yg,cshapelist
    try:
        if can.find_withtag("selected") == ():
            if keyset[0]==1:
                for i in cshapelist:
                    i.move(can,0,5)
                can.move(bgimage,0,5)
                yoff -= 5
            if keyset[1]==1:
                for i in cshapelist:
                    i.move(can,0,-5)
                can.move(bgimage,0,-5)
                yoff += 5
            if keyset[2]==1:
                for i in cshapelist:
                    i.move(can,5,0)
                can.move(bgimage,5,0)
                xoff -= 5
            if keyset[3]==1:
                for i in cshapelist:
                    i.move(can,-5,0)
                can.move(bgimage,-5,0)
                xoff += 5
        else:
            xg = 0
            yg = 0
            for i in tempbox:
                xg += can.coords(i.tk)[0]+can.coords(i.tk)[2]
                yg += can.coords(i.tk)[1]+can.coords(i.tk)[3]
            xg /= 8
            yg /= 8
            if keyset[2]==1:
                for i in cshapelist:
                    if "selected" in can.gettags(i.tk):
                        i.rotate(can,3,point(xg,yg))
                for i0 in tempbox:
                    i0.rotate(can,3,point(xg,yg))
            if keyset[3]==1:
                for i in cshapelist:
                    if "selected" in can.gettags(i.tk):
                        i.rotate(can,-3,point(xg,yg))
                for i0 in tempbox:
                    i0.rotate(can,-3,point(xg,yg))
        window.after(7,main)
    except:
        pass


def bgotos(imageimported=False):
    global name,width,height
    name = interfacelist[0].get()
    width = interfacelist[1].get()
    height = interfacelist[2].get()
    if name != "" and validate(width) and validate(height):
        width = float(width)*800
        height = float(height)*600
        destroyinterface(True)
        if imageimported == False:
            start("background")
        else:
            return(True)
    else:
        return(False)

def spritetos(imageimported=False):
    global name
    name = interfacelist[0].get()
    if name != "":
        destroyinterface()
        if imageimported == False:
            start("sprite")
        else:
            return(True)
    else:
        return(False)

def itemtos(imageimported=False):
    global name
    name = interfacelist[1].get()
    if name != "":
        destroyinterface()
        if imageimported == False:
            start("item")
        else:
            return(True)
    else:
        return(False)

def selectbgimage():
    global imagechoice
    if bgotos(True):
        imagechoice = CHOICE(window,os.listdir(bgid),50,50,800,700,importbgimage)

def selectspriteimage():
    global imagechoice
    if spritetos(True):
        imagechoice = CHOICE(window,os.listdir(sid),50,50,800,700,importspriteimage)

def importbgimage(imname):
    global imagename,im
    imagechoice.destroy()
    imagename = ",\""+imname+"\""
    im = ImageTk.PhotoImage(Image.open(bgid+imname).resize((1600,1200),Image.ANTIALIAS))
    start("background",image=True)

def importspriteimage(imname):
    global imagename,im
    imagechoice.destroy()
    imagename = ",\""+imname+"\""
    im = ImageTk.PhotoImage(Image.open(sid+imname))
    start("sprite",image=True)

def loadspritetoanimate(j):
    print(j)

def backtomenu():
    for i in window.winfo_children():
        i.destroy()
    makedictionaries.fg()
    importlib.reload(dictionaries)
    mainmenu()

def mainmenu():
    global interfacelist
    interfacedata = [["b","draw a sprite",spriteoptions,0.1,0.1,0.35,0.2],["b","draw a background",bgoptions,0.1,0.35,0.35,0.2],["b","draw an item",itemoptions,0.1,0.6,0.35,0.2],["b","place items\non background",lambda i="place item":start(i),0.55,0.1,0.35,0.2],["b","make animations",animationoptions,0.55,0.35,0.35,0.2]]
    interfacelist = []
    createinterface(interfacedata)

def itemoptions():
    destroyinterface()
    interfacedata = [["b","Back",backtomenu,800,20,200,100],["e",0,0,400,50,200,40],["l","Item Name:",0,200,50,200,40],["b","Enter",itemtos,800,150,200,100]]
    createinterface(interfacedata,False)

def spriteoptions():
    destroyinterface()
    interfacedata = [["e",0,0,400,50,200,40],["b","Import Image",selectspriteimage,400,140,200,100],["b","back",backtomenu,800,20,200,100],["l","Sprite Name",0,200,50,200,40],["b","Enter",spritetos,800,150,200,100]]
    createinterface(interfacedata,False)

def bgoptions():
    destroyinterface()
    interfacedata = [["e",0,0,400,50,200,40],["e",0,0,400,120,200,40],["e",0,0,400,220,200,40],["l","Background Name:",0,200,50,200,40],["l","Background Width:\n(1=1 screen wide)\n(1.5=1.5 screens wide)\netc..",0,200,120,200,70],["l","Choose Background Colour",0,10,340,200,70],["l","Background Height:\n(1=1 screen tall)\n(1.5=1.5 screens tall)\netc..",0,200,220,200,70],["b","Import Image",selectbgimage,800,200,200,100],["b","Enter",bgotos,250,320,200,100],["b","back",backtomenu,800,20,200,100]]
    createinterface(interfacedata,False,True)

def animationoptions():
    destroyinterface()
    file = open("items.py","r")
    x = file.readlines()
    file.close()
    items = []
    for i in x:
        items.append(i.split(" ")[0])
    x = CHOICE(window,items,50,50,300,190,loadspritetoanimate)



window = tkinter.Tk()
window.geometry("1060x840")
window.wm_title("Paint")
ww = 1060
wh = 840
stop = False
window.bind_all("<Configure>",resize)

bgid = "./Images/backgrounds/"
sid = "./Images/sprites/"
iid = "./Images/iid/"
imagename = ""

mainmenu()
window.mainloop()
