import pygame
from constants import *
from maze import *

screen = screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
width, height = 21, 21

ghost1_img = pygame.transform.scale(pygame.image.load(f'assets/ghost1_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost2_img = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost3_img = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hallowen.png'), (CELL_SIZE, CELL_SIZE))
ghost4_img = pygame.transform.scale(pygame.image.load(f'assets/ghost4_hallowen.png'), (CELL_SIZE, CELL_SIZE))

spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hackers.png'), (CELL_SIZE, CELL_SIZE))
dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hacker.png'), (CELL_SIZE, CELL_SIZE))

eaten_ghost = [False, False, False, False]
ghost1_dead = False
ghost2_dead = False
ghost3_dead = False
ghost4_dead = False
ghost1_box = False
ghost2_box = False
ghost3_box = False
ghost4_box = False
powerup = False

ghost_speed = 2

class Ghost:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id, maze ):
       self.x_pos = x_coord
       self.y_pos = y_coord
       self.center_x = self.x_pos + 22
       self.center_y = self.y_pos + 22
       self.target = target
       self.speed = speed
       self.img = img
       self.direction = direct
       self.dead = dead
       self.in_box = box
       self.id = id
       self.maze = maze
       self.turns, self.in_box = self.check_collisions()
       self.rect = self.draw()

    def draw(self):
        if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
            screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not eaten_ghost[self.id]:
            screen.blit(spooked_img, (self.x_pos, self.y_pos))
        else:
            screen.blit(dead_img, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect
    
    def check_collisions(self):
        num1 = len(self.maze)
        num2 = len(self.maze[0])
        num3 = 15
        self.turns = [False, False, False, False]
        if 0 < self.center_x // 30 < num2 - 1:
            if self.maze[(self.center_y - num3) // 30][self.center_x // 30] == 0:
                self.turns[2] = True
            if self.maze[self.center_y // 30][(self.center_x - num3) // 30] == 0:
                self.turns[1] = True
            if self.maze[self.center_y // 30][(self.center_x + num3) // 30] == 0:
                self.turns[0] = True
            if self.maze[(self.center_y + num3) // 30][self.center_x // 30] == 0:
                self.turns[3] = True

        if self.direction in [2, 3]:
            if 12 <= self.center_x % 30 <= 18:
                if self.maze[(self.center_y + num3) // 30][self.center_x // 30] == 0:
                    self.turns[3] = True
                if self.maze[(self.center_y - num3) // 30][self.center_x // 30] == 0:
                    self.turns[2] = True
            if 12 <= self.center_y % 30 <= 18:
                if self.maze[self.center_y // 30][(self.center_x - num2) // 30] == 0:
                    self.turns[1] = True
                if self.maze[self.center_y // 30][(self.center_x + num2) // 30] == 0:
                    self.turns[0] = True

        if self.direction in [0, 1]:
            if 12 <= self.center_x % 30 <= 18:
                if self.maze[(self.center_y + num3) // 30][self.center_x // 30] == 0:
                    self.turns[3] = True
                if self.maze[(self.center_y - num3) // 30][self.center_x // 30] == 0:
                    self.turns[2] = True
            if 12 <= self.center_y % 30 <= 18:
                if self.maze[self.center_y // 30][(self.center_x - num3) // 30] == 0:
                    self.turns[1] = True
                if self.maze[self.center_y // 30][(self.center_x + num3) // 30] == 0:
                    self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
            self.in_box = True
        else:
            self.in_box = False
        return self.turns, self.in_box
    
ghost1_x = (width // 2) * CELL_SIZE
ghost1_y = (height // 2) * CELL_SIZE
ghost2_x = (width // 2) * CELL_SIZE + CELL_SIZE
ghost2_y = (height // 2) * CELL_SIZE
ghost3_x = (width // 2) * CELL_SIZE
ghost3_y = (height // 2) * CELL_SIZE + CELL_SIZE
ghost4_x = (width // 2) * CELL_SIZE + CELL_SIZE
ghost4_y = (height // 2) * CELL_SIZE + CELL_SIZE

ghosts = [
    Ghost(ghost1_x, ghost1_y, target=None, speed=2, img=ghost1_img, direct=0, dead=False, box=True, id=0, maze=maze),
    Ghost(ghost2_x, ghost2_y, target=None, speed=2, img=ghost2_img, direct=0, dead=False, box=True, id=1, maze=maze),
    Ghost(ghost3_x, ghost3_y, target=None, speed=2, img=ghost3_img, direct=0, dead=False, box=True, id=2, maze=maze),
    Ghost(ghost4_x, ghost4_y, target=None, speed=2, img=ghost4_img, direct=0, dead=False, box=True, id=3, maze=maze)
] 

