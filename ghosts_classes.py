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

    def set_target(self, pacman_pos: (int, int), valid_positions: list[int]):
        if self.mode == 'scatter': 
           # if (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE) == self.scatter_target:
               # self.target = random.choice([target for target in scatter_targets if target != self.scatter_target])
            self.target = self.scatter_target
        elif self.mode == 'chase':
            self.target = pacman_pos
        elif self.mode == 'frightened':
            self.target = random.choice(valid_positions)


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



'''class Ghost:
    def __init__(self, x, y, color, maze):
        self.x = x
        self.y = y
        self.color = color
        self.maze = maze
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self):
        # Basic movement logic
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1
        
        # Ensure the ghost stays within the maze boundaries
        if self.maze[self.y][self.x] == 1:  # Assuming 1 represents a wall
            self.change_direction()

    def change_direction(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Ghost1(Ghost):  # Red ghost
    def move(self, pacman):
        # Target Pac-Man's current position
        if pacman.x > self.x:
            self.x += 1
        elif pacman.x < self.x:
            self.x -= 1
        elif pacman.y > self.y:
            self.y += 1
        elif pacman.y < self.y:
            self.y -= 1

class Ghost2(Ghost):  # Pink ghost
    def move(self, pacman):
        # Target four tiles ahead of Pac-Man
        if pacman.direction == 'up':
            target_x, target_y = pacman.x, pacman.y - 4
        elif pacman.direction == 'down':
            target_x, target_y = pacman.x, pacman.y + 4
        elif pacman.direction == 'left':
            target_x, target_y = pacman.x - 4, pacman.y
        elif pacman.direction == 'right':
            target_x, target_y = pacman.x + 4, pacman.y

        self.chase_target(target_x, target_y)

    def chase_target(self, target_x, target_y):
        if target_x > self.x:
            self.x += 1
        elif target_x < self.x:
            self.x -= 1
        elif target_y > self.y:
            self.y += 1
        elif target_y < self.y:
            self.y -= 1

class Ghost3(Ghost):  # Blue ghost
    def move(self, pacman, Ghost1):
        # Target a tile in relation to both Pac-Man and Blinky
        vector_x = pacman.x - Ghost1.x
        vector_y = pacman.y - Ghost1.y
        target_x = pacman.x + vector_x
        target_y = pacman.y + vector_y

        self.chase_target(target_x, target_y)

class Ghost4(Ghost):  # Orange ghost
    def move(self, pacman):
        distance = ((pacman.x - self.x) ** 2 + (pacman.y - self.y) ** 2) ** 0.5
        if distance > 8:
            self.chase_target(pacman.x, pacman.y)
        else:
            # Move randomly
            self.change_direction()
            super().move()'''
        
