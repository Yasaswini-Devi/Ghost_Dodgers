import pygame
from constants import *

img_1 = pygame.transform.scale(pygame.image.load(f'assets/pacman_halloween_theme.jpeg'), (45, 45))
img_2 = pygame.transform.scale(pygame.image.load(f'assets/pacman_hacking_theme.jpeg'), (45, 45))

class Pacman:
    def __init__(self, img):
        self.name = PACMAN
        self.color = YELLOW
        self.is_alive = True
        self.img = img

    def die(self):
        self.is_alive = False

    def move_player(self, screen, x: int, y: int):
        screen.blit(self.img, (x * CELL_SIZE, y * CELL_SIZE))

def handle_keys(event, current_direction):
    if event.key == pygame.K_LEFT:
        return 'LEFT'
    elif event.key == pygame.K_RIGHT:
        return 'RIGHT'
    elif event.key == pygame.K_UP:
        return 'UP'
    elif event.key == pygame.K_DOWN:
        return 'DOWN'
    return current_direction

def move_in_direction(x, y, direction):
    if direction == 'LEFT':
        x -= 1
    elif direction == 'RIGHT':
        x += 1
    elif direction == 'UP':
        y -= 1
    elif direction == 'DOWN':
        y += 1
    return x, y
