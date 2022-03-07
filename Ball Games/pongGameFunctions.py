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
