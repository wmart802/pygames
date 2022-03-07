# Full Pong Game

import pygame
import random
from pongGameFunctions import *

# Initializing Window
winBase = 800
winHeight = (3 * 800) // 4
pygame.init()
win = pygame.display.set_mode((winBase, winHeight))
pygame.display.set_caption('Pong')

# Initializing Clock Parameters
tickValue = 100
pyClock = pygame.time.Clock()

# Setting Colors
gameBackgroundColor = (0, 0, 0)
ballColor = (255, 255, 255)
p1color = (255, 0, 0)
p2color = (0, 0, 255)

# Setting Parameters for Ball and Players
playerWidthHeight = [winBase // 25, winHeight // 5]
ballLoc = [winBase // 2, winHeight // 2]
ballV = [2, 1]
ballR = winBase // 30
p1loc = winHeight // 2
p2loc = winHeight // 2

win.fill(gameBackgroundColor)

# Playing the Game
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        p1loc -= 2
    elif key[pygame.K_DOWN]:
        p1loc += 2
    if key[pygame.K_w]:
        p2loc -= 2
    elif key[pygame.K_s]:
        p2loc += 2

    # Clear Board
    win.fill(gameBackgroundColor)

    # Draw Players and Circle
    p1 = pygame.draw.rect(win, p1color, (0, p1loc - (playerWidthHeight[1]//2),
                                         playerWidthHeight[0], playerWidthHeight[1]))
    p2 = pygame.draw.rect(win, p2color, (winBase - playerWidthHeight[0], p2loc - (playerWidthHeight[1]//2),
                                         playerWidthHeight[0], playerWidthHeight[1]))
    gameBall = pygame.draw.circle(win, ballColor, (ballLoc[0], ballLoc[1]), ballR)

    # Calculate New Ball Location
    for i in range(len(ballLoc)):
        ballLoc[i] += ballV[i]

    # Check Ball Location for Bounces
    [ballLoc[1], ballV[1]] = checkWallBounce(win, ballLoc[1], ballV[1], ballR)


    pyClock.tick(tickValue)
    pygame.display.update()

pygame.quit()
