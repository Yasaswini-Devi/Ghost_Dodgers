import pygame

maze = [
    "#########################################",
    "#                                       #",
    "# ########## ######### ################ #",
    "# #        # #       #              # # #",
    "# #  ####### # ##### ####### ###### # # #",
    "# #  #       #     #       # #      # # #",
    "# #  # ############### ##### # ###### # #",
    "# #  #                 #     # #      # #",
    "# #  ######## ########## ##### # ###### #",
    "# #                            #        #",
    "#########################################"
]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 10

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recreating Pacman")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = BLACK if cell == '#' else WHITE
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()

pygame.quit()
