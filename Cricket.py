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

Deffensive = [0,50,70,85,90,97,100]
Current=Deffensive

BatterChoices = [Deffensive, 'Moderate', 'Agresive']

#This first bit sets up the window

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        
        global BatterChoices
        
        
        self.grid()
 
             
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.OptionMenu(self,'this',BatterChoices)
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
        if shot in range(Current[0],Current[1]):
            hit = 0
        if shot in range(Current[1],Current[2]):
            hit=1
        if shot in range(Current[2],Current[3]):
            hit=2
        if shot in range(Current[3],Current[4]):
            hit=3
        if shot in range(Current[4],Current[5]):
            hit=4
        if shot in range(Current[5],Current[6]):
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
        






       
   

   
   

    
