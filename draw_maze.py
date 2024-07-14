import pygame

class Cell(pygame.sprite.Sprite):
	def __init__(self, row, col, length, width):
		super().__init__()
		self.width = length
		self.height = width
		self.id = (row, col)
		self.abs_x = row * self.width
		self.abs_y = col * self.height

		self.rect = pygame.Rect(self.abs_x,self.abs_y,self.width,self.height)

	def update(self, screen):
		pygame.draw.rect(screen, pygame.Color.b, self.rect)

from constants import *
from static_maze import *
from main_character import *

class Maze:
	def __init__(self, screen):
		self.screen = screen
		#self.player = 
		#self.ghosts = 
		#self.walls =
		#self.berries =
		self.generate_maze()

	def generate_maze(self):
		for y_index, col in enumerate(MAZE):
			for x_index, char in enumerate(col):
				if char == "1":	# cell being a part of wall
					self.walls.add(Cell(x_index, y_index, CHAR_SIZE, CHAR_SIZE))
				elif char == " ":	 # cell being filled with pellets
					#self.berries.add(pellets(x_index, y_index, CHAR_SIZE // 4))
				elif char == "B":	# cell being filled with power-ups
					#self.berries.add(power_ups(x_index, y_index, CHAR_SIZE // 2, is_power_up=True))
				elif char == "s": # s, p, o and r are for ghosts' starting points
					#self.ghosts.add(Ghost1(x_index, y_index, "skyblue"))
				elif char == "p": 
					#self.ghosts.add(Ghost2(x_index, y_index, "pink"))
				elif char == "o":
					#self.ghosts.add(Ghost3(x_index, y_index, "orange"))
				elif char == "r":
					#self.ghosts.add(Ghost4(x_index, y_index, "red"))
				elif char == "P":	# cell being pacman's starting point
					self.player.add(pacman(x_index, y_index))
