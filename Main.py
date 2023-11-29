'''
Autores: 
        Luisa Fernanda Ramirez Velazco - 1002861605
        Jense David Martinez Tobón -1004685332   
'''
# Description: Archivo principal del juego, contiene las funciones de las ventanas y el menú principal
import pygame
import sys
from Juego import *
from button import *
import pygame.mixer

pygame.init()
#Configuración de la ventana
Ancho = 800
Alto = 500
size = (Ancho, Alto)
pygame.display.set_caption("Power Racing")
screen = pygame.display.set_mode(size)
# Tamaño del ícono deseado
icon_size = (64, 64)  
icono = pygame.image.load("./Img/icono.png")
icon = pygame.transform.scale(icono, icon_size)
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
#Img y sonidos
fondo_menu = pygame.image.load("./Img/Power Racing 2.png")
fondo_user = pygame.image.load("./Img/user_main.png")
fondo_score = pygame.image.load("./Img/score_main.png")
fondo_help = pygame.image.load("./Img/help_main.png")

music_menu = pygame.mixer.Sound("./Sounds/music_menu.mp3")
music_menu.set_volume(0.2)
music_user = pygame.mixer.Sound("./Sounds/music_user.mp3")
music_score = pygame.mixer.Sound("./Sounds/music_score.mp3")
music_help = pygame.mixer.Sound("./Sounds/music_help.mp3")
music_car = pygame.mixer.Sound("./Sounds/motionCar.mp3")
music_click = pygame.mixer.Sound("./Sounds/buttonClick.mp3")
getFont = pygame.font.Font(None, 40)

#Funcion para reproducir musica del carro
def StartMusic(cancion):
    #Detener musica
    pygame.mixer.stop()
    cancion.play()

#Ventana Usuario
def menu_user():
    #Reproducir musica
    StartMusic(music_user)
    fuente = getFont
    global nombreUsuario
    nombreUsuario = ""
    texto = ""
    button_menu_user = Button(305,350,200,53, pygame.image.load("Buttons/ok.png"),pygame.image.load("Buttons/ok_on.png"),main_juego, music_click.play)
    running = True
    #Capturar nombre del usuario
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                    button_menu_user.handle_hover()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("Texto ingresado:", texto)
                    nombreUsuario = texto
                    texto = ""
                    capturar_nombre(nombreUsuario)
                    button_menu_user.handle_click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif event.key == pygame.K_RETURN:
                    print("Texto ingresado:", texto)
                    nombreUsuario = texto
                    texto = ""
                    capturar_nombre(nombreUsuario)
                    main_juego()
                else:
                    texto += event.unicode
        #Mostrar texto
        screen.fill((0, 0, 0))
        screen.blit(fondo_user, (0, 0))
        texto_superficie = fuente.render(texto, True, "white")
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = (400, 250)     
        screen.blit(texto_superficie, texto_rect)   
        button_menu_user.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

#Funcion para obtener el nombre del usuario
def obtener_nombres():
    with open('usuario.txt', 'r') as file:
        return file.readlines()
    
#Función para Limpiar el score borrando el contenido del archivo    
def borrar_nombres():
    with open('usuario.txt', 'w') as file:
        file.truncate(0)

#Ventana Score
def menu_score():
    #Reproducir musica
    StartMusic(music_score)
    buttons_score = [
    Button(47,440,200,53, pygame.image.load("Buttons/back.png"),pygame.image.load("Buttons/back_on.png"),menu_principal, music_click.play),
    Button(248,440,200,53, pygame.image.load("Buttons/clear.png"),pygame.image.load("Buttons/clear_on.png"),borrar_nombres, music_click.play)
    ]
    running = True
    #Ciclo principal de la ventana score
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for button in buttons_score:
                    button.handle_hover()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_score:
                    button.handle_click()

        screen.fill((0, 0, 0))
        screen.blit(fondo_score, (0, 0))

        # Mostrar título
        fuente_nombre = getFont
        title_user = fuente_nombre.render("Users", True, "white")
        title_points = fuente_nombre.render("Points", True, "white")
        title_rect = title_user.get_rect()
        title_rect.center = (250, 160)  # Posición de "Users"
        screen.blit(title_user, title_rect)

        points_rect = title_points.get_rect()
        points_rect.center = (590, 160)  # Posición de "Points"
        screen.blit(title_points, points_rect)

        # Mostrar nombres y puntajes
        nombres = obtener_nombres()  # Obtener todos los nombres del archivo
        y_offset = 200  # Ajustar la posición vertical inicial

        #Iterar sobre cada línea del archivo
        for line in nombres:   
            line = line.strip()  # Eliminar espacios en blanco y saltos de línea
            nombre, puntaje = line.split(",")  # Dividir la línea en nombre y puntaje

            # Mostrar el nombre centrado debajo del título "Users"
            texto_nombre = fuente_nombre.render(nombre, True, "white")
            texto_nombre_rect = texto_nombre.get_rect()
            texto_nombre_rect.center = (250, y_offset)
            screen.blit(texto_nombre, texto_nombre_rect)

            # Mostrar el puntaje centrado debajo del título "Points"
            texto_puntaje = fuente_nombre.render(puntaje.strip(), True, "white")
            texto_puntaje_rect = texto_puntaje.get_rect()
            texto_puntaje_rect.center = (590, y_offset)
            screen.blit(texto_puntaje, texto_puntaje_rect)

            y_offset += 30  # Ajustar el espacio vertical entre nombres y puntajes

        # Dibujar los botones
        for button in buttons_score:    
            button.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

#Ventana Help
def menu_help():
    #Reproducir musica
    StartMusic(music_help)
    button_menu_help = Button(305,430,200,53, pygame.image.load("Buttons/back.png"),pygame.image.load("Buttons/back_on.png"),menu_principal, music_click.play)
    running = True

    #Ciclo principal de la ventana help
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                    button_menu_help.handle_hover()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    button_menu_help.handle_click()

        screen.fill((0, 0, 0))
        screen.blit(fondo_help, (0, 0))
        button_menu_help.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

#Ventana Principal
def menu_principal():
    #Reproducir musica
    StartMusic(music_menu)  
    list_buttons_principal = [
    Button(361,300,400,400, pygame.image.load("Buttons/auto.png"),pygame.image.load("Buttons/auto_on.png"),None, music_car.play),
    Button(130,15,563,70,pygame.image.load("Buttons/titulo.png"),pygame.image.load("Buttons/titulo_on.png"),None, None),
    Button(50, 130,200,62, pygame.image.load("Buttons/play.png"), pygame.image.load("Buttons/play_on.png"), menu_user, music_click.play),
    Button(50, 220,200,62,pygame.image.load("Buttons/score.png"), pygame.image.load("Buttons/score_on.png"), menu_score, music_click.play),
    Button(50, 310,200,62, pygame.image.load("Buttons/help.png"), pygame.image.load("Buttons/help_on.png"), menu_help, music_click.play),
    Button(50, 400,200,62, pygame.image.load("Buttons/exit.png"), pygame.image.load("Buttons/exit_on.png"), sys.exit, music_click.play)
    ]
    button_main  = list_buttons_principal

    #Ciclo principal del menú
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for button in button_main:
                    button.handle_hover()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_main:
                    button.handle_click()
                
        screen.fill((0, 0, 0))
        screen.blit(fondo_menu, (0, 0))
        for button in button_main:
            button.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu_principal()   