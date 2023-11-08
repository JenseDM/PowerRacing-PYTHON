import pygame
import sys
import random
import pygame.mask
import pygame.mixer
from button import *
pygame.init()

screen_size = pygame.display.set_mode([800, 500])
pygame.display.set_caption("Power Racing")
clock = pygame.time.Clock()

background = pygame.image.load("./Img/Carretera.png").convert()
background_width = background.get_width()
fondo_gameOver = pygame.image.load("./Img/help_main.png")

from Player import *
from enemy import *
from settings import *

white = (255, 255, 255)
settings = Settings()
player = Player()
sound_car = pygame.mixer.Sound("./Sounds/move.mp3")
sound_shok = pygame.mixer.Sound("./Sounds/choque.mp3")
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
hueco_sprites = pygame.sprite.Group()
enemy_timer = 0

aux = False
collision_count = 0


def GameOver():
    #Reproducir musica
    #StartMusic(music_help)
    button_menu_help = Button(305,430,200,53, pygame.image.load("Buttons/back.png"),pygame.image.load("Buttons/back_on.png"),None, None)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                    button_menu_help.handle_hover()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    button_menu_help.handle_click()

        screen_size.fill((0, 0, 0))
        screen_size.blit(fondo_gameOver, (0, 0))
        button_menu_help.draw(screen_size)
        pygame.display.flip()

    pygame.quit()
    sys.exit()
def crash(value):
    global aux,collision_count

    if value == True and aux == False:
        aux = True
        collision_count += 1
        sound_shok.play()
        print("Choque:", collision_count)
    
    if value == False and aux == True:
        aux = False

    if collision_count >= settings.num_vidas:
        print("GAME OVER")
        GameOver()
        #sys.exit()
    
# LÓGICA DEL JUEGO
def main_juego():
    pygame.mixer.stop()
    fuente = pygame.font.SysFont("Pixel Operator", 30)
    scroll = 0  # Posición vertical inicial de la carretera
    game_over = False
    enemy_timer = 0
    hueco_timer = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sound_car.play()
            player.process_event_car(event)
            
        player.move_car()

        # Desplazamiento de la carretera    
        screen_size.blit(background, (0, scroll))
        screen_size.blit(background, (0, scroll - background.get_height()))  # Copia desplazada

        scroll += 5

        if scroll >= background.get_height():
            scroll = 0  # Restablece la posición cuando alcanza el tamaño de la imagen de fondo

        # Crea los enemigos
        enemy_timer += 1
        if enemy_timer >= settings.time_enemy:
            enemy_timer = 0
            lane = random.choice([settings.carril_1, settings.carril_2, settings.carril_3, settings.carril_4])
            enemy = enemy_car(random.randint(1, 5), lane)
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)
        '''
        # Crea los huecos
        hueco_timer += 1
        if hueco_timer >= settings.time_enemy:
            hueco_timer = 0
            lane = random.choice([settings.carril_5, settings.carril_6])
            hueco = Hueco(lane)
            all_sprites.add(hueco)
            hueco_sprites.add(hueco)
        '''
        # Mueve los enemigos
        for enemy in enemy_sprites:
            enemy.move()
        
        # Mueve los huecos
        for hueco in hueco_sprites:
            hueco.move()

        # Colisiones
        for enemy in enemy_sprites:
            car_collision_list = pygame.sprite.spritecollide(player,enemy_sprites,False,pygame.sprite.collide_mask)
            if car_collision_list:
                for colliding_enemy in car_collision_list:
                    colliding_enemy.colision_move(1) 
                crash(True)
            else:
                crash(False)

        # Dibuja los sprites
        all_sprites.draw(screen_size)
        texto = "Vidas: " + str(settings.num_vidas-collision_count) 
        Texto1 = fuente.render(texto,False,white)
        screen_size.blit(Texto1,(421,10))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

