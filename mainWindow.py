# Main Window For Pygames Project

import pygame
import mycolors

winBase = 500
winHeight = winBase * (4 // 3)

# Setting Colors for Window
mainWinColor = mycolors.offwhite
selectColors = [(158, 219, 255), mycolors.white]

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

# Drawing Buttons

pygame.display.update()

mainWinOpen = True
while mainWinOpen:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainWinOpen = False

pygame.quit()
