import pygame
import random
from constants import *

ghost1 = pygame.transform.scale(pygame.image.load(f'assets/ghost1_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost2 = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost3 = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost4 = pygame.transform.scale(pygame.image.load(f'assets/ghost4_hallowen.png'), (CELL_SIZE, CELL_SIZE))


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
    
    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)

    def move(self):
        if self.direction == 'LEFT':
            self.rect.x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            self.rect.x += CELL_SIZE
        elif self.direction == 'UP':
            self.rect.y -= CELL_SIZE
        elif self.direction == 'DOWN':
            self.rect.y += CELL_SIZE

        if random.randint(0, 10) == 0:
            self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])


class Ghost1(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost1)
        
class Ghost2(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost2)

class Ghost3(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost3)

class Ghost4(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost4)
