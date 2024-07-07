import pygame
from maze import Maze

nx, ny = 5, 5
ix, iy = 0, 0

maze_obj = Maze(nx, ny, ix, iy)
maze_obj.make_maze()
maze = str(maze_obj)
maze = [list(row) for row in maze.split('\n')]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 10
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recreating Pacman")

def draw_maze():
    screen.fill(BLACK)
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#': 
                draw_wall(x, y)
            else:
                draw_pellet(x, y)
    pygame.display.flip()

def draw_wall(x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, rect)

def draw_pellet(x: int, y: int):
    pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)

def update_cell(x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLACK, rect)

def move_player(x: int, y: int):
    pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def handle_keys(x: int, y: int, event):
    new_x, new_y = x, y

    if event.key == pygame.K_LEFT:
        new_x -= 1
    elif event.key == pygame.K_RIGHT:
        new_x += 1
    elif event.key == pygame.K_UP:
        new_y -= 1
    elif event.key == pygame.K_DOWN:
        new_y += 1

    if maze[new_y][new_x] != '#':
        return new_x, new_y
    return x, y

def run_game():
    x, y = 1, 1
    running = True
    draw_maze()
    move_player(x, y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                update_cell(x, y)
                x, y = handle_keys(x, y, event)
                move_player(x, y)
        pygame.display.flip()

run_game()
pygame.quit()
