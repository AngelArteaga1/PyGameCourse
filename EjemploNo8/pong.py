# Import de Pygame
import pygame, sys
pygame.init()

# Definicion de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

# Inicializar la pantalla
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Pong Game :3')

# pygame.mouse.set_visible(0)

# Reloj del juego (FPS)
clock = pygame.time.Clock()

# players
player = {}
player['width'] = 15
player['height'] = 90

config_p1 = {}
config_p2 = {}
config_ball = {}

def update_config():
    global config_p1
    global config_p2
    global config_ball

    # player one
    config_p1 = {
        'x' : 30,
        'y' : screen.get_height()/2 - player['height'] / 2,
        'speed' : 0
    }

    # player two
    config_p2 = {
        'x' : screen.get_width() - 30 - player['width'],
        'y' : screen.get_height()/2 - player['height'] / 2,
        'speed' : 0
    }

    # ball
    config_ball = {
        'x' : screen.get_width()/2,
        'y' : screen.get_height()/2,
        'speedx' : 5,
        'speedy' : 5,
        'radius' : 10
    }
update_config()

game_over = False

# loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # Player one
            if event.key == pygame.K_w:
                config_p1['speed'] = -8
            if event.key == pygame.K_s:
                config_p1['speed'] = 8
            # Player two
            if event.key == pygame.K_UP:
                config_p2['speed'] = -8
            if event.key == pygame.K_DOWN:
                config_p2['speed'] = 8
            # Esc
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                update_config()
        elif event.type == pygame.KEYUP:
            # Player one
            if event.key == pygame.K_w:
                config_p1['speed'] = 0
            if event.key == pygame.K_s:
                config_p1['speed'] = 0
            # Player two
            if event.key == pygame.K_UP:
                config_p2['speed'] = 0
            if event.key == pygame.K_DOWN:
                config_p2['speed'] = 0
        elif event.type == pygame.VIDEORESIZE:
            update_config()
            pygame.display.update()
        
    if config_ball['y'] + config_ball['radius'] > screen.get_height() or config_ball['y'] < config_ball['radius']:
        config_ball['speedy'] *= -1
    if config_ball['x'] + config_ball['radius'] > screen.get_width() or config_ball['x'] < config_ball['radius']:
        config_ball['x'] = 400
        config_ball['y'] = 300
        config_ball['speedx'] *= -1
        config_ball['speedy'] *= -1

    # Color de fondo
    screen.fill(BLACK)

    # --- ZONA DE DIBUJO
    # For the movement of the players
    pos_tmp1 = config_p1['y'] + config_p1['speed']
    pos_tmp2 = config_p2['y'] + config_p2['speed']
    if pos_tmp1 + player['height'] <= screen.get_height() and pos_tmp1 >= 0:
        config_p1['y'] += config_p1['speed']
    if pos_tmp2 + player['height'] <= screen.get_height() and pos_tmp2 >= 0:
        config_p2['y'] += config_p2['speed']

    # Movement for the ball
    config_ball['x'] += config_ball['speedx']
    config_ball['y'] += config_ball['speedy'] 

    
    player_one = pygame.draw.rect(screen, WHITE, (config_p1['x'], config_p1['y'], player['width'], player['height']))
    player_two = pygame.draw.rect(screen, WHITE, (config_p2['x'], config_p2['y'], player['width'], player['height']))
    ball = pygame.draw.circle(screen, WHITE, (config_ball['x'], config_ball['y']), config_ball['radius'])

    # Colitions
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        config_ball['speedx'] *= -1

    # --- ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
