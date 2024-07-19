import pygame
from constants import *

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_text(text, font, color, surface, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def show_main_menu(self):
        menu_options = ["Start Game", "Instructions", "Quit"]
  
    def show_life(self, lives):
        text = f"Lives: {lives}"
        lives_text = self.font.render(text, True, WHITE)
        lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH - 5, 5))
        self.screen.blit(lives_text, lives_rect)
        
    def show_score(self, score):
        text = f"Score: {score}"
        score_text = self.font.render(text, True, WHITE)
        score_rect = score_text.get_rect(topleft=(5, 5))
        self.screen.blit(score_text, score_rect)

    def show_life_lost_message(self, lives):
        text = f"You lost a life! Remaining lives: {lives}"
        text_render = self.font.render(text, True, WHITE)
        text_rect = text_render.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text_render, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)

    def show_game_over(self, win = False, score = 0):
        text = "You Win!" if win else "Game Over!"
        text += f" Score: {score}"
        text_render = self.font.render(text, True, WHITE)
        text_rect = text_render.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        self.screen.blit(text_render, text_rect)

        text_restart = self.font.render("Press R to Restart", True, WHITE)
        text_restart_rect = text_restart.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        self.screen.blit(text_restart, text_restart_rect)

        text_quit = self.font.render("Press Q to Quit", True, WHITE)
        text_quit_rect = text_quit.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(text_quit, text_quit_rect)

        pygame.display.flip()
