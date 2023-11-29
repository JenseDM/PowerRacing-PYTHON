'''
Autores: 
        Luisa Fernanda Ramirez Velazco - 1002861605
        Jense David Martinez Tobón -1004685332   
'''
# Description: Clase que contiene la configuración del juego
class Settings:
    def __init__(self):
        self.car_width = 50 #ancho del carro
        self.car_height = 80 #alto del carro
        self.car_pos_x = 400 #posicion inicial del carro en x
        self.car_pos_y = 400 #posicion inicial del carro en y
        self.car_speed = 5 #velocidad de los autos
        self.enemy_pos_y = -100 #posicion inicial de los enemigos en y
        self.power_pos_y = -100 #posicion inicial de los poderes en y
        self.carril_1 = 220 
        self.carril_2 = 330
        self.carril_3 = 435
        self.carril_4 = 535
        self.carril_5 = 375
        self.carril_6 = 275
        self.num_vidas = 5  #numero de vidas
        self.time_enemy = 40 #tiempo de aparicion de enemigos
        self.time_power = 300 #tiempo de aparicion de poderes