import pygame
from constants import *
from static_maze import *
from main_character import *
from ghosts_classes import *
from cells import *
from powerup import *
from pellets import *

class Maze:
    def __init__(self, screen):
        self.screen = screen
        self.player = pygame.sprite.GroupSingle()
        self.ghosts = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.generate_maze()

    def generate_maze(self):
        for y_index, col in enumerate(MAZE):
            for x_index, char in enumerate(col):
                if char == "1":
                    self.walls.add(Cell(x_index, y_index, CELL_SIZE, CELL_SIZE))
                elif char == " ":
                    self.fruits.add(Pellet(x_index, y_index, CELL_SIZE // 4))
                elif char == "B":
                    self.fruits.add(PowerUp(x_index, y_index, CELL_SIZE // 2, is_power_up=True))
                elif char == "s":
                    self.ghosts.add(Ghost1(x_index, y_index, "black"))
                elif char == "p":
                    self.ghosts.add(Ghost2(x_index, y_index, "white"))
                elif char == "o":
                    self.ghosts.add(Ghost3(x_index, y_index, "red"))
                elif char == "r":
                    self.ghosts.add(Ghost4(x_index, y_index, "green"))
                elif char == "P":
                    self.player.add(Pacman(x_index, y_index, img_1))

    def update(self):
        self.walls.update(self.screen)
        self.fruits.update(self.screen)
        self.player.update(self.screen)
        self.ghosts.update(self.screen)

    def move_player(self, direction):
        player = self.player.sprite
        original_position = player.rect.topleft
        player.move(direction)

        if pygame.sprite.spritecollide(player, self.walls, False):
            player.rect.topleft = original_position

        pellets_collided = pygame.sprite.spritecollide(player, self.fruits, True)

        if player.rect.x < 0:
            player.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif player.rect.x >= SCREEN_WIDTH:
            player.rect.x = 0
