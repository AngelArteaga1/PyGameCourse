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

# Variables
coord = [10,10]
speed = [00,00]

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -3
            if event.key == pygame.K_RIGHT:
                speed[0] = 3
            if event.key == pygame.K_DOWN:
                speed[1] = 3
            if event.key == pygame.K_UP:
                speed[1] = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed[0] = 0
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_DOWN:
                speed[1] = 0
            if event.key == pygame.K_UP:
                speed[1] = 0

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    coord[0] += speed[0]
    coord[1] += speed[1]
    pygame.draw.rect(screen, RED, (coord[0], coord[1], 100, 100))

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)