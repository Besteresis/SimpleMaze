import pygame
import sys
import random
from Cube import Cube
import time
pygame.init()


def makeCube(numberOfCubesOnAxis, posX, posY):
    border = [0,0,0,0]
    if posX == 0:
        border[3] = 1
    elif posX == numberOfCubesOnAxis - 1:
        border[1] = 1
    if posY == 0:
        border[0] = 1
    elif posY == numberOfCubesOnAxis - 1:
        border[2] = 1
    return Cube(border, posX, posY)

def getOppositeDirection(direction):
    if direction == 0:
        return 2
    elif direction == 1:
        return 3
    elif direction == 2:
        return 0
    elif direction == 3:
        return 1
    else:
        print("There is no opposite of this direction: " + str(direction))
        exit()


numberOfCubesOnAxis = 20
cubeLength = 25
borderLength = 5
width = numberOfCubesOnAxis * cubeLength + (numberOfCubesOnAxis - 1) * borderLength
height = numberOfCubesOnAxis * cubeLength + (numberOfCubesOnAxis - 1) * borderLength
black = 0, 0, 0
white = 255, 255, 255
purple = 255, 0, 255
green = 0, 255, 0

screen = pygame.display.set_mode((width, height))
screen.fill(black)

cubeMap = [[0 for i in range(numberOfCubesOnAxis)] for j in range(numberOfCubesOnAxis)]
pointerX = 0
pointerY = 0
cubeMap[0][0] = makeCube(numberOfCubesOnAxis, pointerX, pointerY)
curCube = cubeMap[0][0]
path = [[0, 0]]
lastDirection = -1
pathAvailable = 2
while 1:
    curCube = cubeMap[pointerX][pointerY]
    border = curCube.getBorder()
    directions = [0, 0, 0, 0]
    if pointerY != 0:
        if cubeMap[pointerX][pointerY - 1] == 0:
            directions[0] = 1
    if pointerX != numberOfCubesOnAxis - 1:
        if cubeMap[pointerX + 1][pointerY] == 0:
            directions[1] = 1
    if pointerY != numberOfCubesOnAxis - 1:
        if cubeMap[pointerX][pointerY + 1] == 0:
            directions[2] = 1
    if pointerX != 0:
        if cubeMap[pointerX - 1][pointerY] == 0:
            directions[3] = 1
    choosenDirection = -1
    if directions.count(1) == 0:
        if pointerX == 0 and pointerY == 0:
            break
        if lastDirection != 0 and pathAvailable == 2:
            border[2] = 1
        if lastDirection != 1 and pathAvailable == 2:
            border[3] = 1
        if lastDirection != 2 and pathAvailable == 2:
            border[0] = 1
        if lastDirection != 3 and pathAvailable == 2:
            border[1] = 1
        pathAvailable = 0
        del path[-1]
        pointerX = path[len(path) - 1][0]
        pointerY = path[len(path) - 1][1]
    elif directions.count(1) == 1:
        if pathAvailable == 0:
            pathAvailable = 1
        choosenDirection = directions.index(1)
    else:
        if pathAvailable == 0:
            pathAvailable = 1
        randomDirection = random.randint(0, directions.count(1) - 1)
        for i in range(len(directions)):
            if directions[i] == 1:
                if randomDirection != 0:
                    randomDirection -= 1
                else:
                    choosenDirection = i
                    break
    if choosenDirection == 0:
        if pathAvailable == 2:
            if lastDirection != 0:
                border[2] = 1
            if lastDirection != 1:
                border[3] = 1
            if lastDirection != 3:
                border[1] = 1
        lastDirection = 0
        pointerY -= 1
        border[0] = 0
    elif choosenDirection == 1:
        if pathAvailable == 2:
            if lastDirection != 0:
                border[2] = 1
            if lastDirection != 1:
                border[3] = 1
            if lastDirection != 2:
                border[0] = 1
        lastDirection = 1
        pointerX += 1
        border[1] = 0
    elif choosenDirection == 2:
        if pathAvailable == 2:
            if lastDirection != 1:
                border[3] = 1
            if lastDirection != 2:
                border[0] = 1
            if lastDirection != 3:
                border[1] = 1
        lastDirection = 2
        pointerY += 1
        border[2] = 0
    elif choosenDirection == 3:
        if pathAvailable == 2:
            if lastDirection != 0:
                border[2] = 1
            if lastDirection != 2:
                border[0] = 1
            if lastDirection != 3:
                border[1] = 1
        lastDirection = 3
        pointerX -= 1
        border[3] = 0
    curCube.setBorder(border)
    if pathAvailable > 0:
        path.append([pointerX, pointerY])
        cubeMap[pointerX][pointerY] = makeCube(numberOfCubesOnAxis, pointerX, pointerY)
        pathAvailable = 2
    screen.fill(black)
    for i in range(numberOfCubesOnAxis):
        for j in range(numberOfCubesOnAxis):
            if cubeMap[i][j] != 0:
                pygame.draw.rect(screen, white,
                                 pygame.Rect(i * (cubeLength + borderLength), j * (cubeLength + borderLength),
                                             cubeLength, cubeLength))
                border = cubeMap[i][j].getBorder()
                if border[0] == 1:
                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                 j * (cubeLength + borderLength) - borderLength,
                                                                 cubeLength, borderLength))
                    #pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength/2 , j * (cubeLength + borderLength) + cubeLength/2 - 5), 3)
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                 j * (cubeLength + borderLength) - borderLength,
                                                                 cubeLength, borderLength))
                if border[1] == 1:
                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                    #pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 + 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                if border[2] == 1:
                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                 j * (cubeLength + borderLength) + cubeLength,
                                                                 cubeLength, borderLength))
                    #pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2, j * (cubeLength + borderLength) + cubeLength / 2 + 5), 3)
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                 j * (cubeLength + borderLength) + cubeLength,
                                                                 cubeLength, borderLength))
                if border[3] == 1:
                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                    #pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 - 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                else: pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                          j * (cubeLength + borderLength) - borderLength,
                                                          borderLength, borderLength))
                pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                          j * (cubeLength + borderLength) + cubeLength,
                                                          borderLength, borderLength))
                pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                          j * (cubeLength + borderLength) + cubeLength,
                                                          borderLength, borderLength))
                pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                          j * (cubeLength + borderLength) - borderLength,
                                                          borderLength, borderLength))
    pygame.display.flip()
    #time.sleep(1)

playerPath = [[0,0,-1]]
gameActive = 1
lastDirection = -1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if gameActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and cubeMap[playerPath[-1][0]][playerPath[-1][1]].getBorder()[0] == 0:
                    if playerPath[-2][2] != 2:
                        playerPath[-1][2] = 0
                        playerPath.append([playerPath[-1][0], playerPath[-1][1] - 1, -1])
                    else:
                        del playerPath[-1]
                        playerPath[-1][2] = -1
                elif event.key == pygame.K_RIGHT and cubeMap[playerPath[-1][0]][playerPath[-1][1]].getBorder()[1] == 0:
                    if playerPath[-1][:2] == [0,0] or playerPath[-2][2] != 3:
                        playerPath[-1][2] = 1
                        playerPath.append([playerPath[-1][0] + 1, playerPath[-1][1], -1])
                    else:
                        del playerPath[-1]
                        playerPath[-1][2] = -1
                    lastDirection = 1
                elif event.key == pygame.K_DOWN and cubeMap[playerPath[-1][0]][playerPath[-1][1]].getBorder()[2] == 0:
                    if playerPath[-1][:2] == [0,0] or playerPath[-2][2] != 0:
                        playerPath[-1][2] = 2
                        playerPath.append([playerPath[-1][0], playerPath[-1][1] + 1, -1])
                    else:
                        del playerPath[-1]
                        playerPath[-2][2] = -1
                    lastDirection = 2
                elif event.key == pygame.K_LEFT and cubeMap[playerPath[-1][0]][playerPath[-1][1]].getBorder()[3] == 0:
                    if playerPath[-2][2] != 1:
                        playerPath[-1][2] = 3
                        playerPath.append([playerPath[-1][0] - 1, playerPath[-1][1], -1])
                    else:
                        del playerPath[-1]
                        playerPath[-1][2] = -1
                    lastDirection = 3
                if playerPath[-1][:2] == [numberOfCubesOnAxis - 1, numberOfCubesOnAxis - 1]:
                    gameActive = 0
                    screen.fill(black)
                    for i in range(numberOfCubesOnAxis):
                        for j in range(numberOfCubesOnAxis):
                            if cubeMap[i][j] != 0:
                                pygame.draw.rect(screen, white,
                                                 pygame.Rect(i * (cubeLength + borderLength),
                                                             j * (cubeLength + borderLength),
                                                             cubeLength, cubeLength))
                                border = cubeMap[i][j].getBorder()
                                if border[0] == 1:
                                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                                j * (
                                                                                            cubeLength + borderLength) - borderLength,
                                                                                cubeLength, borderLength))
                                    # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength/2 , j * (cubeLength + borderLength) + cubeLength/2 - 5), 3)
                                else:
                                    pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                                j * (
                                                                                            cubeLength + borderLength) - borderLength,
                                                                                cubeLength, borderLength))
                                if border[1] == 1:
                                    pygame.draw.rect(screen, black,
                                                     pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                                    # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 + 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                                else:
                                    pygame.draw.rect(screen, white,
                                                     pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                                if border[2] == 1:
                                    pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                                j * (
                                                                                            cubeLength + borderLength) + cubeLength,
                                                                                cubeLength, borderLength))
                                    # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2, j * (cubeLength + borderLength) + cubeLength / 2 + 5), 3)
                                else:
                                    pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                                j * (
                                                                                            cubeLength + borderLength) + cubeLength,
                                                                                cubeLength, borderLength))
                                if border[3] == 1:
                                    pygame.draw.rect(screen, black,
                                                     pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                                    # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 - 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                                else:
                                    pygame.draw.rect(screen, white,
                                                     pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                 j * (cubeLength + borderLength), borderLength,
                                                                 cubeLength))
                                pygame.draw.rect(screen, black,
                                                 pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                             j * (cubeLength + borderLength) - borderLength,
                                                             borderLength, borderLength))
                                pygame.draw.rect(screen, black,
                                                 pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                             j * (cubeLength + borderLength) + cubeLength,
                                                             borderLength, borderLength))
                                pygame.draw.rect(screen, black,
                                                 pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                             j * (cubeLength + borderLength) + cubeLength,
                                                             borderLength, borderLength))
                                pygame.draw.rect(screen, black,
                                                 pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                             j * (cubeLength + borderLength) - borderLength,
                                                             borderLength, borderLength))
                    for i in range(len(playerPath)):
                        pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                     playerPath[i][1] * (cubeLength + borderLength),
                                                                     cubeLength, cubeLength))
                        if playerPath[i][2] == 0:
                            pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                         playerPath[i][1] * (
                                                                                     cubeLength + borderLength) - borderLength,
                                                                         cubeLength, borderLength))
                        elif playerPath[i][2] == 1:
                            pygame.draw.rect(screen, purple,
                                             pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) + cubeLength,
                                                         playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                         cubeLength))
                        elif playerPath[i][2] == 2:
                            pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                         playerPath[i][1] * (
                                                                                     cubeLength + borderLength) + cubeLength,
                                                                         cubeLength, borderLength))
                        elif playerPath[i][2] == 3:
                            pygame.draw.rect(screen, purple,
                                             pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) - borderLength,
                                                         playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                         cubeLength))
                    for i in range(len(playerPath)):
                        pygame.draw.rect(screen, green, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                     playerPath[i][1] * (cubeLength + borderLength),
                                                                     cubeLength, cubeLength))
                        if playerPath[i][2] == 0:
                            pygame.draw.rect(screen, green, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                         playerPath[i][1] * (
                                                                                     cubeLength + borderLength) - borderLength,
                                                                         cubeLength, borderLength))
                        elif playerPath[i][2] == 1:
                            pygame.draw.rect(screen, green,
                                             pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) + cubeLength,
                                                         playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                         cubeLength))
                        elif playerPath[i][2] == 2:
                            pygame.draw.rect(screen, green, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                         playerPath[i][1] * (
                                                                                     cubeLength + borderLength) + cubeLength,
                                                                         cubeLength, borderLength))
                        elif playerPath[i][2] == 3:
                            pygame.draw.rect(screen, green,
                                             pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) - borderLength,
                                                         playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                         cubeLength))
                        pygame.display.flip()
                        time.sleep(0.05)
                    continue
            screen.fill(black)
            for i in range(numberOfCubesOnAxis):
                for j in range(numberOfCubesOnAxis):
                    if cubeMap[i][j] != 0:
                        pygame.draw.rect(screen, white,
                                         pygame.Rect(i * (cubeLength + borderLength), j * (cubeLength + borderLength),
                                                     cubeLength, cubeLength))
                        border = cubeMap[i][j].getBorder()
                        if border[0] == 1:
                            pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                        j * (cubeLength + borderLength) - borderLength,
                                                                        cubeLength, borderLength))
                            # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength/2 , j * (cubeLength + borderLength) + cubeLength/2 - 5), 3)
                        else:
                            pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                        j * (cubeLength + borderLength) - borderLength,
                                                                        cubeLength, borderLength))
                        if border[1] == 1:
                            pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                        j * (cubeLength + borderLength), borderLength,
                                                                        cubeLength))
                            # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 + 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                        else:
                            pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                        j * (cubeLength + borderLength), borderLength,
                                                                        cubeLength))
                        if border[2] == 1:
                            pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength),
                                                                        j * (cubeLength + borderLength) + cubeLength,
                                                                        cubeLength, borderLength))
                            # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2, j * (cubeLength + borderLength) + cubeLength / 2 + 5), 3)
                        else:
                            pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength),
                                                                        j * (cubeLength + borderLength) + cubeLength,
                                                                        cubeLength, borderLength))
                        if border[3] == 1:
                            pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                        j * (cubeLength + borderLength), borderLength,
                                                                        cubeLength))
                            # pygame.draw.circle(screen, blue, (i * (cubeLength + borderLength) + cubeLength / 2 - 5, j * (cubeLength + borderLength) + cubeLength / 2), 3)
                        else:
                            pygame.draw.rect(screen, white, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                        j * (cubeLength + borderLength), borderLength,
                                                                        cubeLength))
                        pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                    j * (cubeLength + borderLength) - borderLength,
                                                                    borderLength, borderLength))
                        pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) + cubeLength,
                                                                    j * (cubeLength + borderLength) + cubeLength,
                                                                    borderLength, borderLength))
                        pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                    j * (cubeLength + borderLength) + cubeLength,
                                                                    borderLength, borderLength))
                        pygame.draw.rect(screen, black, pygame.Rect(i * (cubeLength + borderLength) - borderLength,
                                                                    j * (cubeLength + borderLength) - borderLength,
                                                                    borderLength, borderLength))
            for i in range(len(playerPath)):
                pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                            playerPath[i][1] * (cubeLength + borderLength),
                                                            cubeLength, cubeLength))
                if playerPath[i][2] == 0:
                    pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                playerPath[i][1] * (cubeLength + borderLength) - borderLength,
                                                                cubeLength, borderLength))
                elif playerPath[i][2] == 1:
                    pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) + cubeLength,
                                                                playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                                cubeLength))
                elif playerPath[i][2] == 2:
                    pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength),
                                                                playerPath[i][1] * (cubeLength + borderLength) + cubeLength,
                                                                cubeLength, borderLength))
                elif playerPath[i][2] == 3:
                    pygame.draw.rect(screen, purple, pygame.Rect(playerPath[i][0] * (cubeLength + borderLength) - borderLength,
                                                                playerPath[i][1] * (cubeLength + borderLength), borderLength,
                                                                cubeLength))

            pygame.display.flip()
            # time.sleep(1)