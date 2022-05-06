# Functions for Tic Tac Toe Game

import mycolors
import random
import pygame

def checkwinner(boardspots):
    winnerCheck = False
    # Check three across
    if boardspots[0] == boardspots[1] == boardspots[2]:
        winnerCheck = boardspots[0]
    elif boardspots[3] == boardspots[4] == boardspots[5]:
        winnerCheck = boardspots[3]
    elif boardspots[6] == boardspots[7] == boardspots[8]:
        winnerCheck = boardspots[6]
    # Check three vertically
    elif boardspots[0] == boardspots[3] == boardspots[6]:
        winnerCheck = boardspots[0]
    elif boardspots[1] == boardspots[4] == boardspots[7]:
        winnerCheck = boardspots[1]
    elif boardspots[2] == boardspots[5] == boardspots[8]:
        winnerCheck = boardspots[2]
    # Check diagonals
    elif boardspots[0] == boardspots[4] == boardspots[8]:
        winnerCheck = boardspots[0]
    elif boardspots[2] == boardspots[4] == boardspots[6]:
        winnerCheck = boardspots[2]

    return winnerCheck

def updatetext(win, gamefont, text, textboxheight):
    # Updates text in tbox
    displaytext = gamefont.render(text, True, mycolors.black)
    textrect = displaytext.get_rect()
    textrect.center = (win.get_width() / 2, win.get_height() - textboxheight / 2)
    win.blit(displaytext, textrect)

def getAIchoice(boardSpots, aiplayer):
    userplayer = aiplayer * -1
    userspots = []
    aispots = []
    openspots = []
    aimove = None
    for i in range(len(boardSpots)):
        if boardSpots[i] == userplayer:
            userspots.append(i)
        elif boardSpots[i] == aiplayer:
            aispots.append(i)
        elif boardSpots[i] == 0:
            openspots.append(i)

    # Check if each of the open spots would cause a win, if so then take that spot
    for i in openspots:
        checkAIwin = boardSpots.copy()
        checkAIwin[i] = aiplayer
        if checkwinner(checkAIwin) == aiplayer:
            aimove = i
            break

    for i in openspots:
        print(i)
        checkUserWin = boardSpots.copy()
        checkUserWin[i] = userplayer
        if checkwinner(checkUserWin) == userplayer:
            print('BLOCKED')
            aimove = i
            break

    if aimove is None:  # if end of the loop does not show any of the winning spots
        if len(openspots) == 9:  # starts in the corner if AI going first
            aimove = 0
        elif 4 in openspots:  # starts in the middle if player went first
            aimove = 4
        elif any(elem in [0, 2, 6, 8] for elem in openspots):  # choose corners if available
            opencorners = []
            for j in [0, 2, 6, 8]:
                if j in openspots:
                    opencorners.append(j)
            randchoice = random.randint(0, len(opencorners) - 1)
            aimove = opencorners[randchoice]
        else:   # choose random spot if nothing else
            randchoice = random.randint(0, len(openspots) - 1)
            aimove = openspots[randchoice]

    return aimove
