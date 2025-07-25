import sys
import pygame
import datetime
import math
import pygame.freetype
import time
import random

pygame.init()



def ZeroField(n):
    return [[0] * n for i in range(n)]

def BetterZeroField(x, y):
    return [[0] * x for i in range(y)]

def checkTake(board, cellSide, selX, selY):
    for x in range(cellSide):
        for y in range(cellSide):
            if(abs(selX - x) == 2 and abs(selY - y) == 2 and board[x][y] == 0):
                return True
    return False


def main():
    side = 800
    cellSide = side/8
    selected = False
    screen = pygame.display.set_mode((side, side))
    running = True
    xIdx = 4
    yIdx = 4
    selX = 0
    selY = 0
    turn = 1
    board = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        ]
    
    board2 = [[0, 1, 0, 1, 0, 1, 0, 1], 
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1], 
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1], 
              [1, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1, 0, 1], 
              [1, 0, 1, 0, 1, 0, 1, 0],
              ]
    while running:
        pygame.display.flip()
        screen.fill((255, 255, 255))


        
        


        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, (0, 0, 0), (cellSide * 2 * j, cellSide * 2 * i, cellSide, cellSide))
                pygame.draw.rect(screen, (0, 0, 0), ((2 * j + 1) * cellSide, (2 * i + 1) * (cellSide), cellSide, cellSide))

        
        if(selected == True):
            pygame.draw.rect(screen, (255, 0, 0), (selX * cellSide, selY * (cellSide), cellSide, cellSide))
            for i in range(8):
                for j in range(8):
                    if(abs(selX - j) == 1 and abs(selY - i) == 1 and board[i][j] == 0):
                        board2[i][j] = 2
                        pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))
                    elif(board[i][j] == 0 and abs(selX - j) == 2 and abs(selY - i) == 2):
                        pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))
                    elif(board2[i][j] != 1):
                        board2[i][j] = 0
        pygame.draw.rect(screen, (0, 255, 0), (cellSide * xIdx, cellSide * yIdx, cellSide, cellSide))

        for i in range(8):
            for j in range(8):
                if(board[i][j] == 1):
                    pygame.draw.circle(screen, (255, 0, 255), (j * cellSide + 49, i * cellSide + 49), 49)
                elif(board[i][j] == 2):
                    pygame.draw.circle(screen, (0, 255, 255), (j * cellSide + 49, i * cellSide + 49), 49)

        
        
                        
            
        



        

        


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    if(xIdx > 0):
                        xIdx -= 1
                elif events.key == pygame.K_RIGHT:
                    if(xIdx < 7):
                        xIdx += 1
                elif events.key == pygame.K_UP:
                    if(yIdx > 0):
                        yIdx -= 1
                elif events.key == pygame.K_DOWN:
                    if(yIdx < 7):
                        yIdx += 1
                elif events.key == pygame.K_SPACE:
                    if(selected == False):
                        if(board2[xIdx][yIdx] == 0 and board[yIdx][xIdx] != 0):
                            if((turn == 1 and board[yIdx][xIdx] == 1) or (turn == 2 and board[yIdx][xIdx] == 2)):
                                selected = True
                                selX = xIdx
                                selY = yIdx
                    else:
                        if((abs(selX - xIdx) == 1 and abs(selY - yIdx) == 1)):

                            a = board[yIdx][xIdx]
                            # if(board[yIdx][xIdx] == 0 or board[selY][selX] == 0):
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            print(board[yIdx][xIdx])
                            print(board[selY][selY])
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        if((abs(selX - xIdx) == 2 and abs(selY - yIdx) == 2)):
                            a = board[yIdx][xIdx]
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            print(board[yIdx][xIdx])
                            print(board[selY][selY])
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                # if(abs(selX - xIdx - 1) == 1 and abs(selY - yIdx - 1) == 1 and board[xIdx][yIdx] != 0):
                                #     board[xIdx][yIdx] = 0
                                for x in range (len(board)):
                                    for y in range(len(board)):
                                        if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs):
                                            board[y][x] = 0

                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        selected = False
                        
                        
                        

    
main()