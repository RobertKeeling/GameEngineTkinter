import tkinter


def buildcanvas():
    can = tkinter.Canvas()
    can.place(relx=0,rely=0,relwidth=1,relheight=1)
    return(can)

def buildwindow(width,height):
    main = tkinter.Tk()
    main.geometry(str(width)+"x"+str(height))
    return(main)
