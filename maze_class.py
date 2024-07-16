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
                    self.fruits.add(Pellet(x_index, y_index, CELL_SIZE // 4))
                    self.pellets += 1
                elif char == "B":
                    self.fruits.add(PowerUp(x_index, y_index, CELL_SIZE // 2, is_power_up=True))
                    self.pellets += 1
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
        self.display_stats()

    def display_life_lost_message(self):
        font = pygame.font.Font(None, 36)
        life_lost_text = font.render(f"You lost a life. Remaining lives: {self.lives}", True, WHITE)
        life_lost_rect = life_lost_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(life_lost_text, life_lost_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_stats(self):
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
        lives_rect = lives_text.get_rect(topright = (SCREEN_WIDTH - 5, 5))
        self.screen.blit(lives_text, lives_rect)

        score_text = font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(topleft = (5, 5))
        self.screen.blit(score_text, score_rect)

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
            self.pellets -= 1
            self.score += 10
            if self.pellets == 0:
                self.game_over(win = True)
        
        if pygame.sprite.spritecollideany(player, self.ghosts):
            self.lives -= 1
            if self.lives == 0:
                self.game_over(win = False)
            else:
                player.rect.topleft = (PACMAN_START_X * CELL_SIZE, PACMAN_START_Y * CELL_SIZE)
                self.display_life_lost_message()

        self.update()

    def game_over(self, win = False):
        font = pygame.font.Font(None, 35)
        text = "You Win!" if win else "Game Over!"
        text += f" Score: {self.score}"
        text_render = font.render(text, True, WHITE)
        text_rect = text_render.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        self.screen.blit(text_render, text_rect)

        text_restart = font.render("Press R to Restart", True, WHITE)
        text_restart_rect = text_restart.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        self.screen.blit(text_restart, text_restart_rect)

        text_quit = font.render("Press Q to Quit", True, WHITE)
        text_quit_rect = text_quit.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(text_quit, text_quit_rect)

        pygame.display.flip()

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
        self.generate_maze()
        self.pellets = 0
        self.score = 0
        self.lives = 3
