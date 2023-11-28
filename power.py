import pygame
import pygame.mask
from load_sprites import *
from pygame.sprite import *
from settings import *

pygame.init()
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
        self.power_speed = settings.car_speed

    def aumentar_velocidad(self):
        from Juego import tiempo, aumento_vel
        if aumento_vel <= 10:
            if tiempo % 700 == 0:
                self.power_speed += 0.5
                print("Velocidad de la estrella: ", self.power_speed)

    def move(self):
        if self.rect.x < 650:
            self.rect.y += self.power_speed
            self.aumentar_velocidad()
        else:
            self.kill()

