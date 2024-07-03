import pygame
from constants import *

class Pacman:
    def __init__(self):
        self.name = PACMAN
        self.color = YELLOW
        self.is_alive = True

    def die(self):
        self.is_alive = False
