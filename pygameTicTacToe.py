# TIC TAC TOE

import pygame
import mycolors
from ticTacToeFunctions import *

def playtictactoe(numPlayers):

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
    xmids = [x[1] - dx // 2, x[2] - dx // 2, x[3] - dx // 2]
    ymids= [y[1] - dx // 2, y[2] - dx // 2, y[3] - dx // 2]
    tboxHeight = winHeight - (boardLength + 2*boardBorder)

    # Geometries for Drawing
    lwidth = winBase // 140

    # Initializing
    pygame.init()
    win = pygame.display.set_mode((winBase, winHeight))
    pygame.display.set_caption('Playing Pygame')

    # Game Variables
    spots = [0]*9
    p1 = 1
    p2 = -1
    player = 1
    gamefont = pygame.font.Font('Arial.ttf', dx // 4)
    againfont = pygame.font.Font('Arial.ttf', dx // 5)
    text = 'Playing Tic Tac Toe!'
    gameEnd = False
    elapsed = 0

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
        tbox = pygame.draw.rect(win, mycolors.offwhite, (0, y[3] + boardBorder, winBase, tboxHeight))
        tboxOutline = pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight), lwidth)
        displaytext = gamefont.render(text, True, mycolors.black)
        textrect = displaytext.get_rect()
        textrect.center = (winBase // 2, winHeight - tboxHeight // 2)
        win.blit(displaytext, textrect)

        # Drawing Selection
        if goodSelection and spots[spotsIndex] == 0:
            spots[spotsIndex] = player
            if player == 1:
                pygame.draw.line(win, c1, (xmids[i-1] + dx // 4, ymids[j-1] + dx // 4),
                                 (xmids[i-1] - dx // 4, ymids[j-1] - dx // 4), 2*lwidth)
                pygame.draw.line(win, c1, (xmids[i - 1] + dx // 4, ymids[j - 1] - dx // 4),
                                 (xmids[i - 1] - dx // 4, ymids[j - 1] + dx // 4), 2 * lwidth)
            elif player == -1:
                pygame.draw.circle(win, c2, (xmids[i-1], ymids[j-1]), dx // 3, 2*lwidth)
            player *= -1

        pygame.display.update()

        # Checking for winner
        winner = checkwinner(spots)
        if winner or 0 not in spots:
            gameEnd = True
            startTime = pygame.time.get_ticks()

        while gameEnd:
            if winner == 1:
                text = 'Player 1 Wins!'
                tbox = pygame.draw.rect(win, mycolors.offwhite, (0, y[3] + boardBorder, winBase, tboxHeight))
                tboxOutline = pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight), lwidth)
                updatetext(win, gamefont, text,  tboxHeight)
                elapsed = pygame.time.get_ticks() - startTime
                pygame.display.update()
            elif winner == -1:
                text = 'Player 2 Wins!'
                tbox = pygame.draw.rect(win, mycolors.offwhite, (0, y[3] + boardBorder, winBase, tboxHeight))
                tboxOutline = pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight), lwidth)
                updatetext(win, gamefont, text, tboxHeight)
                elapsed = pygame.time.get_ticks() - startTime
                pygame.display.update()
            elif 0 not in spots:
                startTime = pygame.time.get_ticks()
                text = 'It\'s a Tie!'
                tbox = pygame.draw.rect(win, mycolors.offwhite, (0, y[3] + boardBorder, winBase, tboxHeight))
                tboxOutline = pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight), lwidth)
                updatetext(win, gamefont, text, tboxHeight)
                elapsed = pygame.time.get_ticks() - startTime
                pygame.display.update()

            if (winner or 0 not in spots) and elapsed == 2000:
                # Put up play again rectangle in center
                # draw rectangles for yes and no
                again = 0
                while again == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            again = 1
                            playing = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if yesRect.collidepoint(event.pos[0], event.pos[1]):
                                    pygame.quit()
                                    playtictactoe(2)
                                elif menuRect.collidepoint(event.pos[0], event.pos[1]):
                                    again = 1
                                    gameEnd = False
                                    playing = False

                        tbox = pygame.draw.rect(win, mycolors.offwhite, (0, y[3] + boardBorder, winBase, tboxHeight))
                        tboxOutline = pygame.draw.rect(win, mycolors.black, (0, y[3] + boardBorder, winBase, tboxHeight),
                                                       lwidth)
                        againText = againfont.render('Play Again?', True, mycolors.black)
                        yesText = againfont.render('Yes', True, mycolors.black)
                        menuText = againfont.render('Main Menu', True, mycolors.black)
                        yesRect = pygame.Rect(win.get_width() * 0.4, win.get_height() - tboxHeight*0.9,
                                              win.get_width() * 0.2, tboxHeight*0.8)
                        menuRect = pygame.Rect(win.get_width() * 0.65, win.get_height() - tboxHeight*0.9,
                                               win.get_width() * 0.3, tboxHeight*0.8)
                        pygame.draw.rect(win, mycolors.aqua, yesRect)
                        pygame.draw.rect(win, mycolors.aqua, menuRect)
                        win.blit(againText, (winBase*0.05, winHeight - tboxHeight*0.8))
                        win.blit(yesText, (winBase*0.4 + win.get_width()*0.1 - yesText.get_width()/2,
                                           winHeight - tboxHeight*0.8))
                        win.blit(menuText, (winBase*0.65 + win.get_width()*0.15 - menuText.get_width()/2,
                                            winHeight - tboxHeight*0.8))
                        pygame.display.update()

    pygame.quit()
