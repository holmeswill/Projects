# -*- coding: utf-8 -*-
import random

balls=0
overs=10
runs=0
i=0
wickets=10


for i in range(0,6):
   hit = random.randint(0,6)
   runs = runs+hit 
   print ("you got a " +str(hit)+" you now have " + str(runs)+ "runs")
   
   out=random.randint(0,100)
   if out >= 50:
       wickets=wickets-1
       print ("you're out you now have "+str(wickets)+ " wickets left")
       
   

   
   

    
