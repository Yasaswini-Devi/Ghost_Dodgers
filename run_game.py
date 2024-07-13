import pygame
from maze import *
from constants import *
from drawing import *
from main_character import *
from ghosts import *

def toggle_fullscreen(full_screen):
    if full_screen:
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    else:
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    return not full_screen

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Trouble Escapers")
    maze = create_maze_with_ghost_house(width, height, ghost_house_x, ghost_house_y, ghost_house_width, ghost_house_height)
    
    x, y = PACMAN_START_X, PACMAN_START_Y
    pacman = Pacman(img_1)
    current_direction = None
    running = True
    full_screen = False
    draw_maze(screen, maze)
    pacman.move_player(screen, x, y)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    full_screen = toggle_fullscreen(full_screen)
                else:
                    current_direction = handle_keys(event, current_direction)

        if current_direction:
            new_x, new_y = move_in_direction(x, y, current_direction)
            if not check_collisions(new_x, new_y):
                update_cell(screen, x, y)
                x, y = new_x, new_y
                pacman.move_player(screen, x, y)

        for ghost in ghosts:
            ghost.draw()

        pygame.display.flip()
        pygame.time.delay(200)

    pygame.quit()

run_game()
