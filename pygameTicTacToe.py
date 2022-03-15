# TIC TAC TOE

import pygame
import mycolors
from ticTacToeFunctions import *
import time

# Calculating Geometry
winHeight = 600
boardLength = 4 * winHeight // 5
winBase = boardLength * 6 // 5

# Board Places
centerX = (winBase + boardLength) // 2
centerY = boardLength // 2
dx = boardLength // 3
boardBorder = boardLength // 20
x0 = (winBase - boardLength) // 2
x = [x0, x0 + dx, x0 + 2*dx, x0 + 3*dx]
y = [boardBorder, boardBorder+dx, boardBorder+2*dx, boardBorder+3*dx]
tboxHeight = winHeight - (boardLength + 2*boardBorder)

# Geometries for Drawing
lwidth = winBase // 140

# Game Variables
spots = [0]*9
p1 = 1
p2 = -1
player = -1

# Initializing
pygame.init()
win = pygame.display.set_mode((winBase, winHeight))
pygame.display.set_caption('Playing Pygame')

# Color setting
win.fill(mycolors.offwhite)
c1 = (255, 0, 0)
c2 = (0, 0, 255)
cb = (162, 97, 186)

# Playing Game
playing = True
while playing:

    goodSelection = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                # Determining mouse selection
                for j in range(1, 4):
                    if y[j-1] < mouseY < y[j]:
                        for i in range(1, 4):
                            if x[i-1] < mouseX < x[i]:
                                spotsIndex = 3*(j-1) + (i-1)
                                goodSelection = True
                                break
                    if goodSelection:
                        break

    # Drawing the Board
    pygame.draw.line(win, cb, (x[1], y[0]), (x[1], y[3]), lwidth)
    pygame.draw.line(win, cb, (x[2], y[0]), (x[2], y[3]), lwidth)
    pygame.draw.line(win, cb, (x[0], y[1]), (x[3], y[1]), lwidth)
    pygame.draw.line(win, cb, (x[0], y[2]), (x[3], y[2]), lwidth)

    # Draw Test Boxes
    pygame.draw.rect(win, mycolors.offwhite, (0, y[3], winBase, tboxHeight))
    pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight), lwidth)

    # Drawing Selection
    if goodSelection:
        player *= -1
        spots[spotsIndex] = player
        if player == 1:
            pygame.draw.circle(win, c1, (x[i] - (dx // 2), y[j] - (dx // 2)), dx*2 // 5)
        elif player == -1:
            pygame.draw.circle(win, c2, (x[i] - (dx // 2), y[j] - (dx // 2)), dx * 2 // 5)

    pygame.display.update()

    # Checking for winner
    winner = checkwinner(spots)
    if winner:
        time.sleep(1)
        if winner == 1:
            win.fill(c1)
            pygame.display.update()
        elif winner == -1:
            win.fill(c2)
            pygame.display.update()
        time.sleep(4)
        playing = False

pygame.quit()
