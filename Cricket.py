# -*- coding: utf-8 -*-
import random

balls=0
overs=10
runs=0
i=0


for i in range(0,6):
   hit = random.randint(0,6)
   runs = runs+hit 
   print ("you got a " +str(hit)+" you now have " + str(runs))
   
   
   

    
