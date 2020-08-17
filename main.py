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

# def toBinaryArray(num):
#     return [int(x) for x in f'{num:08b}']

def getRuleSet():

    ruleSet = {
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 0,
    (0, 0, 1): 1,
    (0, 0, 0): 0
    }

    return ruleSet

def main():
    screen = pygame.display.set_mode([1214, 602])
    done = False
    clock = pygame.time.Clock()

    board = create_board()
    print(getRuleSet())
    exit()

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
