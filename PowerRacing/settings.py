import pygame
import sys

#configuracion del juego
class Settings:
    def __init__(self):
        self.car_width = 30
        self.car_height = 60
        
        self.car_pos_x = 400
        self.car_pos_y = 400

        self.car_speed = 5

        self.enemy_pos_y = -100

        self.carril_1 = 235
        self.carril_2 = 345
        self.carril_3 = 450
        self.carril_4 = 550
        self.carril_5 = 390
        self.carril_6 = 290

        self.num_vidas = 5

        self.time_enemy = 30