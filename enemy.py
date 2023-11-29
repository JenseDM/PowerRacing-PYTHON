#modulo que contiene la clase enemy_car, la cual crea los enemigos del juego
import pygame 
import pygame.mask

pygame.init()

from load_sprites import *
from pygame.sprite import *
from settings import *
# Se instancia la clase Settings
settings = Settings()
#Se crea la clase enemy_car
class enemy_car(pygame.sprite.Sprite):
    def __init__(self, bad,lane):
        super().__init__()
        self.bad = bad # Tipo de enemigo
        self.lane = lane # Carril en el que aparece
        # Carga la imagen del enemigo dependiendo del tipo
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
    
        #se inician los demas atributos de la clase `enemy_car`.
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (settings.car_width, settings.car_height))
        self.rect.x = self.lane
        self.rect.y = settings.enemy_pos_y
        self.mask = pygame.mask.from_surface(self.image)
    # Función que aumenta la velocidad de los autos
    def aumentar_velocidad(self):
        from Juego import tiempo
        if settings.car_speed <= 10:
            if tiempo % 700 == 0:
                settings.car_speed += 0.5
                print("Velocidad de los autos: ", settings.car_speed)
    # Función que mueve los autos
    def move(self):
        if self.rect.x < 650:
            self.rect.y += settings.car_speed
            self.aumentar_velocidad()
        else:
            self.kill()