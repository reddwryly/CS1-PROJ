import pygame #requires pip install *
'''
copy paste in terminal to install: python3 -m pip install -U pygame --user
copy paste in terminal to check if working: python3 -m pygame.examples.aliens
if problems occur visit: https://www.pygame.org/wiki/GettingStarted
'''
import random

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Outfit Picker")

#buttons
topleftArrowButton = pygame.Rect(250,100,100,100)
topRightArrowButton = pygame.Rect(780,100,100,100)
bottomleftArrowButton = pygame.Rect(250,400,100,100)
bottomRightArrowButton = pygame.Rect(780,400,100,100)
lock1Button = pygame.Rect(890,100,100,100)
lock2Button = pygame.Rect(890,400,100,100)
shufleButton = pygame.Rect(890,250,100,100)

#assets number *need updated as assets are added
lstTop = [0, 1, 2, 3, 4, 5]
lstBot = [0, 1, 2, 3, 4, 5]

topIndex = 0 
botIndex = 0

topLock = 0
bottomLock = 0

shuffleLock1 = False
shuffleLock2 = False

#top images 
top0 = pygame.image.load('asset/top/0.png')
top1 = pygame.image.load('asset/top/1.png')
top2 = pygame.image.load('asset/top/2.png')

#bottom images
bottom0 = pygame.image.load('asset/bottom/0.png')
bottom1 = pygame.image.load('asset/bottom/1.png')
bottom2 = pygame.image.load('asset/bottom/2.png')

#button images 
topleftArrow = pygame.image.load('asset/buttons/left.PNG')
topRightArrow = pygame.image.load('asset/buttons/right.png')
bottomleftArrow = pygame.image.load('asset/buttons/left.PNG')
bottomRightArrow = pygame.image.load('asset/buttons/right.png')
shuffle = pygame.image.load('asset/buttons/shuffle.png')

run = True
while run:

    screen.fill("white")

    #load locks
    lockNum1 = str(topLock)
    lockNum2 = str(bottomLock)
    lock1 = pygame.image.load("asset/buttons/" + lockNum1 + ".png")
    lock2 = pygame.image.load("asset/buttons/" + lockNum2 + ".png")

    #draw buttons 
    screen.blit(topleftArrow, (250, 100))
    screen.blit(bottomleftArrow, (250, 400))
    screen.blit(topRightArrow, (780, 100))
    screen.blit(bottomRightArrow, (780, 400))
    screen.blit(lock1, (890, 100))
    screen.blit(lock2, (890, 400))
    screen.blit(shuffle, (890, 250))

    #load images 
    pathNum = str(topIndex)
    top = pygame.image.load("asset/top/" + pathNum + ".png")
    top2 = pygame.transform.scale_by(top, 3)

    pathNum2 = str(botIndex)
    bot = pygame.image.load("asset/bottom/" + pathNum2 + ".png")
    bot2 = pygame.transform.scale_by(bot, 3)


    #draw images
    screen.blit(top2, (420, 30))
    screen.blit(bot2, (420, 310))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if topRightArrowButton.collidepoint(event.pos):
                if topIndex >= lstTop[0] and topIndex < len(lstTop) - 1:
                    topIndex = topIndex + 1
                elif topIndex == len(lstTop) - 1:
                    topIndex = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if topleftArrowButton.collidepoint(event.pos):
                if topIndex <= len(lstTop) and topIndex != lstTop[0]:
                    topIndex = topIndex - 1
                elif topIndex == lstTop[0]:
                    topIndex = lstTop[len(lstTop) - 1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bottomRightArrowButton.collidepoint(event.pos):
                if botIndex >= lstBot[0] and botIndex < len(lstBot) - 1:
                    botIndex = botIndex + 1
                elif botIndex == len(lstBot) - 1:
                    botIndex = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bottomleftArrowButton.collidepoint(event.pos):
                if botIndex <= len(lstBot) and botIndex != lstBot[0]:
                    botIndex = botIndex - 1
                elif botIndex == lstBot[0]:
                    botIndex = lstBot[len(lstBot) - 1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shufleButton.collidepoint(event.pos):
                for i in range(len(lstTop)):
                    if shuffleLock1 == True:
                        break
                    if i == random.randint(lstTop[0], len(lstTop)):
                        topIndex = i
                        continue
                for i in range(len(lstBot)):
                    if shuffleLock2 == True:
                        break
                    if i == random.randint(lstBot[0], len(lstBot)):
                        botIndex = i
                        continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lock1Button.collidepoint(event.pos):
                if topLock == 0:
                    topLock = 1
                    shuffleLock1 = True
                elif topLock == 1:
                    topLock = 0
                    shuffleLock1 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lock2Button.collidepoint(event.pos):
                if bottomLock == 0:
                    bottomLock = 1
                    shuffleLock2 = True
                elif bottomLock == 1:
                    bottomLock = 0
                    shuffleLock2 = False
        
    pygame.display.update()

pygame.quit()