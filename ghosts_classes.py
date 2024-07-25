import pygame
import random
from static_maze import *
from constants import *
from theme import *
from path_finder import a_star
from main_character import Pacman

'''class Ghost(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img, delay: int, scatter_target: (int, int)):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.timer = 0
        self.delay = delay
        self.mode = 'scatter'
        self.target = None
        self.scatter_target = scatter_target
        self.move_timer = 0
        self.move_delay = 400
        self.last_move_time = pygame.time.get_ticks()
        self.speed = CELL_SIZE // 8
    
    def update(self, screen, pacman_pos, valid_positions, blinky_pos=None):
        screen.blit(self.image, self.rect.topleft)
        current_time = pygame.time.get_ticks()

        if current_time - self.last_move_time >= self.move_delay:
           self.last_move_time = current_time
           self.set_target(pacman_pos, blinky_pos)
           self.set_direction(valid_positions)
           self.move()

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)

    def set_target(self, pacman_pos, valid_positions, blinky_pos=None):
        if self.mode == 'scatter': 
           # if (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE) == self.scatter_target:
               # self.target = random.choice([target for target in scatter_targets if target != self.scatter_target])
            self.target = self.scatter_target
        elif self.mode == 'chase':
             if isinstance(self, Ghost1):  
                self.target = pacman_pos
             elif isinstance(self, Ghost2):  
                  self.target = (pacman_pos[0] + 4, pacman_pos[1])  # Move in front of Pac-Man
             elif isinstance(self, Ghost3):  
                  if blinky_pos:
                  #= next((g for g in self.groups()[0] if isinstance(g, Ghost1)), pacman_pos)
                     self.target = (2 * pacman_pos[0] - blinky_pos[0], 2 * pacman_pos[1] - blinky_pos[1])
             elif isinstance(self, Ghost4): 
                  if abs(self.rect.x // CELL_SIZE - pacman_pos[0]) + abs(self.rect.y // CELL_SIZE - pacman_pos[1]) > 8:
                     self.target = pacman_pos
                  else:
                     self.target = self.scatter_target 
           # self.target = pacman_pos
        elif self.mode == 'frightened':
            self.target = random.choice(valid_positions)


    def set_direction(self, valid_positions):
        possible_directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        #current_pos = (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE)
        if self.direction:
           #target_x, target_y = self.target
           possible_directions.remove(opposite_directions[self.direction])

           def get_new_position(pos, direction):
               if direction == 'UP':
                  return (pos[0], pos[1] - 1)
               elif direction == 'DOWN':
                    return (pos[0], pos[1] + 1)
               elif direction == 'LEFT':
                    return (pos[0] - 1, pos[1])
               elif direction == 'RIGHT':
                    return (pos[0] + 1, pos[1])

               distances = []
               for direction in possible_directions:
                   new_pos = get_new_position(current_pos, direction)
                   if new_pos in valid_positions:
                      dist = abs(new_pos[0] - target_x) + abs(new_pos[1] - target_y)
                      distances.append((dist, direction))
            
               if distances:
                  distances.sort()
                  self.direction = distances[0][1]
     
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
                 self.direction = 'DOWN

    def move(self, valid_positions):
        current_pos = (self.rect.x // CELL_SIZE, self.rect.y // CELL_SIZE)
        if self.direction == 'LEFT':
           new_pos = (current_pos[0] - 1, current_pos[1])
           if new_pos in valid_positions:
              self.rect.x -= self.speed
        elif self.direction == 'RIGHT':
             new_pos = (current_pos[0] + 1, current_pos[1])
             if new_pos in valid_positions:
                self.rect.x += self.speed
        elif self.direction == 'UP':
             new_pos = (current_pos[0], current_pos[1] - 1)
             if new_pos in valid_positions:
                self.rect.y -= self.speed
        elif self.direction == 'DOWN':
             new_pos = (current_pos[0], current_pos[1] + 1)
             if new_pos in valid_positions:
                self.rect.y += self.speed

        if self.rect.x < 0:
           self.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif self.rect.x >= SCREEN_WIDTH:
             self.rect.x = 0

        if self.rect.y < 0:
           self.rect.y = SCREEN_HEIGHT - CELL_SIZE
        elif self.rect.y >= SCREEN_HEIGHT:
             self.rect.y = 0

        if self.direction == 'LEFT':
            self.rect.x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            self.rect.x += CELL_SIZE
        elif self.direction == 'UP':
            self.rect.y -= CELL_SIZE
        elif self.direction == 'DOWN':
            self.rect.y += CELL_SIZE

        if self.rect.x < 0:
           self.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif self.rect.x >= SCREEN_WIDTH:
             self.rect.x = 0

        if self.rect.y < 0:
           self.rect.y = SCREEN_HEIGHT - CELL_SIZE
        elif self.rect.y >= SCREEN_HEIGHT:
             self.rect.y = 0

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
        super().__init__(x, y, theme.get_ghost_image(3), 300, scatter_targets[3])'''

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, img, delay: int, scatter_target: (int, int)):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_pos = (x, y)
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.timer = 0
        self.delay = delay
        self.mode = 'scatter'
        self.target = None
        self.scatter_target = scatter_target
        self.move_timer = 0
        self.move_delay = 400
        self.last_move_time = pygame.time.get_ticks()
        self.speed = CELL_SIZE // 8
    
    def update(self, screen, pacman_pos, valid_positions, blinky_pos=None):
        screen.blit(self.image, self.rect.topleft)
        current_time = pygame.time.get_ticks()

        if current_time - self.last_move_time >= self.move_delay:
            self.last_move_time = current_time
            self.set_target(pacman_pos, blinky_pos)
            self.set_direction(valid_positions)
            self.move()

    def reset_pos(self):
        self.rect.topleft = (self.initial_pos[0] * CELL_SIZE, self.initial_pos[1] * CELL_SIZE)

    def set_target(self, pacman_pos, blinky_pos=None):
        if self.mode == 'scatter':
           self.target = self.scatter_target
        elif self.mode == 'chase':
             if isinstance(self, Ghost1):
                self.target = pacman_pos
             elif isinstance(self, Ghost2):
                self.target = (pacman_pos[0] + 4, pacman_pos[1])
             elif isinstance(self, Ghost3):
                  if blinky_pos:
                     self.target = (2 * pacman_pos[0] - blinky_pos[0], 2 * pacman_pos[1] - blinky_pos[1])
             elif isinstance(self, Ghost4):
                  if abs(self.rect.x // CELL_SIZE - pacman_pos[0]) + abs(self.rect.y // CELL_SIZE - pacman_pos[1]) > 8:
                    self.target = pacman_pos
                  else:
                    self.target = self.scatter_target
        elif self.mode == 'frightened':
             self.target = random.choice(valid_positions)

    def set_direction(self, valid_positions):
        possible_directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}

        if self.direction:
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

    def get_next_position(self, direction):
        x, y = self.rect.topleft
        if direction == 'UP':
            return (x // CELL_SIZE, (y - CELL_SIZE) // CELL_SIZE)
        elif direction == 'DOWN':
            return (x // CELL_SIZE, (y + CELL_SIZE) // CELL_SIZE)
        elif direction == 'LEFT':
            return ((x - CELL_SIZE) // CELL_SIZE, y // CELL_SIZE)
        elif direction == 'RIGHT':
            return ((x + CELL_SIZE) // CELL_SIZE, y // CELL_SIZE)

    def get_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def move(self):
        if self.direction == 'LEFT':
           self.rect.x -= CELL_SIZE
        elif self.direction == 'RIGHT':
             self.rect.x += CELL_SIZE
        elif self.direction == 'UP':
             self.rect.y -= CELL_SIZE
        elif self.direction == 'DOWN':
             self.rect.y += CELL_SIZE

        if self.rect.x < 0:
           self.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif self.rect.x >= SCREEN_WIDTH:
             self.rect.x = 0

        if self.rect.y < 0:
           self.rect.y = SCREEN_HEIGHT - CELL_SIZE
        elif self.rect.y >= SCREEN_HEIGHT:
             self.rect.y = 0

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



            
        
