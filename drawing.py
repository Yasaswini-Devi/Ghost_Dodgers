import pygame
from maze import *
from constants import *

maze = create_maze_with_ghost_house(width, height, ghost_house_x, ghost_house_y, ghost_house_width, ghost_house_height)

def draw_maze(screen, maze):
    screen.fill(BLACK)
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'G' or cell == 'S':
                draw_ghost_house(screen, x, y)
            elif cell == '#': 
                draw_wall(screen, x, y)
            else:
                draw_pellet(screen, x, y)
    pygame.display.flip()

def draw_wall(screen, x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, rect)

def draw_pellet(screen, x: int, y: int):
    pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)

def draw_ghost_house(screen, x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (128, 0, 128), rect)

def update_cell(screen, x: int, y: int):
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLACK, rect)

def check_collisions(x: int, y: int) -> bool:
    return maze[y][x] == '#' or maze[y][x] == 'G'
