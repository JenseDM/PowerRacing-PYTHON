import pygame 
import sys
import random
import pygame.mask

pygame.init()

from load_sprites import *
from pygame.sprite import *
from settings import *

settings = Settings()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Player_image
        self.rect = Player_image.get_rect()
        self.image = pygame.transform.scale(self.image, (settings.car_width, settings.car_height))
        self.rect.x = settings.car_pos_x
        self.rect.y = settings.car_pos_y
        self.mask = pygame.mask.from_surface(self.image)
        self.moving_right = False
        self.moving_left = False

    def move_right(self, pixels):
        if self.rect.x < 550:
            self.rect.x += pixels

    def move_left(self,pixels):
        if self.rect.x > 200:
            self.rect.x -= pixels
    
    def process_event_car(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_LEFT:
                self.moving_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            if event.key == pygame.K_LEFT:
                self.moving_left = False

    def move_car(self):
        if self.moving_right:
            self.move_right(settings.car_speed)
        if self.moving_left:
            self.move_left(settings.car_speed)