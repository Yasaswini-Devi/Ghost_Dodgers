import pygame
from constants import *

img_1 = pygame.transform.scale(pygame.image.load(f'assets/pacman_halloween_theme.jpeg'), (45, 45))
img_2 = pygame.transform.scale(pygame.image.load(f'assets/pacman_hacking_them.jpeg'), (45, 45))

class Pacman:
    def __init__(self):
        self.name = PACMAN
        self.color = YELLOW
        self.is_alive = True

    def die(self):
        self.is_alive = False
