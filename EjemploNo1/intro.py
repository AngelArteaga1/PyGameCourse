# Import de Pygame
import pygame, sys
pygame.init()

# Inicializar la pantalla
size = (600,600)
screen = pygame.display.set_mode(size)

# loop
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()