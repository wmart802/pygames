# Functions for use in full pong game
import pygame

def startRound(gameWindow, ballStartLocation, ballStartVelocity):
    # This function starts a new round after score is made
    # Show score update
    # give couple second break
    # reset ball position
    pygame.display.update()

def checkWallBounce(gameWindow, ballLocationY, ballVelocityY, ballRadius):
    # Check if ball hits top and bottom of game window
    winHeight = gameWindow.get_height()

    if (ballLocationY - ballRadius <= 0) or (ballLocationY + ballRadius >= winHeight):
        ballVelocityY *= -1

    return [ballLocationY, ballVelocityY]

def checkPlayerBounce(playerObject, playerWidthHeight, ballLocation, ballVelocity, ballRadius, leftright):
    # Check if ball hits an inputted player block
    if leftright == -1:
        playerObjectX = playerObject.left
    elif leftright == 1:
        playerObjectX = playerObject.left

    ballCheckPoint = ballLocation[0] + (ballRadius * leftright)

    madeHit = 0
    velChange = 1
    if playerObject.top <= ballLocation[1] <= playerObject.bottom:
        if playerObjectX >= ballCheckPoint and leftright == -1:
            velChange = -1.05
            madeHit = 2
        elif playerObjectX - playerWidthHeight[0]*0.8 <= ballCheckPoint and leftright == 1:
            velChange = -1.05
            madeHit = 1

    ballVelocity[0] *= velChange

    return [ballVelocity, madeHit]

def checkscore(window, ballLocation, ballRadius, ballXVelocity):
    # Check for a score
    if ballXVelocity < 0 and ballLocation[0] + ballRadius < 0:
        score = 1
    elif ballXVelocity > 0 and ballLocation[0] - ballRadius > window.get_width():
        score = -1
    else:
        score = 0

    return score