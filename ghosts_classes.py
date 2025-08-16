import pygame
import random
from static_maze import *
from constants import *
from theme import *
from main_character import Pacman

GHOST_HOUSE_POSITIONS = {
    (8, 9), (9, 9), (10, 9), (9, 8)
}
GHOST_GATE_POSITION = (9, 7)
GHOST_EXIT_PATH = {
    (8, 9): 'RIGHT',
    (9, 9): 'UP',
    (10, 9): 'LEFT',
    (9, 8): 'UP' # Move out of the gate
}

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img, scatter_target: (int, int)):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.mode = 'scatter'
        self.target = None
        self.scatter_target = scatter_target
        self.delay = 400
        self.last_move_time = pygame.time.get_ticks()
        self.valid_positions = {}

    def update(self, screen, pacman_pos, valid_positions, pacman_dir=None, blinky_pos=None):
        screen.blit(self.image, self.rect.topleft)
        current_time = pygame.time.get_ticks()
        self.valid_positions = set(valid_positions)

        # Ghost makes a decision and moves only after its delay
        if current_time - self.last_move_time >= self.delay:
            self.last_move_time = current_time
            # Pass all required arguments to set_target
            self.set_target(pacman_pos, pacman_dir, blinky_pos)
            self.set_direction(valid_positions)
            self.move()

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.mode = 'scatter'
        self.last_move_time = pygame.time.get_ticks()

    def set_target(self, pacman_pos=None, pacman_dir=None, blinky_pos=None):
        current_pos = (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE)

        # Force ghosts inside the house to target the gate
        if current_pos in GHOST_HOUSE_POSITIONS:
            self.target = GHOST_GATE_POSITION
            # This is a temporary state, so we don't need a new mode
            return

        # Once out of the house, proceed with normal logic
        if self.mode == 'scatter':
            self.target = self.scatter_target
        elif self.mode == 'chase':
            # This method is overridden by subclasses
            pass
        elif self.mode == 'frightened':
            self.target = (random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1))
    
    def set_direction(self, valid_positions):
        current_pos = (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE)
        
        # New logic to handle exiting the ghost house
        if current_pos in GHOST_HOUSE_POSITIONS or current_pos == GHOST_GATE_POSITION:
            if current_pos in GHOST_EXIT_PATH:
                self.direction = GHOST_EXIT_PATH[current_pos]
                return # Exit the function, no need for other logic
        
        # Normal maze pathfinding logic for ghosts outside the house
        possible_directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        
        if self.direction in opposite_directions:
            possible_directions.remove(opposite_directions[self.direction])
        
        best_direction = None
        min_distance = float('inf')

        for direction in possible_directions:
            next_position = self.get_next_position(direction)
            if next_position in valid_positions:
                distance = self.get_distance(next_position, self.target)
                if distance < min_distance:
                    min_distance = distance
                    best_direction = direction

        if best_direction:
            self.direction = best_direction
        else:
            self.direction = opposite_directions.get(self.direction)

    def get_next_position(self, direction):
        x, y = self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE
        if direction == 'UP':
            return (x, y - 1)
        elif direction == 'DOWN':
            return (x, y + 1)
        elif direction == 'LEFT':
            return (x - 1, y)
        elif direction == 'RIGHT':
            return (x + 1, y)
        return (x, y)

    def get_distance(self, pos1, pos2):
        if pos2 is None:
            return float('inf')
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def move(self):
        next_pos = self.get_next_position(self.direction)
        self.rect.x = next_pos[0] * CELL_SIZE
        self.rect.y = next_pos[1] * CELL_SIZE

        # Handle tunnel wrapping
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif self.rect.x >= SCREEN_WIDTH:
            self.rect.x = 0

# -----------------------------
# Unique Ghost Behaviors
# -----------------------------

class Ghost1(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(0), scatter_targets[0])
        
    def set_target(self, pacman_pos, pacman_dir=None, blinky_pos=None):
        if self.mode == 'chase':
            self.target = pacman_pos
        else:
            super().set_target(pacman_pos, pacman_dir, blinky_pos)


class Ghost2(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(1), scatter_targets[1])

    def set_target(self, pacman_pos, pacman_dir=None, blinky_pos=None):
        if self.mode == 'chase' and pacman_dir:
            dx, dy = 0, 0
            if pacman_dir == 'UP':
                dy = -4
            elif pacman_dir == 'DOWN':
                dy = 4
            elif pacman_dir == 'LEFT':
                dx = -4
            elif pacman_dir == 'RIGHT':
                dx = 4
            self.target = (pacman_pos[0] + dx, pacman_pos[1] + dy)
        else:
            super().set_target(pacman_pos, pacman_dir, blinky_pos)


class Ghost3(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(2), scatter_targets[2])

    def set_target(self, pacman_pos, pacman_dir=None, blinky_pos=None):
        if self.mode == 'chase' and blinky_pos:
            self.target = (
                2 * pacman_pos[0] - blinky_pos[0],
                2 * pacman_pos[1] - blinky_pos[1]
            )
        else:
            super().set_target(pacman_pos, pacman_dir, blinky_pos)


class Ghost4(Ghost):
    def __init__(self, x, y, theme):
        super().__init__(x, y, theme.get_ghost_image(3), scatter_targets[3])        

    def set_target(self, pacman_pos, pacman_dir=None, blinky_pos=None):
        if self.mode == 'chase':
            dist = abs(self.rect.x // CELL_SIZE - pacman_pos[0]) + abs(self.rect.y // CELL_SIZE - pacman_pos[1])
            if dist > 8:
                self.target = pacman_pos
            else:
                self.target = self.scatter_target
        else:
            super().set_target(pacman_pos, pacman_dir, blinky_pos)