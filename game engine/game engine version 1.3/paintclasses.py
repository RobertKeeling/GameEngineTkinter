import tkinter

class CHOICE(object):
    def __init__(self,window,items,x,y,width,height,acommand,bw=80,bh=40,ygap=20,xgap=20):
        self.buttonlist = []
        self.window = window
        self.items = items
        self.command = acommand
        self.x = x
        self.lx = x
        self.hx = x+width
        self.ly = y
        self.hy = y+height
        self.y = y
        self.bw = bw
        self.bh = bh
        self.xgap = xgap
        self.ygap = ygap
        self.itembook = []
        self.perscreen = int((width+xgap)/(bw+xgap))*int(((height+ygap)/(bh+ygap))-1)
        if len(self.items) > self.perscreen+(width+xgap)/(bw+xgap):
            while len(self.items) != 0:
                page = []
                if len(self.items) > self.perscreen:
                    l = self.perscreen
                else:
                    l = len(self.items)
                for i in range(l):
                    page.append(self.items.pop())
                self.itembook.append(page)
            self.booklength = len(self.itembook)-1
            self.pagenumber = 0
            self.draw(self.itembook[0])
        else:
            self.draw(self.items)


    def draw(self,items):
        if self.itembook == []:
            for i in items:
                if self.x+self.bw >= self.hx:
                    self.x = self.lx
                    self.y += self.bh+self.ygap
                self.buttonlist.append(tkinter.Button(self.window,text=i,command=lambda x=i:self.command(x)))
                self.buttonlist[-1].place(x=self.x,y=self.y,width=self.bw,height=self.bh)
                self.x += self.bw+self.xgap
        else:
            for i in self.itembook[self.pagenumber]:
                if self.x+self.bw >= self.hx:
                    hx = self.x-(self.bw+self.xgap)
                    self.x = self.lx
                    self.y += self.bh+self.ygap
                self.buttonlist.append(tkinter.Button(self.window,text=i,command=lambda x=i:self.command(x)))
                self.buttonlist[-1].place(x=self.x,y=self.y,width=self.bw,height=self.bh)
                self.x += self.bw+self.xgap
            if self.pagenumber != self.booklength:
                self.buttonlist.append(tkinter.Button(self.window,text="next",command=self.next))
                self.buttonlist[-1].place(x=hx,y=self.y+self.ygap+self.bh,width=self.bw,height=self.bh)
            if self.pagenumber != 0:
                self.buttonlist.append(tkinter.Button(self.window,text="back",command=self.back))
                self.buttonlist[-1].place(x=self.lx,y=self.y+self.ygap+self.bh,width=self.bw,height=self.bh)

    def next(self):
        for i in self.buttonlist:
            i.destroy()
        self.y = self.ly
        self.x = self.lx
        self.buttonlist = []
        self.pagenumber += 1
        self.draw(self.itembook[self.pagenumber])

    def back(self):
        for i in self.buttonlist:
            i.destroy()
        self.y = self.ly
        self.x = self.lx
        self.buttonlist = []
        self.pagenumber -= 1
        self.draw(self.itembook[self.pagenumber])
                

    def destroy(self):
        for i in self.buttonlist:
            i.destroy()
        del(self)
