# Main Window For Pygames Project

import pygame
import mycolors
from pong import playpong
from pygameTicTacToe import playtictactoe

def openmainmenu():
    winBase = 500
    winHeight = winBase * (4 // 3)

    # Setting Colors for Window
    mainWinColor = mycolors.offwhite
    selectColors = [(100, 219, 250), mycolors.white]

    # Creating Initial Window
    pygame.init()
    mainWin = pygame.display.set_mode((winBase, winHeight))
    mainWin.fill(mainWinColor)

    # Drawing Title Text
    titleFont = pygame.font.Font('Arial Black.ttf', winBase // 20)
    titleText = titleFont.render('PyGame Arcade', True, mycolors.black)
    mainWin.blit(titleText, ((winBase // 2) - titleText.get_width()/2, winHeight // 30))
    # Subtitle Text
    subtitleFont = pygame.font.Font('Arial.ttf', winBase // 30)
    subtitleText1 = subtitleFont.render('Choose the settings you would like to play with,', True, mycolors.black)
    subtitleText2 = subtitleFont.render('and then click on the game that you want to play', True, mycolors.black)
    mainWin.blit(subtitleText1, ((winBase // 2) - subtitleText1.get_width()/2, winHeight // 8))
    mainWin.blit(subtitleText2, ((winBase // 2) - subtitleText2.get_width()/2, winHeight // 8 + subtitleText1.get_height()))

    # Initializing Button Positions, Rectangles, and Colors
    multiPlayXY = [winBase*0.1, winHeight*0.3, winBase*0.3, winHeight*0.1]
    singlePlayXY = [winBase*0.6, winHeight*0.3, winBase*0.3, winHeight*0.1]
    pongXY = [winBase*0.05, winHeight*0.7, winBase*0.4, winHeight*0.1]
    tictacXY = [winBase*0.55, winHeight*0.7, winBase*0.4, winHeight*0.1]

    multiPlayRect = pygame.Rect(multiPlayXY[0], multiPlayXY[1], multiPlayXY[2], multiPlayXY[3])
    singlePlayRect = pygame.Rect(singlePlayXY[0], singlePlayXY[1], singlePlayXY[2], singlePlayXY[3])
    pongRect = pygame.Rect(pongXY[0], pongXY[1], pongXY[2], pongXY[3])
    tictacRect = pygame.Rect(tictacXY[0], tictacXY[1], tictacXY[2], tictacXY[3])

    multiPlayC = selectColors[0]
    singlePlayC = selectColors[1]
    pongC = mycolors.black
    tictacC = mycolors.pink

    # Initializing Button Labels
    buttonFont = pygame.font.Font('Arial.ttf', winBase // 25)
    multiPlayText = buttonFont.render('Multiplayer', True, mycolors.black)
    singlePlayText = buttonFont.render('Singleplayer', True, mycolors.black)
    pongText = buttonFont.render('Pong', True, mycolors.white)
    tictacText = buttonFont.render('Tic Tac Toe', True, mycolors.black)

    mainWinOpen = True
    game = False
    while mainWinOpen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainWinOpen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Checking for Button Selects
                    if multiPlayRect.collidepoint(event.pos[0], event.pos[1]):
                        multiPlayC = selectColors[0]
                        singlePlayC = selectColors[1]
                    elif singlePlayRect.collidepoint(event.pos[0], event.pos[1]):
                        multiPlayC = selectColors[1]
                        singlePlayC = selectColors[0]
                    elif pongRect.collidepoint(event.pos[0], event.pos[1]):
                        game = 1
                        mainWinOpen = False
                    elif tictacRect.collidepoint(event.pos[0], event.pos[1]):
                        game = 2
                        mainWinOpen = False

        # Drawing Buttons
        pygame.draw.rect(mainWin, multiPlayC, multiPlayRect)
        pygame.draw.rect(mainWin, singlePlayC, singlePlayRect)
        pygame.draw.rect(mainWin, pongC, pongRect)
        pygame.draw.rect(mainWin, tictacC, tictacRect)
        # Adding Labels
        mainWin.blit(multiPlayText, (multiPlayXY[0] + multiPlayXY[2]/2 - multiPlayText.get_width()/2,
                                     multiPlayXY[1] + multiPlayXY[3]/2 - multiPlayText.get_height()/2))
        mainWin.blit(singlePlayText, (singlePlayXY[0] + singlePlayXY[2] / 2 - singlePlayText.get_width() / 2,
                                      singlePlayXY[1] + singlePlayXY[3] / 2 - singlePlayText.get_height() / 2))
        mainWin.blit(pongText, (pongXY[0] + pongXY[2] / 2 - pongText.get_width() / 2,
                                pongXY[1] + pongXY[3] / 2 - pongText.get_height() / 2))
        mainWin.blit(tictacText, (tictacXY[0] + tictacXY[2] / 2 - tictacText.get_width() / 2,
                                  tictacXY[1] + tictacXY[3] / 2 - tictacText.get_height() / 2))

        pygame.display.update()

    pygame.quit()

    if game == 1 and multiPlayC == selectColors[0]:
        playpong(2)
    elif game == 2 and multiPlayC == selectColors[0]:
        playtictactoe(2)
    elif game == 2 and singlePlayC == selectColors[0]:
        playtictactoe(1)

openmainmenu()