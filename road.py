import pygame 
import pygame.mask

pygame.init()

from settings import *
settings = Settings()

class Road(pygame.sprite.Sprite):
    def __init__(self,y):
        super().__init__()
        self.image = pygame.image.load("./Img/Carretera.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.y < 500:
            self.rect.y += settings.car_speed
        else:
            self.rect.y = -500
