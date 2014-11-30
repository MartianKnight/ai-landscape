import pygame, sys
from pygame.locals import *

# constants representing colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BROWN = ( 153, 76, 0)
GREY = ( 255, 0, 255)

# constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

# dictionary linking resources to colors
colors = {
            DIRT : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            COAL : BLACK,
            ROCK : GREY,
            LAVA : RED
        }

tilemap = [
            [GRASS, COAL, DIRT, LAVA, GRASS],
            [WATER, WATER, GRASS, LAVA, GRASS],
            [COAL, GRASS, WATER, WATER, ROCK],
            [DIRT, GRASS, COAL, WATER, ROCK],
            [GRASS, WATER, DIRT, GRASS, COAL]
        ]

# game dimensions
TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('Setup tilemaps')

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# DISPLAYSURF.fill(WHITE)
# pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0,106)))
# pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
# pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
# pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
# pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
# pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
# pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

# pixObj = pygame.PixelArray(DISPLAYSURF)
# pixObj[480][380] = BLACK
# pixObj[482][382] = BLACK
# pixObj[484][384] = BLACK
# pixObj[486][386] = BLACK
# pixObj[488][388] = BLACK
# del pixObj
#
# catImg = pygame.image.load('cat.png')
# catx = 10
# caty = 10
# direction = 'right'
#
# fontObj = pygame.font.Font('freesansbold.ttf', 32)
# textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
# textRectObj = textSurfaceObj.get_rect()
# textRectObj.center = (200, 150)

while True: #main game loop

    # if direction == 'right':
    #     catx += 5
    #     if catx == 280:
    #         direction = 'down'
    # elif direction == 'down':
    #     caty += 5
    #     if caty == 220:
    #         direction = 'left'
    # elif direction == 'left':
    #     catx -= 5
    #     if catx == 10:
    #         direction = 'up'
    # elif direction == 'up':
    #     caty -= 5
    #     if caty == 10:
    #         direction = 'right'
    #
    # DISPLAYSURF.blit(catImg, (catx, caty))
    #
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE,row*TILESIZE, TILESIZE, TILESIZE))

    pygame.display.update()
    fpsClock.tick(FPS)
