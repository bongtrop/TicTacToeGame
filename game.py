import pygame
import time
import random
import copy

pygame.init()

size = width, height = 420, 420

screen = pygame.display.set_mode(size)

bg = pygame.image.load("image/board.png")
x = [pygame.image.load("image/x1.png"), pygame.image.load("image/x2.png")]
o = [pygame.image.load("image/o1.png"), pygame.image.load("image/o2.png")]

iw = 80
ih = 80

r = 0

board = [[0,0,0],
        [0,0,0],
        [0,0,0]]

turn = 1;
ended = False

def draw():
    screen.blit(bg, (0, 0))
    for i in range(3):
        for j in range(3):
            left = j*(width/3) + ((width/6)-(iw/2))
            top = i*(height/3) + ((height/6)-(ih/2))
            w = iw
            h = ih

            if board[i][j]<0:
                screen.blit(x[abs(board[i][j])-1], (left, top))
            elif board[i][j]>0:
                screen.blit(o[board[i][j]-1], (left, top))


    pygame.display.flip()

def click(pos):
    global turn
    global ended
    global r

    if not ended:
        for i in range(3):
            for j in range(3):
                left = j*(width/3) + ((width/6)-(iw/2))
                top = i*(height/3) + ((height/6)-(ih/2))
                w = iw
                h = ih

                if pos[0]>left and pos[0]<left+w and pos[1]>top and pos[1]<top+h and board[i][j]==0:
                    board[i][j] = random.randint(1,2)*turn
                    turn*=-1
                    r+=1

        print checkend()

        if checkend()!=0:
            ended = True
            print "end"

        if r==9:
            ended = True
            print "end"

def checkend():

    cboard = copy.deepcopy(board)

    # Preparing list
    for i in range(3):
        for j in range(3):
            if cboard[i][j]>0:
                cboard[i][j] = 1
            elif cboard[i][j]<0:
                cboard[i][j] = -1

    for i in range(3):
        # Horizonral
        s = 0
        for j in range(3):
            s+=cboard[i][j]

        if abs(s)==3:
            return s/3

        # Vertical
        s = 0
        for j in range(3):
            s+=cboard[j][i]

        if abs(s)==3:
            return s/3

    # Diagornal
    d = cboard[0][0]+cboard[1][1]+cboard[2][2]
    if abs(d)==3:
        return d/3

    d = cboard[0][2]+cboard[1][1]+cboard[2][0]
    if abs(d)==3:
        return d/3

    return 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            click(pos)

        if event.type == pygame.QUIT:
            exit()

    draw()
