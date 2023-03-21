# Import de Pygame
import pygame, sys, random
pygame.init()

# Definicion de colores
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)

# Inicializar la pantalla
screen = pygame.display.set_mode([720, 720])

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('meteor.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
        if(self.rect.y > screen.get_height()):
            self.rect.y = 0
            self.rect.x = random.randrange(screen.get_width())

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        mouse_pos = pygame.mouse.get_pos()   
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

# Reloj del juego (FPS)
clock = pygame.time.Clock()

# Imagenes
background = pygame.image.load('background.png').convert()
player = pygame.image.load('player.png').convert()
player.set_colorkey(BLACK)
score = 0

pygame.mouse.set_visible(0)

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(screen.get_width())
    meteor.rect.y = random.randrange(screen.get_height())
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

# loop
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(WHITE)
    screen.blit(background, [0,0])

    # --- ZONA DE DIBUJO
    all_sprite_list.update()

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    for meteor in meteor_hit_list:
        score += 1
        print(score)
    all_sprite_list.draw(screen)

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)