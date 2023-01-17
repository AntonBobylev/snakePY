import pygame
import random

pygame.init()

displayWidth = 800
displayHeight = 600
windowCaption = "Snake"

snakeSpeed = 15
snakeSize = 10

yellowColor = (255, 255, 102)
blackColor  = (0, 0, 0)
redColor = (213, 50, 80)
greenColor = (0, 255, 0)
blueColor = (50, 153, 213)

display = pygame.display.set_mode((displayWidth, displayHeight));
pygame.display.set_caption(windowCaption)

clock = pygame.time.Clock()

def displaySnakeParts(snakeBlock, snakeList):
    for coordinates in snakeList:
        pygame.draw.rect(display, blackColor, [coordinates[0], coordinates[1], snakeBlock, snakeBlock])
    
    pygame.display.update()

def displayCustomMessage(msg, color):
    font = pygame.font.SysFont("bahnschrift", 25);
    
    message = font.render(msg, True, color);
    display.blit(message, [displayWidth / 6, displayHeight / 3])

    pygame.display.update()

def displayPlayerScore(score):
    font = pygame.font.SysFont("comicsansms", 35);
    
    value = font.render("Your score: " + str(score), True, yellowColor)
    display.blit(value, [0, 0])

    pygame.display.update()

def getFieldRandomXPos():
    return round(random.randrange(0, displayWidth - snakeSize ) / 10.0) * 10.0

def getFieldRandomYPos():
    return round(random.randrange(0, displayHeight - snakeSize ) / 10.0) * 10.0

def snakeEat(snakeLength):
    foodX = getFieldRandomXPos()
    foodY = getFieldRandomYPos()
    snakeLength += 1

    return foodX, foodY, snakeLength

def gameLoop():
    gameOver = False;
    gameClose = False;

    xPos = displayWidth / 2
    yPos = displayHeight / 2

    xPosOffset = 0
    yPosOffset = 0

    snakeList = []
    snakeLength = 1

    foodX = getFieldRandomXPos()
    foodY = getFieldRandomYPos()

    while not gameOver:
        while gameClose == True:
            display.fill(blueColor)

            displayCustomMessage("You lose! Press Q to exit or C for retry", redColor)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xPosOffset = -snakeSize
                    yPosOffset = 0
                elif event.key == pygame.K_RIGHT:
                    xPosOffset = snakeSize
                    yPosOffset = 0
                elif event.key == pygame.K_UP:
                    yPosOffset = -snakeSize
                    xPosOffset = 0
                elif event.key == pygame.K_DOWN:
                    yPosOffset = snakeSize
                    xPosOffset = 0
        
        if xPos >= displayWidth or xPos < 0 or yPos >= displayHeight or yPos < 0:
            gameClose = True

        xPos += xPosOffset
        yPos += yPosOffset

        display.fill(blueColor)

        pygame.draw.rect(display, greenColor, [foodX, foodY, snakeSize, snakeSize])

        snakeHead = []
        snakeHead.append(xPos)
        snakeHead.append(yPos)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        displaySnakeParts(snakeSize, snakeList)

        if xPos == foodX and yPos == foodY:
            eatingResult = snakeEat(snakeLength)
            foodX = eatingResult[0]
            foodY = eatingResult[1]
            snakeLength = eatingResult[2]
            
        displayPlayerScore(snakeLength)

        clock.tick(snakeSpeed)
    pygame.quit()

    quit()

gameLoop()