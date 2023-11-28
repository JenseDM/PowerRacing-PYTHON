# This code is importing necessary modules and classes for the "Power Racing" game. It imports the
# following modules: `pygame`, `sys`, `random`, `pygame.mask`, and `pygame.mixer`. It also imports
# classes from the following files: `button.py`, `Player.py`, `enemy.py`, `settings.py`, `power.py`,
# and `road.py`. Additionally, it initializes the pygame module, sets the screen size and caption, and
# loads images for the background and game over screen.
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
fondo_gameOver = pygame.image.load("./Img/game_over.png")

from Player import *
from enemy import *
from settings import *
from power import *
from road import *


def regresar():
    import Main  
    Main.menu_principal()  

def GameOver():
    buttons_GameOver = [
    Button(200,440,200,53, pygame.image.load("Buttons/play.png"), pygame.image.load("Buttons/play_on.png"), main_juego, music_click.play),
    Button(405,440,200,53, pygame.image.load("Buttons/back.png"),pygame.image.load("Buttons/back_on.png"),regresar, music_click.play)
    ]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                    for button in buttons_GameOver:
                        button.handle_hover()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons_GameOver:
                        button.handle_click()

        screen_size.fill((0, 0, 0))
        screen_size.blit(fondo_gameOver, (0, 0))
        for button in buttons_GameOver:
            button.draw(screen_size)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def poder():
    sound_power = pygame.mixer.Sound("./Sounds/power.mp3")
    sound_power.play()
    settings.num_vidas += 1

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
        pygame.mixer.stop()
        GameOver()
    
# LÓGICA DEL JUEGO
    """
    La función main_juego es la lógica de un juego donde el jugador controla un coche y evita colisiones.
    con autos enemigos mientras recolectas potenciadores y aumentas su puntuación.
    """
def main_juego():
    pygame.mixer.stop()
    global fuente, white, settings, player, sound_car, sound_shok, music_click, all_sprites, enemy_sprites, hueco_sprites, power_sprites, enemy_timer, aux, collision_count
    fuente = pygame.font.SysFont("Pixel Operator", 30)
    white = (255, 255, 255)
    settings = Settings()
    player = Player()
    road = Road(-500) 
    road_2 = Road(0)
    sound_car = pygame.mixer.Sound("./Sounds/move.mp3")
    sound_shok = pygame.mixer.Sound("./Sounds/choque.mp3")
    music_click = pygame.mixer.Sound("./Sounds/buttonClick.mp3")
    all_sprites = pygame.sprite.Group() # Grupo de sprites
    all_sprites.add(player)           # Agrega el jugador al grupo de sprites
    enemy_sprites = pygame.sprite.Group() # Grupo de enemigos
    power_sprites = pygame.sprite.Group() # Grupo de poderes
    road_sprites = pygame.sprite.Group() # Grupo de carreteras
    road_sprites.add(road) # Agrega la carretera al grupo de carreteras
    road_sprites.add(road_2) 
    enemy_timer = 0
    aux = False
    collision_count = 0 # Contador de colisiones
    game_over = False # Bandera para el game over
    enemy_timer = 0 # Timer para los enemigos
    power_timer = 0 # Timer para los poderes
    tiempo = 0  # Tiempo de juego
    Puntaje = 0 # Puntaje del juego
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sound_car.play()
            # Procesa los eventos del carro
            player.process_event_car(event)
        # Mueve el carro
        player.move_car()
        # Mueve la carretera
        road.move()
        road_2.move()

        # Crea los enemigos
        enemy_timer += 1
        if enemy_timer >= settings.time_enemy:
            enemy_timer = 0
            lane = random.choice([settings.carril_1, settings.carril_2, settings.carril_3, settings.carril_4])
            enemy = enemy_car(random.randint(1, 5), lane)
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)
        # Crea los poderes
        power_timer += 1
        if power_timer >= settings.time_power:
            power_timer = 0
            lane = random.choice([settings.carril_1, settings.carril_2, settings.carril_3, settings.carril_4])
            power = Power(lane)
            all_sprites.add(power)
            power_sprites.add(power)

        # Mueve los enemigos
        for enemy in enemy_sprites:
            enemy.move()
        # Mueve el poder
        for power in power_sprites:
            power.move()
        #colisiones con los poderes
        power_collision_list = pygame.sprite.spritecollide(player, power_sprites, True, pygame.sprite.collide_mask) 
        for power in power_collision_list:
            poder()

        # Colisiones con los enemigos
        for enemy in enemy_sprites:
            car_collision_list = pygame.sprite.spritecollide(player,enemy_sprites,False,pygame.sprite.collide_mask)
            if car_collision_list:
                crash(True)
            else:
                crash(False)
        
        road_sprites.draw(screen_size) # Dibuja la carretera
        all_sprites.draw(screen_size) # Dibuja los sprites
        texto = str(settings.num_vidas-collision_count) 
        Texto1 = fuente.render(texto,False,white)
        screen_size.blit(corazon,(30,10)) # Dibuja el corazón en pantalla
        screen_size.blit(reloj,(360,10)) # Dibuja el reloj en pantalla
        screen_size.blit(Texto1,(45,22)) # Dibuja el texto del corazón en pantalla
        screen_size.blit(score,(650,10)) # Dibuja el texto del puntaje en pantalla
        tiempo += 1 #Aumentamos el tiempo con cada iteración
        texto_tiempo = fuente.render( str(tiempo), False, white)   #creamos el texto del tiempo
        screen_size.blit(texto_tiempo, (410, 20)) #Mostramos el tiempo en pantalla
        if tiempo % 50 == 0: 
            Puntaje += 1 #Aumentamos el puntaje cada 2 segundos
        texto_puntaje = fuente.render(str(Puntaje), False, white)   #creamos el texto del puntaje
        screen_size.blit(texto_puntaje, (700, 20)) #Mostramos el puntaje en pantalla
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main_juego()