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

# Reloj del juego (FPS)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    # print(mouse_pos)
    pygame.draw.rect(screen, RED, (x, y, 100, 100))


    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)