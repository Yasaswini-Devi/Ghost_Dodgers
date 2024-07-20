import pygame
import random
from static_maze import *
from constants import *
from theme import *

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = ''
    
    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)

    def set_direction(self, player_pos):
        path = a_star((self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE), player_pos, maze)

    def move(self):
        if self.direction == 'LEFT':
            self.rect.x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            self.rect.x += CELL_SIZE
        elif self.direction == 'UP':
            self.rect.y -= CELL_SIZE
        elif self.direction == 'DOWN':
            self.rect.y += CELL_SIZE

class Ghost1(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(0))
        
class Ghost2(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(1))

class Ghost3(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(2))

class Ghost4(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(3))
