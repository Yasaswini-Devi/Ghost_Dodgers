import pygame
from constants import *
from pellets import *

class PowerUp(Pellet):
    def __init__(self, x, y, size, is_power_up=False):
        super().__init__(x, y, size)
        self.is_power_up = is_power_up
        self.image.fill(RED)
