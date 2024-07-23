import pygame
import random
from static_maze import *
from constants import *
from theme import *
from path_finder import a_star
from main_character import Pacman

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img, delay: int, scatter_target: (int, int)):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = ''
        self.timer = 0
        self.delay = delay
        self.mode = 'scatter'
        self.target = None
        self.scatter_target = scatter_target
    
    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)

    def set_target(self, pacman_pos: (int, int)):
        if self.mode == 'scatter': 
            self.target = self.scatter_target
        elif self.mode == 'chase':
            self.target = pacman_pos
        elif self.mode == 'frightened':
            self.target = (random.randint(1, NCOLS - 2), random.randint(1, NROWS - 2))


    def set_direction(self):
        path = a_star((self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE), self.target, MAZE)
        if path and len(path) > 1:
            next_pos = path[1]
            if next_pos[0] * CELL_SIZE < self.rect.x:
                self.direction = 'LEFT'
            elif next_pos[0] * CELL_SIZE > self.rect.x:
                self.direction = 'RIGHT'
            elif next_pos[1] * CELL_SIZE < self.rect.y:
                self.direction = 'UP'
            elif next_pos[1] * CELL_SIZE > self.rect.y:
                self.direction = 'DOWN'

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
        super().__init__(x, y, theme.get_ghost_image(0), 0, scatter_targets[0])
        
class Ghost2(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(1), 100, scatter_targets[1])

class Ghost3(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(2), 200, scatter_targets[2])

class Ghost4(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(3), 300, scatter_targets[3])
