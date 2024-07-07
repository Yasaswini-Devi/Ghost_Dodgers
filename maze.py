class Cell:

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
