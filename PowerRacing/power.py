import pygame
import pygame.mask

pygame.init()

from load_sprites import *
from pygame.sprite import *
from settings import *

settings = Settings()

class Power(pygame.sprite.Sprite):
    def __init__(self,lane):
        super().__init__()
        self.image = power
        self.lane = lane
        self.rect = self.image.get_rect()
        self.rect.x = self.lane
        self.rect.y = settings.power_pos_y
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.x < 650:
            self.rect.y += settings.car_speed
        else:
            self.kill()

