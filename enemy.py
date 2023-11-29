'''
Autores: 
        Luisa Fernanda Ramirez Velazco - 1002861605
        Jense David Martinez Tobón -1004685332   
'''
#Description: Clase para los enemigos
import pygame 
import pygame.mask

pygame.init()

from load_sprites import *
from pygame.sprite import *
from settings import *

settings = Settings()

#Clase para el enemigo
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
    #Funcion para aumentar la velocidad de los autos
    def aumentar_velocidad(self):
        from Juego import tiempo
        if settings.car_speed <= 10:
            if tiempo % 700 == 0:
                settings.car_speed += 0.5
                print("Velocidad de los autos: ", settings.car_speed)
    #Funcion para mover los autos
    def move(self):
        if self.rect.x < 650:
            self.rect.y += settings.car_speed
            self.aumentar_velocidad()
        else:
            self.kill()
    #Funcion para mover los autos en la colision
    def colision_move(self, direction):
        if direction == 1:
            self.rect.x += self.enemy_speed
        elif direction == 2:
            self.rect.x -= self.enemy_speed
        elif direction == 3:
            self.rect.x += self.enemy_speed
        elif direction == 4:
            self.rect.x -= self.enemy_speed

