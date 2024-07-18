import pygame
from constants import *
from static_maze import *
from main_character import *
from ghosts_classes import *
from cells import *
from powerup import *
from pellets import *
from display import *

class Maze:
    def __init__(self, screen):
        self.screen = screen
        self.display = Display(screen)
        self.player = pygame.sprite.GroupSingle()
        self.ghosts = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.pellets = 0
        self.score = 0
        self.lives = 3
        self.generate_maze()

    def generate_maze(self):
        for y_index, col in enumerate(MAZE):
            for x_index, char in enumerate(col):
                if char == "1":
                    self.walls.add(Cell(x_index, y_index, CELL_SIZE, CELL_SIZE))
                elif char == " ":
                    self.fruits.add(Pellet(x_index, y_index, CELL_SIZE // 3))
                    self.pellets += 1
                elif char == "B":
                    self.fruits.add(PowerUp(x_index, y_index, CELL_SIZE, is_power_up = True))
                    self.pellets += 1
                elif char == "s":
                    self.ghosts.add(Ghost1(x_index, y_index))
                elif char == "p":
                    self.ghosts.add(Ghost2(x_index, y_index))
                elif char == "o":
                    self.ghosts.add(Ghost3(x_index, y_index))
                elif char == "r":
                    self.ghosts.add(Ghost4(x_index, y_index))
                elif char == "P":
                    self.player.add(Pacman(x_index, y_index, img_1))

    def update(self):
        self.walls.update(self.screen)
        self.fruits.update(self.screen)
        self.player.update(self.screen)
        self.ghosts.update(self.screen)
        self.display.show_life(self.lives)
        self.display.show_score(self.score)

    def move_player(self, direction):
        player = self.player.sprite
        original_position = player.rect.topleft
        player.move(direction)

        if player.rect.x < 0:
            player.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif player.rect.x >= SCREEN_WIDTH:
            player.rect.x = 0

        if pygame.sprite.spritecollide(player, self.walls, False):
            player.rect.topleft = original_position

        pellets_collided = pygame.sprite.spritecollide(player, self.fruits, True)
        if pellets_collided:
            for pellet in pellets_collided:
                self.pellets -= 1
                if isinstance(pellet, PowerUp):
                    self.score += 50
                else:
                    self.score += 10

            if self.pellets == 0:
                self.update()
                self.game_over(win = True)
        
        if pygame.sprite.spritecollideany(player, self.ghosts):
            self.lives -= 1
            if self.lives == 0:
                self.game_over(win = False)
            else:
                player.rect.topleft = (PACMAN_START_X * CELL_SIZE, PACMAN_START_Y * CELL_SIZE)
                self.display.show_life_lost_message(self.lives)

        self.update()

    def game_over(self, win = False):
        self.display.show_game_over(win, self.score)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        return

    def reset_game(self):
        self.player.empty()
        self.ghosts.empty()
        self.walls.empty()
        self.fruits.empty()
        self.pellets = 0
        self.score = 0
        self.lives = 3
        self.generate_maze()
