import math
import tkinter
import items
from PIL import Image,ImageTk

class point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x += x
        self.y += y

    def scale(self,center,factor):
        self.x -= center.x
        self.y -= center.y
        self.x *= factor
        self.y *= factor
        self.x += center.x
        self.y += center.y

    def hvscale(self,hfactor,vfactor,center=False):
        if center == False:
            self.x *= hfactor
            self.y *= vfactor
        else:
            self.x -= center.x
            self.y -= center.y
            self.x *= hfactor
            self.y *= vfactor
            self.x += center.x
            self.y += center.y

    def rotate(self,center,angle,degrees=True):
        if degrees==True:
            angle = math.radians(angle)
        newx = center.x+(math.cos(angle)*(self.x-center.x)-math.sin(angle)*(self.y-center.y))
        self.y = center.y+(math.sin(angle)*(self.x-center.x)+math.cos(angle)*(self.y-center.y))
        self.x = newx

    def repos(self,x,y):
        self.x = x
        self.y = x

class center(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

class DEGREE(object):
    def __init__(self,v=0):
        self.value = v

    def bound(self):
        if self.value < 0:
            self.value*=-1
        if self.value > 90:
            self.value%=90


class polygon(object):
    def __init__(self,can,points,fill="red",outline="red",acenter=False,tag=""):
        self.points = []
        self.pointint = []
        self.fill = fill
        self.outline = outline
        if isinstance(tag,tuple):
            tag = list(tag)
        self.tags = tag
        for i in points:
            self.points.append(point(i[0],i[1]))
            self.pointint.append(int(i[0]))
            self.pointint.append(int(i[1]))
        if acenter != False:
            self.cenoff = [acenter.x-self.pointint[0],acenter.y-self.pointint[1]]
        else:
            self.cenoff = False
        self.p1 = point(self.pointint[0],self.pointint[1])
        self.tk = can.create_polygon(self.pointint,fill=self.fill,outline=self.outline,tags=self.tags)

    def move(self,can,x,y):
        self.p1.move(x,y)
        for i in self.points:
            i.move(x,y)
        for i in range(len(self.points)):
            self.pointint[2*i] = int((self.points[i].x))
            self.pointint[2*i+1] = int(self.points[i].y)
        can.coords(self.tk,tuple(self.pointint))

    def scale(self,can,factor,acenter="self"):
        if acenter == "self":
            if self.cenoff == False:
                acenter = center(self.p1.x,self.p1.y)
            else:
                acenter = center(self.p1.x+self.cenoff[0],self.p1.y+self.cenoff[1])
        self.p1.scale(acenter,factor)
        for i in range(len(self.points)):
            self.points[i].scale(acenter,factor)
        for i in range(len(self.points)):
            self.pointint[2*i] = int((self.points[i].x))
            self.pointint[2*i+1] = int(self.points[i].y)
        self.cenoff[0] *= factor
        self.cenoff[1] *= factor
        can.coords(self.tk,tuple(self.pointint))

    def hvscale(self,can,hfactor,vfactor,center=False):
        for i in self.points:
            i.hvscale(hfactor,vfactor,center)
        for i in range(len(self.points)):
            self.pointint[2*i] = int((self.points[i].x))
            self.pointint[2*i+1] = int(self.points[i].y)
        self.p1.hvscale(hfactor,vfactor,center)
        self.cenoff[0] *= hfactor
        self.cenoff[1] *= vfactor
        can.coords(self.tk,tuple(self.pointint))

    def rotate(self,can,angle,acenter="self",degrees=True):
        if acenter == "self":
            if self.cenoff==False:
                acenter = center(self.p1.x,self.p1.y)
            else:
                acenter = center(self.p1.x+self.cenoff[0],self.p1.y+self.cenoff[1])
        for i in self.points:
            i.rotate(acenter,angle,degrees)
        for i in range(len(self.points)):
            self.pointint[2*i] = int((self.points[i].x))
            self.pointint[2*i+1] = int(self.points[i].y)
        can.coords(self.tk,tuple(self.pointint))

    def dtag(self,tag):
        todel = []
        for i in range(len(self.tags)):
            if self.tags[i] == tag:
                todel.append(i)
        todel.sort()
        todel = todel[::-1]
        for i  in todel:
            del(self.tags[i])
            
    def destroy(self,can):
        can.delete(self.tk)
        del(self.points)
        del(self.pointint)

    def redraw(self,can):
        can.delete(self.tk)
        self.tk = can.create_polygon(self.pointint,fill=self.fill,outline=self.outline,tags=self.tags)


class background(object):
    def __init__(self,can,data):
        self.items = []
        self.dimensions = data.pop()
        if isinstance(data[-1],str):
            self.im = Image.open("./Images/backgrounds/"+data.pop())
            imr = self.im.resize((int(self.dimensions[0]),int(self.dimensions[1])),Image.ANTIALIAS)
            self.im2 = ImageTk.PhotoImage(imr)
        else:
            self.im2 = False
        for i in data:
            self.items.append(polygon(can,i[0],i[1],i[2],center(i[4][0],i[4][1]),i[3]))
        if self.im2 != False:
            self.tkimage = can.create_image(0,0,image=self.im2,anchor="nw")

    def move(self,can,x,y):
        for i in self.items:
            i.move(can,x,y)
        if self.im2 != False:
            can.move(self.tkimage,x,y)

    def hvscale(self,can,hfactor,vfactor,xoff=0,yoff=0):
        for i in self.items:
            i.hvscale(can,hfactor,vfactor)
        self.dimensions[0] *= hfactor
        self.dimensions[1] *= vfactor
        if self.im2 != False:
            imr = self.im.resize((int(self.dimensions[0]),int(self.dimensions[1])),Image.ANTIALIAS)
            self.im2 = ImageTk.PhotoImage(imr)
            can.delete(self.tkimage)
            self.tkimage = can.create_image(xoff,yoff,image=self.im2,anchor="nw")

class player(object):
    def __init__(self,can,data):
        self.items = []
        self.can = can
        self.boxheight = data.pop()
        self.boxwidth = data.pop()
        r = data.pop()
        self.center = point(r[0],r[1])
        r = data.pop()
        self.rh = point(r[0],r[1])
        r = data.pop()
        self.lh = point(r[0],r[1])
        self.inventory = []
        self.hitbox = [point(self.center.x-self.boxwidth,self.center.y+self.boxheight),point(self.center.x+self.boxwidth,self.center.y-self.boxheight)]
        for i in data:
            self.items.append(polygon(can,i[0],i[1],i[2],self.center,i[3]))

    def destroy(self):
        for i in self.items:
            i.destroy(self.can)
        del(self)

    def move(self,can,x,y):
        for i in self.hitbox:
            i.move(x,y)
        if self.detect(can,"solid") == []:
            for i in self.items:
                i.move(can,x,y)
            self.center.move(x,y)
            self.rh.move(x,y)
            self.lh.move(x,y)
        else:
            for i in self.hitbox:
                i.move(-x,-y)

    def scale(self,can,factor,acenter="self"):
        for i in self.items:
            i.scale(can,factor,acenter)
        self.rh.scale(self.center,factor)
        self.lh.scale(self.center,factor)

    def hvscale(self,can,hfactor,vfactor):
        for i in self.items:
            i.hvscale(can,hfactor,vfactor)
        self.center.hvscale(hfactor,vfactor)
        self.rh.hvscale(hfactor,vfactor)
        self.lh.hvscale(hfactor,vfactor)
        for i in self.hitbox:
            i.hvscale(hfactor,vfactor)

    def rotate(self,can,angle,acenter="self",degrees=True):
        for i in self.items:
            i.rotate(can,angle,self.center,degrees)
        if acenter != "self":
            self.center.rotate(acenter,angle)
            self.rh.rotate(acenter,angle)
            self.lh.rotate(acenter,angle)
        else:
            self.rh.rotate(self.center,angle)
            self.lh.rotate(self.center,angle)

    def detect(self,can,tag):
        overlapping = can.find_overlapping(self.hitbox[0].x,self.hitbox[0].y,self.hitbox[1].x,self.hitbox[1].y)
        detected = []
        for i in overlapping:
            q = can.gettags(i)
            for x in q:
                if x == tag:
                    detected.append(i)
        return(detected)

    def pickup(self,can):
        f = self.detect(can,"item")
        if f != []:
            e = can.gettags(f[0])
            can.delete(str(e[3]))
            self.inventory.append(e[2])

    def redraw(self,can,x=False,y=False):
        if x == False:
            x = self.center.x
        if y == False:
            y = self.center.y
        for i in self.items:
            i.redraw(can)
        movex = self.center.x-x
        movey = self.center.y-y
        for i in self.items:
            i.move(can,-movex,-movey)
        self.hitbox[0].x -= movex
        self.hitbox[0].y -= movey
        self.hitbox[1].x -= movex
        self.hitbox[1].y -= movey
        self.center.x -= movex
        self.center.y -= movey

class item(object):
    def __init__(self,can,data,et=False):
        self.items = []
        c = data.pop()
        self.center = point(c[0],c[1])
        if et != False:
            for i in data:
                i[3] = list(i[3])
                i[3].append(et)
                i[3] = tuple(i[3])
        for i in data:
            self.items.append(polygon(can,i[0],i[1],i[2],center(self.center.x,self.center.y),i[3]))

    def move(self,can,x,y):
        self.center.move(x,y)
        for i in self.items:
            i.move(can,x,y)

    def scale(self,can,factor,acenter="self"):
        for i in self.items:
            i.scale(can,factor,acenter)

    def hvscale(self,can,hfactor,vfactor):
        for i in self.items:
            i.hvscale(can,hfactor,vfactor)

    def rotate(self,can,angle,acenter="self",degrees=True):
        for i in self.items:
            i.rotate(can,angle,acenter,degrees)

    def repos(self,can,x,y):
        movex = self.center.x-x
        movey = self.center.y-y
        for i in self.items:
            i.move(can,-movex,-movey)
        self.center.x -= movex
        self.center.y -= movey
















