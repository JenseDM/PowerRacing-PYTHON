'''
Autores: 
        Luisa Fernanda Ramirez Velazco - 1002861605
        Jense David Martinez Tobón -1004685332   
'''
# Description: Clase para los botones
import pygame

#Clase para los botones
class Button:
    def __init__(self, x, y, width, height,image,hover_image,action, hover_action):
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action
        self.hover_action = hover_action
        self.image = image
        self.hover_image = hover_image
        self.hovered = False  #atributo para rastrear el estado de hover

    #Función para dibujar los botones
    def draw(self, screen):
        if self.hovered:
            screen.blit(self.hover_image, self.rect.topleft)
        else:
            screen.blit(self.image, self.rect.topleft)
    #Función para manejar el click
    def handle_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()
    #Función para manejar el hover
    def handle_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True  # Cambia a True solo si no estaba previamente en ese estado

                # Llama a hover_action si self.hovered es True y hover_action está definida
                if self.hover_action is not None and callable(self.hover_action):
                    self.hover_action()
        else:
            self.hovered = False
            