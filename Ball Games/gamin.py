# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:39:43 2022

@author: wimarti
"""

import sys
import pygame
import random
from pongFunctions import *

r = 40
tickValue = 100

ballInput = input('Enter number of balls:  ')
try:
    numBalls = int(ballInput)
except:
    sys.exit(['Must enter number'])


winBase = 800
winHeight = 3 * winBase // 4

pygame.init()
win = pygame.display.set_mode((winBase, winHeight))
pygame.display.set_caption('Gamin')

clock = pygame.time.Clock()

game = True
x = [None] * (numBalls)
y = [None] * (numBalls)
xvel = [None] * (numBalls)
yvel = [None] * (numBalls)
ballColor = [None] * (numBalls)

for i in range(0,numBalls):
    x[i] = random.randint(0, winBase - r)
    y[i] = random.randint(0, winHeight - r)
    if i % 2 == 0:
        xvel[i] = 2
        yvel[i] = 1
    else:
        xvel[i] = -2
        yvel[i] = -1
    ballColor[i] = (random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255))

while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    win.fill((20, 20, 20)) # clear board
    
    # Draw circle and set postion for next circle
    
    for i in range(0,len(x)):
        pygame.draw.circle(win, ballColor[i], (x[i],y[i]), r)
        x[i] += xvel[i]
        y[i] += yvel[i]
        [x[i], y[i], xvel[i], yvel[i]] = circlecoord(x[i], y[i], xvel[i],
                                                     yvel[i], r, winBase,
                                                     winHeight)

    clock.tick(tickValue)
    pygame.display.update()
    
pygame.quit()
