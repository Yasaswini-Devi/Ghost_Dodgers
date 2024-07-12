import random

def initialize_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    return maze

def add_ghost_house(maze, x, y, width, height):
    for i in range(y, y + height):
        for j in range(x, x + width):
            maze[i][j] = 'G'

def carve_passages_from(cx, cy, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for direction in directions:
        nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '#':
            grid[cy + direction[1]][cx + direction[0]] = ' '
            grid[ny][nx] = ' '
            carve_passages_from(nx, ny, grid)

def create_maze_with_ghost_house(width, height, ghost_house_x, ghost_house_y, ghost_house_width, ghost_house_height):
    maze = initialize_maze(width, height)

    add_ghost_house(maze, ghost_house_x, ghost_house_y, ghost_house_width, ghost_house_height)

    start_x, start_y = 1, 1
    while (ghost_house_x <= start_x < ghost_house_x + ghost_house_width and 
           ghost_house_y <= start_y < ghost_house_y + ghost_house_height):
        start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)

    maze[start_y][start_x] = ' '
    carve_passages_from(start_x, start_y, maze)

    return maze
