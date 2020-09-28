#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:35:39 2020

@author: egeakertek
"""

import random
from tkinter import *

master = Tk()

canvas1 = Canvas(master,width = 600, height = 600)
canvas1.pack()

def draw():
    
    
    x1 = random.randint(1,600)
    y1 = random.randint(1,600)
    width = random.randint(20,100)
    height = random.randint(20,100)
    
    x2 = x1 + width
    y2 = y1 + height
    
    colors = ["red","green","blue","yellow"]
   
    color = random.choice(colors)
    canvas1.create_rectangle(x1,y1,x2,y2,fill = color)
def dispatch():
    
    canvas1.delete("all")
    for i in range(100):
        draw()
    master.after(200,dispatch) # 0.2 seconds
    
dispatch()
mainloop()