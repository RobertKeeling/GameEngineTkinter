from tkinter import *

class player(object):

    def __init__(self,can,speed):
        self.speed = speed
        self.body = can.create_oval(400,300,500,400,fill="black",outline="tan",tags=("player"))
        self.rarm = can.create_oval(490,330,530,370,fill="red",outline="tan",tags=("player"))
        self.larm = can.create_oval(370,330,410,370,fill="red",outline="tan",tags=("player"))
        self.bodycoords = [400,300,500,400]
        self.rarmcoords = [self.bodycoords[0]+90,self.bodycoords[1]+30,self.bodycoords[2]+30,self.bodycoords[3]-30]
        self.larmcoords = [self.bodycoords[0]-30,self.bodycoords[1]+30,self.bodycoords[2]-90,self.bodycoords[3]-30]


    def move(self,can,keyset):
        x = [[0,-self.speed,0,-self.speed],[0,self.speed,0,self.speed],[-self.speed,0,-self.speed,0],[self.speed,0,self.speed,0]]
        y = [[1,0],[3,700],[0,0],[2,900]]
        k = keyset
        z = [[[[k[0],1],[k[2],1],[k[3],0],[k[1],0]],[[k[1],1],[k[3],1],[k[2],0],[k[0],0]]],[[[k[0],1],[k[2],0],[k[3],1],[k[1],0]],[[k[1],1],[k[3],0],[k[2],1],[k[0],0]]],[[[k[0],1],[k[3],0],[k[2],0],[0,0]],[[k[1],1],[k[3],0],[k[2],0],[0,0]]],[[[k[2],1],[k[0],0],[k[1],0],[0,0]],[[k[3],1],[k[0],0],[k[1],0],[0,0]]]]
        t = [[[80,0,20,-60],[-20,70,-80,10]],[[80,70,20,10],[-20,0,-80,-60]],[[90,30,30,-30],[-30,30,-90,-30]],[[30,90,-30,30],[30,10,-30,-130]]]
        #detects contact with solid objects
        a = can.find_withtag("solid")
        b = can.coords(self.body)
        c = [0,0,0,0]
        for i in a:
            p = can.coords(i)
            if b[0]-5 <= p[2] and b[2]+5 >= p[0] and b[1]-5 <= p[3] and b[3]+5 >= p[1]:
                if b[0]-5-p[2] < 10 and b[0]-5-p[2] > -10:
                    c[2] = "left"
                if b[2]+5-p[0] < 10 and b[2]+5-p[0] > -10:
                    c[3] = "right"
                if b[1]-5-p[3] < 10 and b[1]-5-p[3] > -10:
                    c[0] = "top"
                if b[3]+5-p[1] < 10 and b[3]+5-p[1] > -10:
                    c[1] = "bottom"
        #detects contact with exit
        a = can.find_withtag("exit")
        b = can.coords(self.body)
        d = [0,0,0,0]
        for i in a:
            p = can.coords(i)
            if b[0]-5 <= p[2] and b[2]+5 >= p[0] and b[1]-5 <= p[3] and b[3]+5 >= p[1]:
                if b[0]-5-p[2] < 10 and b[0]-5-p[2] > -10:
                    d[2] = "left"
                if b[2]+5-p[0] < 10 and b[2]+5-p[0] > -10:
                    d[3] = "right"
                if b[1]-5-p[3] < 10 and b[1]-5-p[3] > -10:
                    d[0] = "top"
                if b[3]+5-p[1] < 10 and b[3]+5-p[1] > -10:
                    d[1] = "bottom"
        # moves room according to with exit is reached
        for i in d:
            if i != 0:
                print(i)
        for i in range(4):
            check = False
            if (z[i][0][0][0] == z[i][0][0][1] and z[i][0][1][0] == z[i][0][1][1]and z[i][0][2][0] == z[i][0][2][1]and z[i][0][3][0] == z[i][0][3][1]) or (z[i][1][0][0] == z[i][1][0][1] and z[i][1][1][0] == z[i][1][1][1] and z[i][1][2][0] == z[i][1][2][1] and z[i][1][3][0] == z[i][1][3][1]):
                check = True
            if check == True:
                self.larmcoords = self.bodycoords[0]+t[i][1][0],self.bodycoords[1]+t[i][1][1],self.bodycoords[2]+t[i][1][2],self.bodycoords[3]+t[i][1][3]
                self.rarmcoords = self.bodycoords[0]+t[i][0][0],self.bodycoords[1]+t[i][0][1],self.bodycoords[2]+t[i][0][2],self.bodycoords[3]+t[i][0][3]
                can.coords(self.rarm,self.rarmcoords[0],self.rarmcoords[1],self.rarmcoords[2],self.rarmcoords[3])
                can.coords(self.larm, self.larmcoords[0],self.larmcoords[1],self.larmcoords[2],self.larmcoords[3])
                coords = [self.bodycoords,self.rarmcoords,self.larmcoords]
            if (keyset[i] == 1 and ((self.bodycoords[y[i][0]] >= y[i][1] and (i==0 or i==2)) or (self.bodycoords[y[i][0]] <= y[i][1] and (i==1 or i==3)))) and c[i]==0:
                self.bodycoords = self.bodycoords[0]+x[i][0],self.bodycoords[1]+x[i][1],self.bodycoords[2]+x[i][2],self.bodycoords[3]+x[i][3]
                can.coords(self.body,self.bodycoords[0],self.bodycoords[1],self.bodycoords[2],self.bodycoords[3])
                self.larmcoords = self.larmcoords[0]+x[i][0],self.larmcoords[1]+x[i][1],self.larmcoords[2]+x[i][2],self.larmcoords[3]+x[i][3]
                can.coords(self.larm, self.larmcoords[0],self.larmcoords[1],self.larmcoords[2],self.larmcoords[3])
                self.rarmcoords =  self.rarmcoords[0]+x[i][0],self.rarmcoords[1]+x[i][1],self.rarmcoords[2]+x[i][2],self.rarmcoords[3]+x[i][3]
                can.coords(self.rarm,self.rarmcoords[0],self.rarmcoords[1],self.rarmcoords[2],self.rarmcoords[3])
        coords = [self.bodycoords,self.rarmcoords,self.larmcoords]
        return(coords)




#left top right bottom
