import pygame


class Line(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.len = pos[1][1] - pos[0][1]
        self.image = pygame.Surface((1, self.len))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0][0]
        self.rect.y = pos[0][1]
