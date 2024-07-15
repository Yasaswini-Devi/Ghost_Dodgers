import pygame
from constants import *

class Cell(pygame.sprite.Sprite):
	def __init__(self, row, col, length, width):
		super().__init__()
		self.width = length
		self.height = width
		self.id = (row, col)
		self.abs_x = row * self.width
		self.abs_y = col * self.height
		self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

	def update(self, screen):
		pygame.draw.rect(screen, BLACK, self.rect)
