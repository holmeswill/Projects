# -*- coding: utf-8 -*-
import random
import tkinter
import numpy as np


#First we define some global varibles


overs=0
runs=0
wickets=10

#Set up for agressiveness
nuL=0
nuH=20
siL=nuH
siH=45
duL=siH
duH=75
trL=duH
trH=80
foL=trH
foH=95
sxL=foH
sxH=100


#This first bit sets up the window

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
 

#This is the textbox that is currently not needed       
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Enter text here")

#This sets up the button and points to OnButtonClick, sets up the label etc, this ahpends four times
        button = tkinter.Button(self,text="Bowl",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set("Total Runs:")

        self.labelVariable2 = tkinter.StringVar()
        label2 = tkinter.Label(self,textvariable=self.labelVariable2,
                              anchor="w",fg="black",bg="grey")
        label2.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable2.set("Total Overs:")

        self.labelVariable3 = tkinter.StringVar()
        label3 = tkinter.Label(self,textvariable=self.labelVariable3,
                              anchor="w",fg="black",bg="grey")
        label3.grid(column=0,row=3,columnspan=2,sticky='EW')
        self.labelVariable3.set("Wickets Remaining: " +str(wickets))
        
        self.labelVariable4 = tkinter.StringVar()
        label4 = tkinter.Label(self,textvariable=self.labelVariable4,
                              anchor="w",fg="black",bg="grey")
        label4.grid(column=0,row=4,columnspan=2,sticky='EW')
        self.labelVariable4.set("Status: ")

#this is about resizing the window

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

#This is the button click event

    def OnButtonClick(self):
        global runs, overs, wickets
              
        shot = random.randint(0,100) #shot gives a probablity to work with
        if shot in range(nuL,nuH):
            hit = 0
        if shot in range(siL,siH):
            hit=1
        if shot in range(duL,duH):
            hit=2
        if shot in range(trL,trH):
            hit=3
        if shot in range(foL,foH):
            hit=4
        if shot in range(sxL,sxH):
            hit =6
        out = random.randint(0,100)
        if out >= 90:
            wickets = wickets -1
            
        runs=runs+hit
        overs=overs+0.1
        self.labelVariable.set("Total Runs: "+str(runs))
        
        self.labelVariable2.set("Total Overs: "+str(np.round(overs,1)))
        self.labelVariable3.set("Wickets Remaining: "+str(wickets))
        self.labelVariable4.set("Status: You hit a "+str(hit))
        
        if wickets==1:
            self.labelVariable3.set("Wickets Remaining: "+" All Out!!")
            
    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+"you pressed enter")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Clickit')
    app.mainloop()
        






       
   

   
   

    
