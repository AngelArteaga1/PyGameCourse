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

# Lista de coordenadas
listita_cord = []
for i in range(60):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    listita_cord.append([x,y])

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()


    # Color de fondo
    screen.fill(WHITE)

    # --- ZONA DE DIBUJO
    for coordenada in listita_cord:
        pygame.draw.circle(screen, RED, coordenada, 4)
        coordenada[1] += 1
        if(coordenada[1] > size[1]): 
            coordenada[1] = 0
    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(30)