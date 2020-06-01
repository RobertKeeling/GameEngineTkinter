import tkinter

main = tkinter.Tk()
main.geometry("900x700")

can = tkinter.Canvas()
can.place(relx=0,rely=0,relwidth=1,relheight=1)

solid = False
click = False
firstmove = True
rectangles = []
rectanglep = []
deletes = []
deletep = []
colour = "green"
shape = "rectangle"
exits = False

def gpressed(event):
    global colour
    colour = "green"
def ypressed(event):
    global colour
    colour = "yellow"
def ppressed(event):
    global colour
    colour = "purple"
def opressed(event):
    global colour
    colour = "orange"
def bpressed(event):
    global colour
    colour = "blue"
def rpressed(event):
    global colour
    colour = "red"
def npressed(event):
    global colour
    colour = "black"
def mpressed(event):
    global colour
    colour = "brown"
def wpressed(event):
    global colour
    colour = "white"
def tpressed(event):
    global solid
    solid = True
def upressed(event):
    global solid
    solid = False
def pressed1(event):
    global shape
    shape = "rectangle"
def pressed2(event):
    global shape
    shape = "oval"
def epressed(event):
    global exits
    exits = True
def qpressed(event):
    exits = False
    
def zpressed(event):
    global rectanglep,rectangles,deletes,deletep
    if rectanglep != []:
        x = rectangles.pop()
        can.delete(x)
        deletes.append(x)
        y = rectanglep.pop()
        deletep.append(y)

def xpressed(event):
    global rectanglep,rectangles,deletes,deletep
    if deletep != []:
        x = deletes.pop()
        y = deletep.pop()
        if str(y[5]) == "rectangle":
            rectangles.append(can.create_rectangle(y[0],y[1],y[2],y[3],fill=y[4]))
        if str(y[5]) == "oval":
            rectangles.append(can.create_oval(y[0],y[1],y[2],y[3],fill=y[4],outline=y[4],tags=(y[5]+y[6]+y[7])))
        rectanglep.append(y)

def printall(event):
    a = 0
    b = 0
    for i in rectanglep:
        if str(i[5]) == "rectangle":
            print('can.create_rectangle('+str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+',fill="'+str(i[4])+"\","+'outline="'+str(i[4])+'",tags=("'+str(i[5])+'","'+str(i[6])+'","'+str(i[7])+'"))')
            a = a+1
        elif str(i[5]) == "oval":
            print("can.create_oval("+str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+',fill="'+str(i[4])+'",'+'outline="'+str(i[4])+'",tags=("'+str(i[5])+'","'+str(i[6])+'","'+str(i[7])+'"))')
            b = b+1



def b1press(event):
    global click,firstx,firsty
    click = True
    firstx = event.x
    firsty = event.y

def b1release(event):
    global click,lastx,lasty,temp,firstmove,rectangles,rectanglep
    click = False
    firstmove = True
    can.delete(temp)
    lastx = event.x
    lasty = event.y
    print(exits)
    if shape == "rectangle":
        if exits == True:
            rectangles.append(can.create_rectangle(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","nsolid","exit")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"rectangle","background","exit"])
        elif solid == True:
            rectangles.append(can.create_rectangle(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","solid")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"rectangle","background","solid"])
        else:
            rectangles.append(can.create_rectangle(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","nsolid")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"rectangle","background","nsolid"])
    elif shape == "oval":
        if exits == True:
            rectangles.append(can.create_oval(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","solid","exit")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"oval","background","exit"])
        elif solid == True:
            rectangles.append(can.create_oval(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","solid")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"oval","background","solid"])
        else:
            rectangles.append(can.create_oval(firstx,firsty,lastx,lasty,fill=colour,outline=colour,tags=("background","solid")))
            rectanglep.append([firstx,firsty,lastx,lasty,colour,"oval","background","nsolid"])

def motion(event):
    global temp,firstmove
    if click == True:
        if firstmove == False:
            can.delete(temp)
        else:
            firstmove = False
        if shape == "rectangle":
            temp = can.create_rectangle(firstx,firsty,event.x,event.y)
        elif shape == "oval":
            temp = can.create_oval(firstx,firsty,event.x,event.y)

main.bind_all("<Button-1>",b1press)
main.bind_all("<ButtonRelease-1>",b1release)
main.bind_all("<B1-Motion>",motion)
main.bind_all("g",gpressed)
main.bind_all("y",ypressed)
main.bind_all("p",ppressed)
main.bind_all("e",epressed)
main.bind_all("o",opressed)
main.bind_all("b",bpressed)
main.bind_all("r",rpressed)
main.bind_all("n",npressed)
main.bind_all("w",wpressed)
main.bind_all("m",mpressed)
main.bind_all("z",zpressed)
main.bind_all("x",xpressed)
main.bind_all("t",tpressed)
main.bind_all("u",upressed)
main.bind_all("1",pressed1)
main.bind_all("2",pressed2)
main.bind_all("<Return>",printall)


main.mainloop()
