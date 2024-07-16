import pygame
from constants import *

img_1 = pygame.transform.scale(pygame.image.load(f'assets/pacman_halloween_theme.png'), (CELL_SIZE, CELL_SIZE))
img_2 = pygame.transform.scale(pygame.image.load(f'assets/pacman_hacking_theme.png'), (CELL_SIZE, CELL_SIZE))

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.is_alive = True
        self.direction = None

    def die(self):
        self.is_alive = False

    def update(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self, direction):
        if direction == 'LEFT':
            self.rect.x -= CELL_SIZE
        elif direction == 'RIGHT':
      	    self.rect.x += CELL_SIZE
        elif direction == 'UP':
       	    self.rect.y -= CELL_SIZE
        elif direction == 'DOWN':
       		self.rect.y += CELL_SIZE

def handle_keys(event):
    if event.key == pygame.K_LEFT:
        return 'LEFT'
    elif event.key == pygame.K_RIGHT:
        return 'RIGHT'
    elif event.key == pygame.K_UP:
        return 'UP'
    elif event.key == pygame.K_DOWN:
        return 'DOWN'
    return None
