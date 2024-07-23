import pygame

pygame.init()
pygame.mixer.init()

eat_sound = pygame.mixer.Sound('assets/sounds/eat.mp3')
game_over_sound = pygame.mixer.Sound('assets/sounds/game_over.mp3')
click_sound = pygame.mixer.Sound('assets/sounds/click.wav')

def play_eat_sound():
    eat_sound.play()

def play_game_over_sound():
    game_over_sound.play()

def play_background_music():
    pygame.mixer.music.load('assets/sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def play_click_sound():
    click_sound.play()
