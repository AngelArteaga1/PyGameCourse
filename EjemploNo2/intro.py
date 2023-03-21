# Import de Pygame
import pygame, sys
pygame.init()

# Definicion de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)


# Inicializar la pantalla
size = (600,600)
screen = pygame.display.set_mode(size)

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    pygame.draw.line(screen, GREEN, [0, 100], [150, 150], 5)
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))
    pygame.draw.circle(screen, RED, (300,300), 100)
    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()