class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = ((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE)

    def update(self, screen):
        screen.blit(self.image, self.rect.center)
