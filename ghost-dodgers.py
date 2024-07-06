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

#maze = [list(row.replace(" ", ".")) for row in maze]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 10
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recreating Pacman")

def update_cell(x: int, y: int):
    if maze[y][x] == '.':
        maze[y][x] = ' '
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLACK, rect)

def run_game():
    x, y = 1, 1
    running = True
    draw_maze()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                update_cell(x, y)
                x += 1
                pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)                
            pygame.display.flip()

def draw_maze():
    screen.fill(BLACK)
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#': 
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLUE, rect)
            else:
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)
    pygame.display.flip()

run_game()
pygame.quit()

