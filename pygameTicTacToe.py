# TIC TAC TOE

import pygame
import mycolors
import time
import math

# Calculating Geometry
rootBase = 800
rootHeight = 2*rootBase // 3
boardLength = 4*rootHeight // 5

# Board Places
centerX = (rootBase+boardLength) // 2
centerY = boardLength // 2
dx = boardLength // 3
x0 = (rootBase-boardLength) // 2
x = [x0, x0 + dx, x0 + 2*dx, x0 + 3*dx]
y = [0, dx, 2*dx, 3*dx]
tboxHeight = rootHeight - boardLength

# Geometries for Drawing
lwidth = rootBase // 140

# Initializing
pygame.init()
root = pygame.display.set_mode((rootBase, rootHeight))
pygame.display.set_caption('Playing Pygame')

root.fill(mycolors.offwhite)
c1 = (255, 0, 0)
c2 = (0, 0, 255)
cb = (162, 97, 186)

# Drawing the Board
pygame.draw.line(root, cb, (x[1], y[0]), (x[1], y[3]), lwidth)
pygame.draw.line(root, cb, (x[2], y[0]), (x[2], y[3]), lwidth)
pygame.draw.line(root, cb, (x[0], y[1]), (x[3], y[1]), lwidth)
pygame.draw.line(root, cb, (x[0], y[2]), (x[3], y[2]), lwidth)

pygame.draw.rect(root, mycolors.offwhite, (0, y[3], rootBase, tboxHeight))
pygame.draw.rect(root, mycolors.black, (0, y[3], rootBase, tboxHeight), lwidth)

pygame.display.update()

input()
pygame.display.quit()
