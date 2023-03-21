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
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
        pygame.draw.line(screen, GREEN, (x, 0), (x, 100), 5)
    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()