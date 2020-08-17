BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Square():

    margin = 2
    width = 10

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
