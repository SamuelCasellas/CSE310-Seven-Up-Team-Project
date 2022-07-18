import os
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

MUSIC = pygame.mixer.music
MUSIC.set_volume(0.05)

DEFAULT_PATH = os.path
ASSET_PATH = os.path.join("Assets")

LETTER_SIZE = 4
BORDER_DISTANCE = 0
WIDTH = 900
HEIGHT = 700

#This is a file that contains default values that can be called repeatedly.
#This file will also allow for easy testing of speeds, etc.

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors, maybe we need to agree on a theme.
#         RED   GREEN BLUE
WHITE =  (255,  255,  255)
BLACK =  (0,    0,    0)
RED =    (255,  0,    0)
GREEN =  (0,    255,  0) 
BLUE =   (0,    0,    255)
YELLOW = (255,  255,  0)
TEAL =   (0,    255,  255)
PURPLE = (255,  0,    255)
BROWN =  (255,  255,  0)

MAIN_FONT = pygame.font.SysFont("comicsans", 100) 
ROCK_FONT = pygame.font.SysFont("comicsans", 40)
STATS_FONT = pygame.font.SysFont("Comic Sans Ms", 35)
FONT = pygame.font.SysFont('Arial', 40)
SCORE = pygame.font.SysFont('Arial', 60)

FPS = 60
ASTEROID_VEL = 1.25
BORDER_DISTANCE = 0 #to spawn asteroids in the borders of the game
LETTER_SIZE = 5 #for use in asteroids

ASTEROID_HIT = pygame.USEREVENT + 1 #for collision between bullet and successful type?
CANNON_HIT = pygame.USEREVENT + 2   #for collision between asteriod and cannon
DEFAULT_PATH = os.path
ASSET_PATH = DEFAULT_PATH.join("Assets")


SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
    ASSET_PATH, "Pictures", "Backgrounds", "Background.PNG")), 
    (WIDTH+100, HEIGHT+100))

SPACESTATION_SIZE = (WIDTH- (WIDTH/10), WIDTH- (WIDTH/10))

SPACESTATION = pygame.transform.scale(pygame.image.load(
    os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
    ASSET_PATH, "Pictures", "Space-Station", "Space Station.png")), 
    (SPACESTATION_SIZE))

# Different asteroid images
asteroid_image_1 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_1.png"))
asteroid_image_2 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_2.png"))
asteroid_image_3 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_3.png"))
asteroid_images = [asteroid_image_1, asteroid_image_2, asteroid_image_3]

# TIMER_COUNT = 0
ROCK_FONT = pygame.font.SysFont('comicsans', 40)

explosion_anim = []
for i in range(16):
    if i < 10:
        filename = 'expl_01_000{}.png'.format(i)
    if i >= 10:
        filename = 'expl_01_00{}.png'.format(i)
    img = pygame.image.load(os.path.join("Assets", "Pictures", "explosion", filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim.append(img_lg)