# Import de Pygame
import pygame, sys, random
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

# Variables del sistema
speed = 1

# Lista de coordenadas
circles = []
for i in range(60):
    circle = {}
    circle['coord'] = [random.randint(0, size[0]), random.randint(0, size[1])]
    circle['speed'] = [random.randint(-2, 2), random.randint(-2,2)]
    circle['radius'] = random.randint(3, 7)
    circles.append(circle)

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()


    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    for circle in circles:
        if circle["coord"][0] + circle['radius'] > size[0] or circle["coord"][0] - circle['radius'] < 0:
            circle["speed"][0] *= -1
        if circle["coord"][1] + circle['radius'] > size[1] or circle["coord"][1] - circle['radius'] < 0:
            circle["speed"][1] *= -1
        circle["coord"][0] += circle["speed"][0]
        circle["coord"][1] += circle["speed"][1]
        pygame.draw.circle(screen, RED, circle["coord"], circle['radius'])
    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)