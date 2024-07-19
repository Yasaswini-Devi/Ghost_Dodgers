import pygame
from constants import *
from maze_class import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Trouble Escapers')

    clock = pygame.time.Clock()
    theme_name = "It's Halloween Time"
    maze = Maze(screen, theme_name)

    running = True
    current_direction = None
    move_timer = 0  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_direction = handle_keys(event)
                if new_direction:
                    current_direction = new_direction

        move_timer += 1
        if move_timer >= 10:
            maze.move_player(current_direction)
            for ghost in maze.ghosts:
                maze.move_ghost(ghost)
            move_timer = 0

        screen.fill(BLUE)
        maze.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
