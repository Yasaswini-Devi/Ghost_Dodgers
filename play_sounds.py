import pygame

pygame.init()
pygame.mixer.init()

eat_sound = pygame.mixer.Sound('assets/eat.mp4')
game_over_sound = pygame.mixer.Sound('assets/game_over.mp3')

def play_eat_sound():
    eat_sound.play()

def play_game_over_sound():
    game_over_sound.play()
