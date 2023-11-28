import pygame

class Button:
    def __init__(self, x, y, width, height,image,hover_image,action, hover_action):
        self.rect = pygame.Rect(x, y, width, height) #rectángulo que representa el botón
        self.action = action #función que se ejecuta cuando se hace click en el botón
        self.hover_action = hover_action #función que se ejecuta cuando el mouse está sobre el botón
        self.image = image #imagen que se muestra cuando el mouse no está sobre el botón
        self.hover_image = hover_image #imagen que se muestra cuando el mouse está sobre el botón
        self.hovered = False  #atributo para rastrear el estado de hover

    # Dibuja el botón en la pantalla
    def draw(self, screen):
        if self.hovered:
            screen.blit(self.hover_image, self.rect.topleft)
        else:
            screen.blit(self.image, self.rect.topleft)
    # Maneja el evento click
    def handle_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()
    # Maneja el evento hover
    def handle_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True  # Cambia a True solo si no estaba previamente en ese estado

                # Llama a hover_action si self.hovered es True y hover_action está definida
                if self.hover_action is not None and callable(self.hover_action):
                    self.hover_action()
        else:
            self.hovered = False
            