# Import de Pygame
import pygame, sys
pygame.init()

# Definicion de colores
WHITE = (255, 255, 255)

# Inicializar la pantalla
screen = pygame.display.set_mode([720, 720])

# Reloj del juego (FPS)
clock = pygame.time.Clock()

background = pygame.image.load('background.png').convert()

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO

    screen.blit(background, [0,0])

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)