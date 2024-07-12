import pygame
from maze import Maze
from constants import *

PACMAN_START_X = 1
PACMAN_START_Y = 1

maze_obj = Maze(nx, ny, ix, iy)
maze_obj.make_maze()
maze = str(maze_obj)
maze = [list(row) for row in maze.split('\n')]

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recreating Pacman")

def draw_maze():
    screen.fill(BLACK)
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if maze_obj.is_in_ghost_house(x, y):
                draw_ghost_house(x, y)
            elif cell == '#': 
                draw_wall(x, y)
            else:
                draw_pellet(x, y)
    pygame.display.flip()

def draw_wall(x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, rect)

def draw_pellet(x: int, y: int):
    pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)

def draw_ghost_house(x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (128, 0, 128), rect)

def update_cell(x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLACK, rect)

def move_player(x: int, y: int):
    pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def check_collisions(x: int, y: int) -> bool:
    return maze[y][x] == '#' or maze_obj.is_in_ghost_house(x, y)

def handle_keys(event, current_direction):
    if event.key == pygame.K_LEFT:
        return 'LEFT'
    elif event.key == pygame.K_RIGHT:
        return 'RIGHT'
    elif event.key == pygame.K_UP:
        return 'UP'
    elif event.key == pygame.K_DOWN:
        return 'DOWN'
    return current_direction

def move_in_direction(x, y, direction):
    if direction == 'LEFT':
        x -= 1
    elif direction == 'RIGHT':
        x += 1
    elif direction == 'UP':
        y -= 1
    elif direction == 'DOWN':
        y += 1
    return x, y

def run_game():
    x, y = PACMAN_START_X, PACMAN_START_Y
    current_direction = None
    running = True
    draw_maze()
    move_player(x, y)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                current_direction = handle_keys(event, current_direction)

        if current_direction:
            new_x, new_y = move_in_direction(x, y, current_direction)
            if not check_collisions(new_x, new_y):
                update_cell(x, y)
                x, y = new_x, new_y
                move_player(x, y)

        pygame.display.flip()
        pygame.time.delay(200) 

run_game()
pygame.quit()
