#IMPORTING MODULES

import tkinter
from backgrounds import *
from classes import *
from functions import *

#DEFINING FUNCTIONS FOR KEYBINDINGS

def uppressed(key):
    keyset[0] = 1
def upreleased(key):
    keyset[0] = 0
def downpressed(key):
    keyset[1] = 1
def downreleased(key):
    keyset[1]= 0
def leftpressed(key):
    keyset[2] = 1
def leftreleased(key):
    keyset[2] = 0
def rightpressed(key):
    keyset[3] = 1
def rightreleased(key):
    keyset[3] = 0

#SETTING GLOBAL VARIABLES

window = tkinter.Tk()
window.geometry("900x700")
can = tkinter.Canvas()
can.place(relx=0,rely=0,relwidth=1,relheight=1)

                        #TEMP REDIFINE INTO BACKGROUND CLASS AT LATER DATE
room1(can)
                        #TEMP REDIFINE INTO BACKGROUND CLASS AT LATER DATE

can.addtag_all("all")
player1 = player(can,6)
keyset = [0,0,0,0]


#CONFIGURING KEYBDINGS

window.bind_all("<Up>",uppressed)
window.bind_all("<KeyRelease-Up>",upreleased)
window.bind_all("<Down>",downpressed)
window.bind_all("<KeyRelease-Down>",downreleased)
window.bind_all("<Left>",leftpressed)
window.bind_all("<KeyRelease-Left>",leftreleased)
window.bind_all("<Right>",rightpressed)
window.bind_all("<KeyRelease-Right>",rightreleased)


        


#DEFINING GAME LOOP

def game():
    player1.move(can,keyset)
    window.after(7,game)

#CALLING GAME AND MAINLOOP

game()
window.mainloop()

