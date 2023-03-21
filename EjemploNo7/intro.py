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
x = 10
y = 10
speed = 0

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -3
            if event.key == pygame.K_RIGHT:
                speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed = 0
            if event.key == pygame.K_RIGHT:
                speed = 0

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    x += speed
    pygame.draw.rect(screen, RED, (x, y, 100, 100))

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)