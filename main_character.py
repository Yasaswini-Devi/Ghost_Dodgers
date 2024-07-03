import pygame
PACMAN = "Pacman"
YELLOW = (255, 255, 0)

class Pacman:
    def __init__(self):
        self.name = PACMAN
        self.color = YELLOW
        self.is_alive = True

    def die(self):
        self.is_alive = False
