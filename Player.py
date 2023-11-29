#Modulo que contiene la clase Player, la cual se encarga de crear el objeto jugador, 
#el cual es el carro que se mueve en la pantalla
import pygame 
import pygame.mask
from load_sprites import *
from pygame.sprite import *
from settings import *
pygame.init()
# Se instancia la clase Settings
settings = Settings()

#Se crea la clase Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Player_image # Imagen del jugador
        self.rect = Player_image.get_rect() # Rectángulo de la imagen
        self.image = pygame.transform.scale(self.image, (settings.car_width, settings.car_height))
        self.rect.x = settings.car_pos_x   # Posición inicial en x 
        self.rect.y = settings.car_pos_y   # Posición inicial en y
        self.mask = pygame.mask.from_surface(self.image)  # Máscara de colisión
        self.moving_right = False  # Variable que indica si se mueve a la derecha
        self.moving_left = False  # Variable que indica si se mueve a la izquierda
        self.velocidad = 4  # Velocidad de movimiento
        
    def move_right(self, pixels): # Función que mueve el carro a la derecha
        if self.rect.x < 550:
            self.rect.x += pixels

    def move_left(self,pixels): # Función que mueve el carro a la izquierda
        if self.rect.x > 200:
            self.rect.x -= pixels
    
    def process_event_car(self, event): # Función que procesa los eventos del carro
        if event.type == pygame.KEYDOWN: # Si se presiona la tecla, se mueve
            if event.key == pygame.K_d:
                self.moving_right = True
            if event.key == pygame.K_a:
                self.moving_left = True

        if event.type == pygame.KEYUP: # Si se suelta la tecla, se detiene el movimiento
            if event.key == pygame.K_d:
                self.moving_right = False
            if event.key == pygame.K_a:
                self.moving_left = False

    def move_car(self): # Función que mueve el carro
        if self.moving_right:
            self.move_right(self.velocidad)
        if self.moving_left:
            self.move_left(self.velocidad)