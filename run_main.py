import pygame
from constants import *
from static_maze import *
from main_character import *
from ghosts_classes import *
from cells import *
from powerup import *
from pellets import *
from maze_class import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Trouble Escapers')

    clock = pygame.time.Clock()
    maze = Maze(screen)

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
                ghost.move()
            move_timer = 0

        screen.fill(BLUE)
        maze.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
