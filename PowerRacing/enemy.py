import pygame 
import pygame.mask

pygame.init()

from load_sprites import *
from pygame.sprite import *
from settings import *

settings = Settings()
class enemy_car(pygame.sprite.Sprite):
    def __init__(self, bad,lane):
        super().__init__()
        self.bad = bad
        self.lane = lane
        self.enemy_speed = 10
        if self.bad == 1:
            self.image = enemy_modern_blue
        elif self.bad == 2:
            self.image = enemy_super_cyan
        elif self.bad == 3:
            self.image = enemy_kar_pink
        elif self.bad == 4:
            self.image = enemy_modern_green
        else:
            self.image = enemy_modern_pink

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (settings.car_width, settings.car_height))
        self.rect.x = self.lane
        self.rect.y = settings.enemy_pos_y

        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.x < 650:
            self.rect.y += settings.car_speed
        else:
            self.kill()

    def colision_move(self, direction):
        if direction == 1:
            self.rect.x += self.enemy_speed
        elif direction == 2:
            self.rect.x -= self.enemy_speed
        elif direction == 3:
            self.rect.x += self.enemy_speed
        elif direction == 4:
            self.rect.x -= self.enemy_speed


class Hueco(pygame.sprite.Sprite):
    def __init__(self,lane):
        super().__init__()
        self.image = hueco
        self.lane = lane
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (59, 47))
        self.rect.x = self.lane
        self.rect.y = settings.enemy_pos_y

        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.x < 650:
            self.rect.y += settings.car_speed
        else:
            self.kill()
