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

global white
white= (255, 255, 255)

from Player import *
from enemy import *
from settings import *
from power import *

#Funcion para capturar el nombre del usuario
def capturar_nombre(name):
    global nombreJugador
    nombreJugador = name
    
#Funcion para regresar al menu principal
def regresar():
    import Main  # Importar el archivo Main (sugiriendo que se encuentra en el mismo directorio)
    Main.menu_principal()   # Regresamos al menú principal

#Funcion para guardar el nombre del usuario y el puntaje en un archivo de texto
def agregar_nombre():
    global Puntaje
    nombre_encontrado = False
    lineas_actualizadas = []
    
    with open('usuario.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            parts = line.split(', ')
            nombre = parts[0]
            puntaje = int(parts[1])
            if nombre == nombreJugador:
                nombre_encontrado = True
                if Puntaje > puntaje:
                    line = f"{nombreJugador}, {Puntaje}\n"
            lineas_actualizadas.append(line.rstrip('\n'))  # Elimina el salto de línea existente
    
    if not nombre_encontrado:
        lineas_actualizadas.append(f"{nombreJugador}, {Puntaje}")

    with open('usuario.txt', 'w') as file:
        file.write('\n'.join(lineas_actualizadas))  # Une todas las líneas con saltos de línea

    if nombre_encontrado:
        print("Puntaje actualizado correctamente.")
    else:
        print("Nuevo registro agregado.")

#Funcion para mostrar el menu de game over y su funcionalidad
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

#Función para aplicar habilidad de aumento de salud
def poder():
    sound_power = pygame.mixer.Sound("./Sounds/power.mp3")
    sound_power.play()
    settings.num_vidas += 1

#Función para detectar colisiones
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
        agregar_nombre()
        GameOver()
        #sys.exit()

#Lógica del juego
def main_juego():
    pygame.mixer.stop()
    global scroll, nombreJugador, collision_count, tiempo, Puntaje, aumento_vel, fuente, settings, player, sound_car, sound_shok, music_click, all_sprites, enemy_sprites, hueco_sprites, power_sprites, enemy_timer, aux
    fuente = pygame.font.SysFont("Pixel Operator", 30)
    sound_car = pygame.mixer.Sound("./Sounds/move.mp3")
    sound_shok = pygame.mixer.Sound("./Sounds/choque.mp3")
    music_click = pygame.mixer.Sound("./Sounds/buttonClick.mp3")
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    hueco_sprites = pygame.sprite.Group()
    power_sprites = pygame.sprite.Group()
    settings = Settings()
    player = Player()
    all_sprites.add(player)
    enemy_timer = 0
    aux = False
    collision_count = 0
    tiempo = 0
    Puntaje = 0
    aumento_vel = 5
    game_over = False
    scroll = 0
    power_timer = 0
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
        scroll += aumento_vel  # Velocidad de desplazamiento

        if scroll >= background.get_height():
            scroll = 0  # Restablece la posición cuando alcanza el tamaño de la imagen de fondo
            if scroll <= 10: 
                if tiempo % 300 == 0:
                    aumento_vel += 0.1
                    print("Velocidad de la carretera: ", scroll)

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
        
        power_collision_list = pygame.sprite.spritecollide(player, power_sprites, True, pygame.sprite.collide_mask)
        for power in power_collision_list:
            poder()

        # Colisiones
        for enemy in enemy_sprites:
            car_collision_list = pygame.sprite.spritecollide(player,enemy_sprites,False,pygame.sprite.collide_mask)
            if car_collision_list:
                """ for colliding_enemy in car_collision_list:
                    colliding_enemy.colision_move(1) """ 
                crash(True)
            else:
                crash(False)

        # Dibuja los sprites
        all_sprites.draw(screen_size)
        texto = str(settings.num_vidas-collision_count) 
        Texto1 = fuente.render(texto,False,white)
        screen_size.blit(corazon,(30,10))
        screen_size.blit(reloj,(360,10))
        screen_size.blit(Texto1,(45,22))
        screen_size.blit(score,(650,10))
        tiempo += 1 #Aumentamos enl tiempo con cada iteración
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

#main_juego()