import pygame
from math import sqrt
from variables import *

pre_mouse = False


class Basket(pygame.sprite.Sprite):

    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), basket_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ball(pygame.sprite.Sprite):



    def __init__(self, image, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(pygame.image.load(image), ball_size)
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.bool_ind = False
        self.ind1 = False
        self.xy_start = self.rect.center
        self.res_x = 0
        self.res_y = 0
        self.mouse_ind = False
        self.jump_ind = False
        self.point = False
        self.screen = screen
        self.floor_count = 0

    def update(self):
        if not self.mouse_ind:
            if bool(pygame.mouse.get_pressed()[0]) and not self.jump_ind:
                position = pygame.mouse.get_pos()
                if not self.ind1:
                    self.xy_start = position
                    self.ind1 = True

                self.res_x = position[0] - self.xy_start[0]
                self.res_y = position[1] - self.xy_start[1]
                self.draw_punct(self.screen)
                self.bool_ind = True

            if not bool(pygame.mouse.get_pressed()[0]) and self.bool_ind and not self.jump_ind:
                self.jump(self.res_x, self.res_y)
                self.ind1 = False

            if self.jump_ind:
                self.fly()

            self.rect.x += self.speedx
            self.rect.y += self.speedy


    def jump(self, rx, ry):
        self.jump_ind = True
        self.speedx = -(rx / 7)
        self.speedy = -(ry / 7)

    def fly(self):
        self.speedy += (G * 0.2)

    def draw_punct(self, screen):
        speedx = -(self.res_x / 7)
        speedy = -(self.res_y / 7)
        x = self.rect.x + ball_size[0] / 2
        y = self.rect.y + ball_size[1] / 2
        while speedy < 0:
            x += speedx
            y += speedy
            pygame.draw.circle(screen, RED, (x, y), 3)
            speedy += G * 0.2


def reset(ball_path, screen):
    return Ball(ball_path, ball_start_pos[0], ball_start_pos[1], screen)