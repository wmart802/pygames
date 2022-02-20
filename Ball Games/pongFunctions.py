# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:38:10 2022

@author: wimarti
"""

def circlecoord(x, y, xvel, yvel, r, width, height):
    
    if x + r >= width: # if circle hits right border change x vel
        x = width - r
        xvel *= -1

    elif x - r <= 0: # if circle hits left border change x vel
        x = r
        xvel *= -1
        
    if y + r >= height: # if hits top border change y vel
        y = height - r
        yvel *= -1

    elif y - r <= 0: # if hits bottom border change y vel
        y = r
        yvel *= -1

    return(x,y,xvel,yvel)
        