import pygame
from constants import *

img_1 = pygame.transform.scale(pygame.image.load(f'assets/pacman_halloween_theme.png'), (CELL_SIZE, CELL_SIZE))
img_2 = pygame.transform.scale(pygame.image.load(f'assets/pacman_hacking_theme.png'), (CELL_SIZE, CELL_SIZE))

class Pacman:
    def __init__(self, img):
        self.name = PACMAN
        self.is_alive = True
        self.img = img

    def die(self):
        self.is_alive = False

    def move_player(self, screen, x: int, y: int):
        screen.blit(self.img, (x * CELL_SIZE, y * CELL_SIZE))

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
