import pygame
from Square import Square
import sys
import getopt


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
            if row == 0 and col == wide // 2:
                currSquare.state = 1
            rowBoard.append(currSquare)
        board.append(rowBoard)

    return board

def toBinaryArray(num):
    return [int(x) for x in f'{num:08b}']

def getRuleSet(num):

    arr = toBinaryArray(num)
    ruleSet = {}
    j=7
    for i in range(len(arr)):
        pos = tuple([int(x) for x in f'{j:03b}'])
        ruleSet[pos] = arr[i]
        j-=1

    return ruleSet

def updateBoard(ruleSet, board):
    for i in range(1, len(board)):
        for j in range(len(board[i])):
            board[i][j].state = getNextState(ruleSet, board, i, j)

def getNextState(ruleSet, board, i, j):
    if j == 0:
        leftNeighbor = 0
    else:
        leftNeighbor = board[i-1][j-1].getState()
    if j == len(board[0])-1:
        rightNeighbor = 0
    else:
        rightNeighbor = board[i-1][j+1].getState()
    topNeighbor = board[i-1][j].getState()


    return ruleSet[tuple([leftNeighbor, topNeighbor, rightNeighbor])]

def main(argv):
    wide=101
    high = 50
    ruleNum = 30
    try:
        opts, args = getopt.getopt(argv, "w:h:r:", ["width=", "height=", "rule="])
    except getopt.GetoptError:
        print ('test.py -w <width> -h <height> -r <rule>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-w", "--width"):
            wide = int(arg)
        elif opt in ("-h", "--height"):
            high = int(arg)
        elif opt in ("-r", "--rule"):
            ruleNum = int(arg)

    pygame.init()

    screen = pygame.display.set_mode([(wide * Square.width) + (2 * (wide + 1)), (high * Square.width) + (2 * (high + 1))])
    done = False
    clock = pygame.time.Clock()

    board = create_board(wide, high)
    ruleSet = getRuleSet(ruleNum)
    updateBoard(ruleSet, board)

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

        clock.tick(60)

        pygame.display.flip()


if __name__ == '__main__':
    main(sys.argv[1:])
