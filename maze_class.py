import pygame
import sys
from constants import *
from static_maze import *
from main_character import *
from ghosts_classes import *
from cells import *
from powerup import *
from pellets import *
from display import *
from theme import *
from path_finder import *
from play_sounds import *

class Maze:
    def __init__(self, screen, theme):
        self.screen = screen
        self.theme = theme
        self.display = Display(screen)
        self.player = pygame.sprite.GroupSingle()
        self.ghosts = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.pellets = 0
        self.score = 0
        self.lives = 3
        self.generate_maze()
        self.grid = MAZE

    def generate_maze(self):
        for y_index, col in enumerate(MAZE):
            for x_index, char in enumerate(col):
                if char == "1":
                    self.walls.add(Cell(x_index, y_index, CELL_SIZE, CELL_SIZE))
                elif char == " ":
                    self.fruits.add(Pellet(x_index, y_index, CELL_SIZE // 3))
                    self.pellets += 1
                elif char == "B":
                    self.fruits.add(PowerUp(x_index, y_index, CELL_SIZE,self.theme, is_power_up=True))
                    self.pellets += 1
                elif char == "s":
                    self.ghosts.add(Ghost1(x_index, y_index, self.theme))
                elif char == "p":
                    self.ghosts.add(Ghost2(x_index, y_index, self.theme))
                elif char == "o":
                    self.ghosts.add(Ghost3(x_index, y_index, self.theme))
                elif char == "r":
                    self.ghosts.add(Ghost4(x_index, y_index, self.theme))
                elif char == "P":
                    self.player.add(Pacman(x_index, y_index, self.theme.get_pacman_image()))

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
        
        if player.invincible:
            if player.invincible_timer == 0:
                player.invincible = False
                for ghost in self.ghosts:
                    ghost.mode = "chase"
            else:
                player.invincible_timer -= 1

        if pygame.sprite.spritecollide(player, self.walls, False):
            player.rect.topleft = original_position

        pellets_collided = pygame.sprite.spritecollide(player, self.fruits, True)
        if pellets_collided:
            play_eat_sound()
            for pellet in pellets_collided:
                self.pellets -= 1
                if isinstance(pellet, PowerUp):
                    self.score += 50
                    player.activate_powerup(100)
                    for ghost in self.ghosts:
                        ghost.mode = "frightened"
                else:
                    self.score += 10

            if self.pellets == 0:
                self.update()
                self.game_over(win=True)
        
        if pygame.sprite.spritecollideany(player, self.ghosts):
            if player.invincible:
                for ghost in pygame.sprite.spritecollide(player, self.ghosts, False):
                    ghost.reset_pos()
            else:
                self.lives -= 1
                if self.lives == 0:
                    self.game_over(win=False)
                else:
                    for ghost in self.ghosts:
                        ghost.reset_pos()
                    player.reset_pos()
                    self.display.show_life_lost_message(self.lives)

        self.update()

    def game_over(self, win=False):
        play_game_over_sound()
        self.display.show_game_over(win, self.score)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def reset_game(self):
        self.player.empty()
        self.ghosts.empty()
        self.walls.empty()
        self.fruits.empty()
        self.pellets = 0
        self.score = 0
        self.lives = 3
        self.generate_maze()

    def move_ghost(self, ghost):
        target = {'chase': (self.player.sprite.rect.x // CELL_SIZE, self.player.sprite.rect.y // CELL_SIZE), 'frightened': ghost.initial_pos}
        original_position = ghost.rect.topleft
        ghost.set_direction(target[ghost.mode])
        ghost.move()

        for other_ghost in self.ghosts:
            if other_ghost != ghost and pygame.sprite.collide_rect(ghost, other_ghost):
                ghost.rect.topleft = original_position
                ghost.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])

        if ghost.rect.x < 0:
            ghost.rect.x = SCREEN_WIDTH - CELL_SIZE
        elif ghost.rect.x >= SCREEN_WIDTH:
            ghost.rect.x = 0
