import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MARGIN = 2
SQUARE_WIDTH = 10
pygame.init()

class Square():

    margin = 2

    def __init__(self, left, top, state):
        self.left=left
        self.top=top
        self.state=state

    def getState(self):
        return self.state

    def getPos(self):
        return (self.left, self.top)

    def getColor(self):
        return BLACK if self.state == 1 else WHITE


def create_board():
    board = []

    for row in range(50):
        rowBoard = []
        for col in range(101):
            currSquare = Square(left=(MARGIN + SQUARE_WIDTH) * col + MARGIN,
                                top=(MARGIN + SQUARE_WIDTH) * row + MARGIN,
                                 state=0)
            if row == 0 and col == 50:
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

def main():
    screen = pygame.display.set_mode([1214, 602])
    done = False
    clock = pygame.time.Clock()

    board = create_board()
    ruleSet = getRuleSet(90)
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
                                SQUARE_WIDTH,
                                SQUARE_WIDTH])

        clock.tick(60)

        pygame.display.flip()

    print(len(board[0]), len(board))



if __name__ == '__main__':
    main()
