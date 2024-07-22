import pygame
from constants import *
from play_sounds import *

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.title_font = pygame.font.Font(None, 56)
        self.themes = {
                "It's Halloween Time": "halloween",
                "Let's Hack": "lets_hack"
                }

    def show_main_menu(self):
        background = pygame.transform.scale(pygame.image.load("assets/main_menu.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill(BLACK)
        menu_options = ["Start Game", "Instructions", "Quit"]
        selected_option = 0

        while True:
            self.screen.blit(background, (0, 0))
            title_text = self.title_font.render("WELCOME TO TROUBLE ESCAPERS!", True, BLACK)
            title_rect = title_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            self.screen.blit(title_text, title_rect)

            for index, option in enumerate(menu_options):
                option_text = self.font.render(option, True, BLACK)
                option_rect = option_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + index * 50))

                box_rect = pygame.Rect(option_rect.left - 10, option_rect.top - 10, option_rect.width + 20, option_rect.height + 20)
                pygame.draw.rect(self.screen, RED, box_rect, 2)

                self.screen.blit(option_text, option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    play_click_sound()
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            return "start"
                        elif selected_option == 1:
                            self.show_instructions()
                        elif selected_option == 2:
                            pygame.quit()
                            exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    play_click_sound()
                    if event.button == 1:
                        x, y = event.pos
                        for i, option in enumerate(menu_options):
                            option_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + i * 60 - 20, 200, 40)
                            if option_rect.collidepoint(x, y):
                                if i == 0:
                                    return "start"
                                elif i == 1:
                                    self.show_instructions()
                                elif i == 2:
                                    pygame.quit()
                                    exit()

    def show_instructions(self):
        self.screen.fill(BLACK)
        instructions = [
            "1. Use arrow keys to move Pacman.",
            "2. Eat pellets to score points.",
            "3. Avoid ghosts or use power-ups to defeat them.",
            "4. You have three lives to win the game.",
            "5. Press Q to quit or R to restart during the game.",
            "6. Press Esc to go back to home page."
        ]
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, WHITE)
            self.screen.blit(text, (20, SCREEN_HEIGHT // 4 + i * 50))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    play_click_sound()
                    return

    def theme_selection_menu(self):
        background = pygame.transform.scale(pygame.image.load("assets/wallpaper.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        title_font = pygame.font.Font(None, 56)
        title_text = self.title_font.render("Select a Theme", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        theme_texts = []

        for i, (theme_name, theme_folder) in enumerate(self.themes.items()):
            text = self.font.render(theme_name, True, BLACK)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 40))
            theme_texts.append((text, rect, theme_folder))

        while True:
            self.screen.blit(background, (0, 0))
            self.screen.blit(title_text, title_rect)

            for text, rect, _ in theme_texts:
                self.screen.blit(text, rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    play_click_sound()
                    for text, rect, theme_folder in theme_texts:
                        if rect.collidepoint(event.pos):
                            play_click_sound()
                            return theme_folder

    def draw_text(text, font, color, surface, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)
          
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
