# Import de Pygame
import pygame, sys
pygame.init()

# Definicion de colores
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)

# Inicializar la pantalla
screen = pygame.display.set_mode([720, 720])

# Reloj del juego (FPS)
clock = pygame.time.Clock()

# Imagenes
background = pygame.image.load('background.png').convert()
player = pygame.image.load('player.png').convert()
player.set_colorkey(BLACK)

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
    screen.blit(background, [0,0])
    screen.blit(player , mouse_pos)

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)