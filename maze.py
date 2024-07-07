class Cell:

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

class Maze:

    def __init__(self, rows: int, colums: int, ix: int, iy: int):
        self.rows, self.colums = rows, columns
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(columns)] for x in range(rows)]
