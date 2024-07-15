import pygame
from constants import *
from main_character import *

ghost1 = pygame.transform.scale(pygame.image.load(f'assets/ghost1_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost2 = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost3 = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost4 = pygame.transform.scale(pygame.image.load(f'assets/ghost4_hallowen.png'), (CELL_SIZE, CELL_SIZE))

class Ghost1(Pacman):
    def __init__(self, x, y, color):
        super().__init__(x, y, ghost1)

class Ghost2(Pacman):
    def __init__(self, x, y, color):
        super().__init__(x, y, ghost2)

class Ghost3(Pacman):
    def __init__(self, x, y, color):
        super().__init__(x, y, ghost3)

class Ghost4(Pacman):
    def __init__(self, x, y, color):
        super().__init__(x, y, ghost4)
