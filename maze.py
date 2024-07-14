import random
from constants import *

def initialize_maze(width: int, height: int) -> list[list[str]]:
    maze = [['#'] * width for _ in range(height)]
    return maze

def add_ghost_house(maze: list[list[str]], x: int, y: int, width: int, height: int):
    for row in range(y, y + height):
        for col in range(x, x + width):
            maze[row][col] = 'G'

def carve_passages_from(cx: int, cy: int, grid: list[list[str]]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for direction in directions:
        nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '#':
            grid[cy + direction[1]][cx + direction[0]] = ' '
            grid[ny][nx] = ' '
            carve_passages_from(nx, ny, grid)

def create_maze_with_ghost_house(width: int, height: int, ghost_house_x: int, ghost_house_y: int, ghost_house_width: int, ghost_house_height: int) -> list[list[str]]:
    maze = initialize_maze(width, height)

    add_ghost_house(maze, ghost_house_x, ghost_house_y, ghost_house_width, ghost_house_height)

    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '
    carve_passages_from(start_x, start_y, maze)
    x, y = ghost_house_x + ghost_house_width // 2, ghost_house_y - 1
    maze[x][y] = 'S'
    return maze
