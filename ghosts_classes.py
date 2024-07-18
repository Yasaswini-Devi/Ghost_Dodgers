import pygame
import random
from constants import *
from main_character import *

ghost1 = pygame.transform.scale(pygame.image.load(f'assets/ghost1_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost2 = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost3 = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost4 = pygame.transform.scale(pygame.image.load(f'assets/ghost4_hallowen.png'), (CELL_SIZE, CELL_SIZE))


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
    
    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)

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
        #self.directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
'''
    def move(self, maze):
        direction = self.choose_direction(maze)
        original_position = self.rect.topleft
        super().move(direction)

        if pygame.sprite.spritecollide(self, maze.walls, False):
            self.rect.topleft = original_position

    def choose_direction(self, maze):
        # Implement logic to choose direction based on maze and player position
        # Example logic:
        # Randomly choose a direction initially
        direction = random.choice(self.directions)

        # Check if moving in that direction would collide with walls
        next_position = self.rect.move(CELL_SIZE, CELL_SIZE).topleft
        if direction == 'LEFT' and next_position[0] < 0:
            direction = 'RIGHT'
        elif direction == 'RIGHT' and next_position[0] >= SCREEN_WIDTH:
            direction = 'LEFT'
        elif direction == 'UP' and next_position[1] < 0:
            direction = 'DOWN'
        elif direction == 'DOWN' and next_position[1] >= SCREEN_HEIGHT:
            direction = 'UP'

        return direction
'''
class Ghost2(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost2)

class Ghost3(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost3)

class Ghost4(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, ghost4)
