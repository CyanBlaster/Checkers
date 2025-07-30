import sys
import pygame
import datetime
import math
import pygame.freetype
import time
import random

pygame.init()


GAME_FONT = pygame.font.Font(None, 24)
GAME_FONT2 = pygame.font.Font(None, 36)

def ZeroField(n):
    return [[0] * n for i in range(n)]

def BetterZeroField(x, y):
    return [[0] * x for i in range(y)]

def main():
    side = 800
    cellSide = side/8
    selected = False
    screen = pygame.display.set_mode((side + 200, side))
    running = True
    guidance = False
    xIdx = 4
    yIdx = 4
    selX = 0
    selY = 0
    turn = 1
    OneLoss = 0
    TwoLoss = 0
    piecesLeftBlue = 12
    piecesLeftPink = 12

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
    # 
    
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

        pygame.draw.rect(screen, (0, 0, 0), (800, 0, 200, 800))
        pygame.draw.rect(screen, (255, 255, 255), (800, 0, 1, 800))
        if(turn == 1):
            pygame.draw.rect(screen, (255, 0, 255), (850, 350, 100, 100))
            text_surface = GAME_FONT.render("Pink", True, (255, 0, 255))
            screen.blit(text_surface, (875, 320))
            text_surface = GAME_FONT.render("Turn:", True, (255, 0, 255))
            screen.blit(text_surface, (875, 300))
        else:
            pygame.draw.rect(screen, (0, 255, 255), (850, 350, 100, 100))
            text_surface = GAME_FONT.render("Blue", True, (0, 255, 255))
            screen.blit(text_surface, (875, 320))
            text_surface = GAME_FONT.render("Turn:", True, (0, 255, 255))
            screen.blit(text_surface, (875, 300))

        text_surface = GAME_FONT.render("Guidance:", True, (255, 255, 255))
        screen.blit(text_surface, (825, 600))
        text_surface = GAME_FONT.render(str(guidance), True, (255, 255, 255))
        screen.blit(text_surface, (925, 600))



        

        text_surface = GAME_FONT2.render("Pieces Left:", True, (255, 0, 255))
        screen.blit(text_surface, (820, 100))
        text_surface = GAME_FONT2.render(str(piecesLeftPink), True, (255, 0, 255))
        screen.blit(text_surface, (870, 120))
        text_surface = GAME_FONT2.render("Pieces Left:", True, (0, 255, 255))
        screen.blit(text_surface, (820, 500))
        text_surface = GAME_FONT2.render(str(piecesLeftBlue), True, (0, 255, 255))
        screen.blit(text_surface, (870, 520))
        
        


        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, (0, 0, 0), (cellSide * 2 * j, cellSide * 2 * i, cellSide, cellSide))
                pygame.draw.rect(screen, (0, 0, 0), ((2 * j + 1) * cellSide, (2 * i + 1) * (cellSide), cellSide, cellSide))




        
        if(selected == True and guidance == True):
            pygame.draw.rect(screen, (255, 0, 0), (selX * cellSide, selY * (cellSide), cellSide, cellSide))
            for i in range(8):
                for j in range(8):
                    if((board[selY][selX] == 3 or board[selY][selX] == 4) and abs(selX - j) == 1 and abs(selY - i) == 1 and board[i][j] == 0):
                        board2[i][j] = 2
                        pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))
                    
                    
                    # elif((board[i][j] == 0 and abs(selX - j) == 2 and abs(selY - i) == 2)):
                    #     pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))

                    if((board[selY][selX] == 1) and abs(selX - j) == 1 and i - selY == 1 and board[i][j] == 0):
                        board2[i][j] = 2
                        pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))
                    if((board[selY][selX] == 2) and abs(selX - j) == 1 and selY - i == 1 and board[i][j] == 0):
                        board2[i][j] = 2
                        pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))



                    
                    # elif(board[i][j] == 0 and abs(selX - j) == 2 and abs(selY - i) == 2 and ((abs(selX - 1 - j) == 1 and abs(selY - 1 - i) == 1) or (abs(selX + 1 - j) == 1 and abs(selY - 1 - i) == 1) or (abs(selX - 1 - j) == 1 and abs(selY + 1 - i) == 1) or (abs(selX + 1 - j) == 1 and abs(selY + 1 - i) == 1))):
                    
                    if((abs(j - 1 - selX) == 1 and abs(i - 1 - selY) == 1 and selY > 0 and selX > 0 and board[selY - 1][selX - 1] == 0) or (abs(j - 1 - selX) == 1 and abs(i + 1 - selY) == 1) or (abs(j + 1 - selX) == 1 and abs(i + 1 - selY) == 1) or (abs(j + 1 - selX) == 1 and abs(i - 1 - selY) == 1)):
                        if(abs(j - selX) == 2 and abs(i - selY) == 2 and board[j][i] == 0):
                            pygame.draw.rect(screen, (255, 0, 0), (j * cellSide, cellSide * i, cellSide, cellSide))

                    # elif(board2[i][j] != 1):
                    #     board2[i][j] = 0


        pygame.draw.rect(screen, (0, 255, 0), (cellSide * xIdx, cellSide * yIdx, cellSide, cellSide))

        for i in range(8):
            for j in range(8):
                if(board[i][j] == 1):
                    pygame.draw.circle(screen, (255, 0, 255), (j * cellSide + 49, i * cellSide + 49), 49)
                elif(board[i][j] == 2):
                    pygame.draw.circle(screen, (0, 255, 255), (j * cellSide + 49, i * cellSide + 49), 49)
                elif(board[i][j] == 3):
                    pygame.draw.circle(screen, (200, 0, 200), (j * cellSide + 49, i * cellSide + 49), 49)
                elif(board[i][j] == 4):
                    pygame.draw.circle(screen, (0, 200, 200), (j * cellSide + 49, i * cellSide + 49), 49)

        
        # if(selected == True):
        #         for x in range (len(board)):
        #             for y in range(len(board)):
        #                 if(board[selY][selX] == 0):
        #                     if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs(x - xIdx) == 1 and abs(y - yIdx) == 1):
        #                         pygame.draw.rect(screen, (255, 0, 0), (x * cellSide, cellSide * y, cellSide, cellSide))



        

        # Check for win

        for y in range(8):
            for x in range(8):
                if(board[x][y] != 1):
                    OneLoss += 1
        if(OneLoss == 64):
            print("Blue win")
            running = False
        else:
            OneLoss = 0

        for y in range(8):
            for x in range(8):
                if(board[x][y] != 2):
                    TwoLoss += 1
        if(TwoLoss == 64):
            print("Pink win")
            running = False
        else:
            TwoLoss = 0


        # Kings pieces

        for x in range(8):
            if(board[7][x] == 1):
                board[7][x] = 3
        for x in range(8):
            if(board[0][x] == 2):
                board[0][x] = 4


        # Counts pieces
        p = 0
        b = 0
        for y in range(8):
            for x in range(8):
                if(board[y][x] == 1):
                    p += 1
                if(board[y][x] == 2):
                    b += 1
        piecesLeftBlue = b
        piecesLeftPink = p


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
                elif events.key == pygame.K_1:
                    if(guidance == False):
                        guidance = True
                    else:
                        guidance = False
                elif events.key == pygame.K_b:
                    print(board)
                elif events.key == pygame.K_SPACE:
                    if(selected == False):
                        if(board2[xIdx][yIdx] == 0 and board[yIdx][xIdx] != 0):
                            if((turn == 1 and (board[yIdx][xIdx] == 1 or board[yIdx][xIdx] == 3)) or (turn == 2 and (board[yIdx][xIdx] == 2 or board[yIdx][xIdx] == 4))):
                                selected = True
                                selX = xIdx
                                selY = yIdx
                    else:
                        if((abs(selX - xIdx) == 1 and abs(selY - yIdx) == 1) and (board[selY][selX] == 3 or board[selY][selX] == 4)):
                            a = board[yIdx][xIdx]
                            # if(board[yIdx][xIdx] == 0 or board[selY][selX] == 0):
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        else:
                            print(selY, selX, board[selY][selX])
                        


                        # if((abs(selX - xIdx) == 2 and abs(selY - yIdx) == 2)):
                        #     a = board[yIdx][xIdx]
                        #     board[yIdx][xIdx] = board[selY][selX]
                        #     board[selY][selX] = a
                        #     if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                        #         a = board[yIdx][xIdx]
                        #         board[yIdx][xIdx] = board[selY][selX]
                        #         board[selY][selX] = a
                        #     else:
                        #         # if(abs(selX - xIdx - 1) == 1 and abs(selY - yIdx - 1) == 1 and board[xIdx][yIdx] != 0):
                        #         #     board[xIdx][yIdx] = 0
                        #         for x in range (len(board)):
                        #             for y in range(len(board)):
                        #                 if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs(x - xIdx) == 1 and abs(y - yIdx) == 1):
                        #                     board[y][x] = 0

                        #         if(turn == 1):
                        #             turn = 2
                        #         else:
                        #             turn = 1
                        # selected = False


                        if((abs(selX - xIdx) == 1 and yIdx - selY == 1) and board[selY][selX] == 1):

                            a = board[yIdx][xIdx]
                            # if(board[yIdx][xIdx] == 0 or board[selY][selX] == 0):
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1

                        if((abs(selX - xIdx) == 1 and selY - yIdx == 1) and board[selY][selX] == 2):

                            a = board[yIdx][xIdx]
                            # if(board[yIdx][xIdx] == 0 or board[selY][selX] == 0):
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        
                        if((abs(selX - xIdx) == 2 and yIdx - selY == 2 and board[selY][selX] == 1)):
                            a = board[yIdx][xIdx]
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                # if(abs(selX - xIdx - 1) == 1 and abs(selY - yIdx - 1) == 1 and board[xIdx][yIdx] != 0):
                                #     board[xIdx][yIdx] = 0
                                for x in range (len(board)):
                                    for y in range(len(board)):
                                        if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs(x - xIdx) == 1 and abs(y - yIdx) == 1):
                                            if((turn == 1 and board[y][x] == 2) or (turn == 2 and board[y][x] == 1)):
                                                print("Delete at", x, y)
                                                board[y][x] = 0

                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        
                        if((abs(selX - xIdx) == 2 and selY - yIdx == 2 == 2 and board[selY][selX] == 2)):
                            a = board[yIdx][xIdx]
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                # if(abs(selX - xIdx - 1) == 1 and abs(selY - yIdx - 1) == 1 and board[xIdx][yIdx] != 0):
                                #     board[xIdx][yIdx] = 0
                                for x in range (len(board)):
                                    for y in range(len(board)):
                                        if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs(x - xIdx) == 1 and abs(y - yIdx) == 1):
                                            if((turn == 1 and board[y][x] == 2) or (turn == 2 and board[y][x] == 1)):
                                                print("Delete at", x, y)
                                                board[y][x] = 0

                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        selected = False
                        if((abs(selX - xIdx) == 2 and abs(selY - yIdx) == 2 == 2 and (board[selY][selX] == 3 or board[selY][selX] == 4))):
                            a = board[yIdx][xIdx]
                            board[yIdx][xIdx] = board[selY][selX]
                            board[selY][selX] = a
                            if(board[yIdx][xIdx] != 0 and board[selY][selX] != 0):
                                a = board[yIdx][xIdx]
                                board[yIdx][xIdx] = board[selY][selX]
                                board[selY][selX] = a
                            else:
                                # if(abs(selX - xIdx - 1) == 1 and abs(selY - yIdx - 1) == 1 and board[xIdx][yIdx] != 0):
                                #     board[xIdx][yIdx] = 0
                                for x in range (len(board)):
                                    for y in range(len(board)):
                                        if(abs(selX - x) == 1 and abs(selY - y) == 1 and board[y][x] != 0 and abs(x - xIdx) == 1 and abs(y - yIdx) == 1):
                                            if((turn == 1 and board[y][x] == 2) or (turn == 2 and board[y][x] == 1)):
                                                print("Delete at", x, y)
                                                board[y][x] = 0

                                if(turn == 1):
                                    turn = 2
                                else:
                                    turn = 1
                        selected = False
                        
                        

    
main()