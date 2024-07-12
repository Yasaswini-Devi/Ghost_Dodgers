import pygame
from maze import *
from constants import *
from ghost-dodgers import *

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
