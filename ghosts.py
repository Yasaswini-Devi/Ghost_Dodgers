import pygame
from constants import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

>>>>>>> fc2c090f5fd7b9c40af707b47ee20b921e28821f
ghost1_img = pygame.transform.scale(pygame.image.load(f'assets/ghost1_hallowen.png'), (45, 45))
ghost2_img = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hallowen.png'), (45, 45))
ghost3_img = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hallowen.png'), (45, 45))
ghost4_img = pygame.transform.scale(pygame.image.load(f'assets/ghost4_hallowen.png'), (45, 45))

spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost2_hackers.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost3_hacker.png'), (45, 45))

ghost1_x = 56
ghost1_y = 58
ghost1_direction = 0
ghost2_x = 440
ghost2_y = 388
ghost2_direction = 2
ghost3_x = 440
ghost3_y = 438
ghost3_direction = 2
ghost4_x = 440
ghost4_y = 438
ghost4_direction = 2

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
    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id ):
       self.x_pos = x_coord
       self.y_pos = y_coord
       self.center_x = self.x_pos + 22
       self.center_y = self.y_pos + 22
       self.target = target
       self.speed = speed
       self.img = img
       self.in_box = box
       self.id = id
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
