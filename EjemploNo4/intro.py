# Import de Pygame
import pygame, sys
pygame.init()

# Definicion de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

x = 0
y = 200
speedx = 1
speedy = 1

# Inicializar la pantalla
size = (600,600)
screen = pygame.display.set_mode(size)

# Reloj del juego (FPS)
clock = pygame.time.Clock()

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    if x > (size[0] - 80) or x < 0:
        speedx *= -1
    if y > (size[1] - 80) or y < 0:
        speedy *= -1

    x += speedx
    y += speedy

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (x, y, 80, 80))
    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)