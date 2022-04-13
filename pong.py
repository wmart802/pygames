# Full Pong Game

import pygame
import mycolors
import random
from pongGameFunctions import *


def playpong(numplayers):

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
    p1color = (0, 0, 255)
    p2color = (255, 0, 0)

    # Setting Parameters for Ball and Players
    playerWidthHeight = [winBase // 25, winHeight // 5]
    ballLoc = [winBase // 2, winHeight // 2]
    ballV = [2, 1]
    ballR = winBase // 30
    p1loc = winHeight // 2
    p2loc = winHeight // 2
    lastHit = 0
    playerScores = [0, 0]
    scoreFont = pygame.font.Font('Arial Black.ttf', winBase // 10)

    win.fill(gameBackgroundColor)

    # Playing the Game
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and p1loc - playerWidthHeight[1]/2 > 0:
            p1loc -= 2
        elif key[pygame.K_DOWN] and p1loc + playerWidthHeight[1]/2 < winHeight:
            p1loc += 2
        if key[pygame.K_w] and p2loc - playerWidthHeight[1]/2 > 0:
            p2loc -= 2
        elif key[pygame.K_s] and p2loc + playerWidthHeight[1]/2 < winHeight:
            p2loc += 2

        # Clear Board
        win.fill(gameBackgroundColor)

        # Draw Players and Circle
        p2 = pygame.draw.rect(win, p2color, (0, p2loc - (playerWidthHeight[1]//2),
                                             playerWidthHeight[0], playerWidthHeight[1]))
        p1 = pygame.draw.rect(win, p1color, (winBase - playerWidthHeight[0], p1loc - (playerWidthHeight[1]//2),
                                             playerWidthHeight[0], playerWidthHeight[1]))
        gameBall = pygame.draw.circle(win, ballColor, (ballLoc[0], ballLoc[1]), ballR)

        # Calculate New Ball Location
        for i in range(len(ballLoc)):
            ballLoc[i] += ballV[i]

        # Check Score
        score = checkscore(win, ballLoc, ballR, ballV[0])
        if score:
            scoreTime = pygame.time.get_ticks()
            ballLoc = [winBase // 2, winHeight // 2]
            ballV = [2*-1*score, 1]
            p1loc = winHeight // 2
            p2loc = winHeight // 2
            if score == 1:
                playerScores[0] += 1
            else:
                playerScores[1] += 1
            displayScore = True
            while displayScore:
                elapsed = pygame.time.get_ticks() - scoreTime
                scoreString = str(playerScores[1]) + ' - ' + str(playerScores[0])
                scoreText = scoreFont.render(scoreString, True, mycolors.white)
                win.blit(scoreText, (winBase/2 - scoreText.get_width()/2, winHeight/2 - scoreText.get_height()))
                pygame.display.update()
                if elapsed > 4000:
                    pygame.draw.rect(win, mycolors.black, (winBase/2 - scoreText.get_width()/2,
                                                           winHeight/2 - scoreText.get_height(),
                                                           scoreText.get_width(), scoreText.get_height()))
                    pygame.display.update()
                    displayScore = False

        # Check Ball Location for Wall Bounces
        [ballLoc[1], ballV[1]] = checkWallBounce(win, ballLoc[1], ballV[1], ballR)

        # Check Ball for Player Bounces
        if ballLoc[0] < (winBase // 3) and lastHit != 2:  # Checking Player 2 bounces on left third of screen
            [ballV, lastHit] = checkPlayerBounce(p2, playerWidthHeight, gameBall, ballV, ballR, -1)
        elif ballLoc[0] > (winBase * 2 // 3) and lastHit != 1:  # Checking Player 1 bounces on right third of screen
            [ballV, lastHit] = checkPlayerBounce(p1, playerWidthHeight, gameBall, ballV, ballR, 1)

        pyClock.tick(tickValue)
        pygame.display.update()

    pygame.quit()
