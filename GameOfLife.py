import pygame
from Square import Square
import sys
import getopt
from random import randint
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def create_board(wide, high):
    board = []

    for row in range(high):
        rowBoard = []
        for col in range(wide):
            currSquare = Square(left=(Square.margin + Square.width) * col + Square.margin,
                                top=(Square.margin + Square.width) * row + Square.margin,
                                 state=0)
            rowBoard.append(currSquare)
        board.append(rowBoard)

    return board

def getNextState(board, i, j):
    topLeft = 0
    topMid = 0
    topRight = 0
    rightMid = 0
    rightBottom = 0
    bottomMid = 0
    bottomLeft = 0
    leftMid = 0
    # print(i, j)
    if j - 1 >= 0:
        leftMid = board[i][j-1].getState()
    if j + 1 <= len(board[0]) - 1:
        rightMid = board[i][j+1].getState()
    if i - 1 >= 0:
        topMid = board[i-1][j].getState()
    if i + 1 <= len(board) - 1:
        bottomMid = board[i+1][j].getState()
    if j - 1 >= 0 and i -1 >= 0:
        topLeft = board[i-1][j-1].getState()
    if j - 1 >= 0 and i + 1 <= len(board) - 1:
        bottomLeft = board[i+1][j-1].getState()
    if j + 1 <= len(board[0]) - 1 and i - 1 >= 0:
        topRight = board[i-1][j+1].getState()
    if j + 1 <= len(board[0]) - 1 and i + 1 <= len(board) - 1:
        rightBottom = board[i+1][j+1].getState()

    currCell = board[i][j]
    currState = currCell.getState()
    aliveCell = topLeft + topMid + topRight + rightMid + rightBottom + bottomMid + bottomLeft + leftMid
    #print(aliveCell)
    returnState = 0

    if currState == 1 and (aliveCell == 2 or aliveCell == 3):
        returnState = 1
    elif currState == 0 and aliveCell == 3:
        returnState = 1

    # print(currState, returnState)
    return returnState


def updateBoard(board):
    changes = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            nextState = getNextState(board, i, j)
            changes[tuple([i, j])] = nextState


    for key, value in changes.items():
            board[key[0]][key[1]].state = value

def initializeStartingPattern(board, preset):
    presets = {
        'glider': [
                    (len(board)//2-2, len(board[0])//2-1),
                    (len(board)//2-1, len(board[0])//2),
                    (len(board)//2, len(board[0])//2),
                    (len(board)//2, len(board[0])//2-1),
                    (len(board)//2, len(board[0])//2-2)
                    ],
        'blinker': [
                    (len(board) // 2, len(board[0]) // 2),
                    (len(board) // 2, len(board[0]) // 2+1),
                    (len(board) // 2, len(board[0]) // 2-1)
                    ],
        'toad': [
                (len(board)//2, len(board[0])//2),
                (len(board)//2, len(board[0])//2+1),
                (len(board)//2+1, len(board[0])//2),
                (len(board)//2+1, len(board[0])//2+1),
                (len(board)//2, len(board[0])//2+2),
                (len(board)//2+1, len(board[0])//2-1)
                ],
        'random': [(randint(0, len(board)-1), randint(0, len(board[0])-1)) for i in range(500)]
        }

    for coord in presets[preset]:
        board[coord[0]][coord[1]].state = 1




def main(argv):
    wide=100
    high = 50
    preset = "glider"
    sleep = 0
    try:
        opts, args = getopt.getopt(argv, "w:h:p:s:", ["width=", "height=", "preset=", "sleep="])
    except getopt.GetoptError:
        print ('test.py -w <width> -h <height>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-w", "--width"):
            wide = int(arg)
        elif opt in ("-h", "--height"):
            high = int(arg)
        elif opt in ("-p", "--preset"):
            preset = arg
        elif opt in ("-s", "--sleep"):
            sleep = int(arg)

    pygame.init()

    screen = pygame.display.set_mode([(wide * Square.width) + (2 * (wide + 1)), (high * Square.width) + (2 * (high + 1))])
    done = False
    clock = pygame.time.Clock()

    board = create_board(wide, high)
    initializeStartingPattern(board, preset)

    # print(getNextState(board,3,3))
    # exit()


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        screen.fill(BLACK)

        for row in board:
            for col in row:
                pos = col.getPos()
                color = col.getColor()
                pygame.draw.rect(screen,
                                color,
                                [pos[0], pos[1],
                                Square.width,
                                Square.width])

        updateBoard(board)
        if sleep != 0:
            time.sleep(0.5)
        clock.tick(60)

        pygame.display.flip()



if __name__ == '__main__':
    main(sys.argv[1:])
