import pygame
from constants import *

class Theme:
    def __init__(self, theme_name):
        self.theme_name = theme_name
        self.load_assets()

    def load_assets(self):
        self.pacman_img = pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/pacman.png'), (CELL_SIZE, CELL_SIZE))
        self.ghost_images = [
            pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/ghost1.png'), (CELL_SIZE, CELL_SIZE)),
            pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/ghost2.png'), (CELL_SIZE, CELL_SIZE)),
            pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/ghost3.png'), (CELL_SIZE, CELL_SIZE)),
            pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/ghost4.png'), (CELL_SIZE, CELL_SIZE))
            ]
        self.powerup_image = pygame.transform.scale(pygame.image.load(f'assets/{self.theme_name}/powerup.png'), (CELL_SIZE, CELL_SIZE))

    def get_pacman_image(self):
        return self.pacman_img

    def get_ghost_image(self, ghost_index):
        return self.ghost_images[ghost_index]

    def get_powerup_image(self):
        return self.powerup_image
