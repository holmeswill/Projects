#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:48:23 2017

@author: will
"""

import tkinter as tk
import random
import numpy as np

batter1={'name':'one','Ave':50,'SR':50,'Score':0}
batter2={'name':'two','Ave':45,'SR':50,'Score':0}
batter3={'name':'three','Ave':40,'SR':50,'Score':0}
batter4={'name':'four','Ave':35,'SR':50,'Score':0}
batter5={'name':'five','Ave':30,'SR':50,'Score':0}
batter6={'name':'six','Ave':25,'SR':50,'Score':0}
batter7={'name':'seven','Ave':20,'SR':50,'Score':0}
batter8={'name':'eight','Ave':15,'SR':50,'Score':0}
batter9={'name':'nine','Ave':10,'SR':50,'Score':0}
batter10={'name':'ten','Ave':5,'SR':50,'Score':0}
batter11={'name':'eleven','Ave':0,'SR':50,'Score':0}


team1=[batter1,batter2,batter3,batter4,batter5,batter6,batter7,batter8,batter9,batter10,batter11]

Deffensive = [0,50,70,85,90,97,100]
Modderate = [0,20,40,60,70,90,100]
Agressive = [0,10,20,30,40,80,100]
Current=Deffensive
Cteam=team1
Cbatter=Cteam[0]
Abatter=Cteam[1]
overs=0
runs=0
wickets=10
hit=0
out=0

mod1=50




def teambox():
    teambox=tk.Tk()
    teambox.grid()
    teambox.title('Team Options')
    teambut1=tk.Button(teambox,text='Team 1',command=Teamcho1)
    teambut1.grid(column=0,row=0)
    teambox.mainloop()
    
def Teamcho1():
    global Cteam
    Cteam=team1
    root.team1Variable.set("Batting: "+str(Cbatter['name']))

def Batopt():
    Batbox=tk.Tk()
    Batbox.grid()
    Batbox.title('Batter Options')
    
    Batbut1=tk.Button(Batbox,text='Deffensive',command=BatDef)
    Batbut1.grid(column=0,row=0)
    Batbut2=tk.Button(Batbox,text='Modderate',command=BatMod)
    Batbut2.grid(column=0,row=1)
    Batbut3=tk.Button(Batbox,text='Agressive',command=BatAgg)
    Batbut3.grid(column=0,row=2)
    Batbox.geometry('{}x{}'.format(200, 200))
    Batbox.mainloop()
    
def Bowlopt():
    Bowlbox=tk.Tk()
    Bowlbox.title('Bowler Options')
    Bowlbox.mainloop()
    
def BatDef():
    global Current, Deffensive
    Current=Deffensive
    root.BatDemlabelVariable.set("Batter Demenor: Deffensive")

def BatMod():
    global Current, Modderate
    Current=Modderate
    root.BatDemlabelVariable.set("Batter Demenor: Modderate")

def BatAgg():
    global Current, Agressive
    Current=Agressive
    root.BatDemlabelVariable.set("Batter Demenor: Agressive")

    
def Bowl():
        global runs, overs, wickets, Cbatter, ACbatter, hit, out,mod1
              
        shot = random.randint(Cbatter['SR']/2,100)
        out = random.randint(0,np.floor(100-Cbatter['Ave']/5))
        if shot in range(Current[0],Current[1]):
            hit = 0
            root.StatuslabelVariable.set("Commentator: Safely Defended")
            
            if out >=95:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(0)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0
            
        if shot in range(Current[1],Current[2]):
            hit=1
            root.StatuslabelVariable.set("Commentator: A quick single")
            
            if out >=93:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(1)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0

                
        if shot in range(Current[2],Current[3]):
            hit=2
            root.StatuslabelVariable.set("Commentator: Thats two")
    
            if out >=90:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(2)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0

        if shot in range(Current[3],Current[4]):
            hit=3
            root.StatuslabelVariable.set("Commentator: They've taken three")
            
            if out >=87:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(3)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0

        if shot in range(Current[4],Current[5]):
            hit=4
            root.StatuslabelVariable.set("Commentator: That's four runs")
            
            if out >=80:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(4)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0

        if shot >= Current[5]:
            hit =6
            root.StatuslabelVariable.set("Commentator: A cracking six!!")
            
            if out >=75:
                wickets=wickets-1
                root.StatuslabelVariable.set("Commentator: That's betten the Bat!!(6)")
                Cbatter=Cteam[10-wickets]
                root.team1Variable.set("Batting: "+str(Cbatter['name']))
                hit=0
        
            
        runs=runs+hit
        overs=overs+0.1
        Cbatter['Score']=Cbatter['Score']+hit
        print('shot '+str(shot))
        print('hit ' +str(hit))
        print('out ' +str(out))
        print('CBatScore_'+str(Cbatter['Score']))
        
        root.RunslabelVariable.set("Total Runs: "+str(runs))
        root.OverslabelVariable.set("Total Overs: "+str(np.round(overs,1)))
        root.WicketslabelVariable.set("Wickets Remaining: "+str(wickets))
        
        
        
root = tk.Tk()

root.grid()

root.RunslabelVariable = tk.StringVar()
Runslabel = tk.Label(root,textvariable=root.RunslabelVariable,anchor="w",fg="black",bg="grey")
Runslabel.grid(column=2,row=2,columnspan=2,sticky='EW')
root.RunslabelVariable.set("Total Runs:")

root.OverslabelVariable = tk.StringVar()
Overslabel = tk.Label(root,textvariable=root.OverslabelVariable, anchor="w",fg="black",bg="grey")
Overslabel.grid(column=2,row=1,columnspan=2,sticky='EW')
root.OverslabelVariable.set("Total Overs:")

root.WicketslabelVariable = tk.StringVar()
Wicketslabel = tk.Label(root,textvariable=root.WicketslabelVariable, anchor="w",fg="black",bg="grey")
Wicketslabel.grid(column=2,row=3,columnspan=2,sticky='EW')
root.WicketslabelVariable.set("Wickets Remaining: " +str(wickets))

root.StatuslabelVariable = tk.StringVar()
Statuslabel = tk.Label(root,textvariable=root.StatuslabelVariable, anchor="w",fg="black",bg="grey")
Statuslabel.grid(column=2,row=4,columnspan=2,sticky='EW')
root.StatuslabelVariable.set("Commentator: ")

root.BatDemlabelVariable = tk.StringVar()
BatDemlabel = tk.Label(root,textvariable=root.BatDemlabelVariable, anchor="w",fg="black",bg="grey")
BatDemlabel.grid(column=2,row=5,columnspan=2,sticky='EW')
root.BatDemlabelVariable.set("Batter Demenor: Deffensive")

root.team1Variable = tk.StringVar()
team1label = tk.Label(root,textvariable=root.team1Variable, anchor="w",fg="black",bg="grey")
team1label.grid(column=2,row=6,columnspan=2,sticky='EW')
root.team1Variable.set("Batting: ")

but1 = tk.Button(root,text='Bowl',command=Bowl)
but1.grid(column=0,row=0)



Optmenu=tk.Menu(root)
root.config(menu=Optmenu)

submenu=tk.Menu(Optmenu)
Optmenu.add_cascade(label='Options', menu=submenu)
submenu.add_command(label='Batter',command=Batopt)
submenu.add_command(label='Bowler',command=Bowlopt)
submenu.add_command(label='Choose Teams',command=teambox)

#Teammenu=tk.Menu(root)
#root.config(menu=Teammenu)
#subTeammenu=tk.Menu(Teammenu)
#Teammenu.add_cascade(label='Choose Teams', menu=subTeammenu)



#menu=Menu(root)
#root.config(menu=menu)




root.geometry('{}x{}'.format(600, 600))
root.title('Clicket')
root.mainloop()

