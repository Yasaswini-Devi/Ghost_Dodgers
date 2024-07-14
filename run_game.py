import pygame
from maze import *
from constants import *
from drawing import *
from main_character import *
from ghosts import *

def toggle_fullscreen(full_screen) -> bool:
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
    ghosts = [
    Ghost(ghost1_x, ghost1_y, target=None, speed=2, img=ghost1_img, direct=0, dead=False, box=True, id=0, maze=maze),
    Ghost(ghost2_x, ghost2_y, target=None, speed=2, img=ghost2_img, direct=0, dead=False, box=True, id=1, maze=maze),
    Ghost(ghost3_x, ghost3_y, target=None, speed=2, img=ghost3_img, direct=0, dead=False, box=True, id=2, maze=maze),
    Ghost(ghost4_x, ghost4_y, target=None, speed=2, img=ghost4_img, direct=0, dead=False, box=True, id=3, maze=maze)
]
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
                    screen_content = screen.copy()
                    full_screen = toggle_fullscreen(full_screen)
                    screen.blit(screen_content, (0, 0))
                    pygame.display.flip()
                else:
                    current_direction = handle_keys(event, current_direction)

        if current_direction:
            new_x, new_y = move_in_direction(x, y, current_direction)
            if not check_collisions(maze, new_x, new_y):
                update_cell(screen, x, y)
                x, y = new_x, new_y
                pacman.move_player(screen, x, y)
            else:
                current_direction = None

        for ghost in ghosts:
            ghost.draw()

        pygame.display.flip()
        pygame.time.delay(200)

    pygame.quit()

run_game()
