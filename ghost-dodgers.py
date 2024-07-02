import pygame

pygame.init()

SIZE= (700, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Recreating Pacman")

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
