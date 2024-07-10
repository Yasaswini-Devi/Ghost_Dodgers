import random

class Cell:
    
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        return all(self.walls.values())

    def knock_down_wall(self, other, wall: str):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class Maze:

    def __init__(self, nx: int, ny: int, ix: int, iy: int):
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]
        self.ghost_house_area = ((nx - 1, ny), (nx + 1, ny))

    def create_top_border(self) -> str:
        return '#' * (self.nx * 2 + 1)

    def create_east_wall_row(self, y: int) -> str:
        maze_row = ['#']
        for x in range(self.nx):
            if self.maze_map[x][y].walls['E']:
                maze_row.append(' #')
            else:
                maze_row.append('  ')
        return ''.join(maze_row)

    def create_south_wall_row(self, y: int) -> str:
        maze_row = ['#']
        for x in range(self.nx):
            if self.maze_map[x][y].walls['S']:
                maze_row.append('##')
            else:
                maze_row.append(' #')
        return ''.join(maze_row)

    def __str__(self):
        maze_rows = [self.create_top_border()]
        for y in range(self.ny):
            maze_rows.append(self.create_east_wall_row(y))
            maze_rows.append(self.create_south_wall_row(y))
        return '\n'.join(maze_rows)

    def cell_at(self, x, y):
        return self.maze_map[x][y]

    def find_valid_neighbours(self, cell) -> list:
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]

        neighbours = []

        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        visited = 1

        while visited < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                current_cell = cell_stack.pop()
            else:
                direction, next_cell = random.choice(neighbours)
                current_cell.knock_down_wall(next_cell, direction)
                cell_stack.append(current_cell)
                current_cell = next_cell
                visited += 1

    def is_in_ghost_house(self, x, y):
        (x1, y1), (x2, y2) = self.ghost_house_area
        return x1 <= x <= x2 and y1 <= y <= y2
