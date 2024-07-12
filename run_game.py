import pygame
from maze import *
from constants import *
from drawing import *
from main_character import *
#from ghosts import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Trouble Escapers")
    
    x, y = PACMAN_START_X, PACMAN_START_Y
    pacman = Pacman(img_1)
    current_direction = None
    running = True
    draw_maze(screen, maze)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                current_direction = handle_keys(event, current_direction)

        if current_direction:
            new_x, new_y = move_in_direction(x, y, current_direction)
            if not check_collisions(new_x, new_y):
                update_cell(screen, x, y)
                x, y = new_x, new_y
                pacman.move_player(screen, x, y)
        
        pygame.display.flip()
        pygame.time.delay(200)

    pygame.quit()

run_game()
