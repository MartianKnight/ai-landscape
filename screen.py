import pygame, sys, random
from pygame.locals import *

# constants representing colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BROWN = ( 153, 76, 0)
GREY = ( 255, 0, 255)

# cloud positions
cloudx = -200
cloudy = 0

# constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
CLOUD = 6

# game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

# dictionary linking resources to colors
colors = {
            DIRT : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            COAL : BLACK,
            ROCK : GREY,
            LAVA : RED
        }

# TODO: Add diamond resource
textures = {
            DIRT : pygame.image.load('dirt.png'),
            GRASS : pygame.image.load('grass.png'),
            WATER : pygame.image.load('water.png'),
            COAL : pygame.image.load('coal.png'),
            ROCK : pygame.image.load('dirt.png'),
            LAVA : pygame.image.load('dirt.png'),
            CLOUD : pygame.image.load('cloud.png')
        }

inventory = {
            DIRT : 0,
            GRASS : 0,
            WATER : 0,
            COAL : 0
        }

# tilemap = [
#             [GRASS, COAL, DIRT, LAVA, GRASS],
#             [WATER, WATER, GRASS, LAVA, GRASS],
#             [COAL, GRASS, WATER, WATER, ROCK],
#             [DIRT, GRASS, COAL, WATER, ROCK],
#             [GRASS, WATER, DIRT, GRASS, COAL]
#         ]
resources = [DIRT,GRASS,WATER,COAL]

tilemap = [ [random.choice(resources) for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

PLAYER = pygame.image.load('player.png')
playerPos = [0,0]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))

#INVFONT = pygame.font.SysFont("comicsansms",15)
INVFONT = pygame.font.Font("freesansbold.ttf", 18)
pygame.display.set_caption('M I N E C R A F T -- 2 D')
pygame.display.set_icon(pygame.image.load('player.png'))

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# finish tile map
for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,15)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

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

    # Clear the screen
    DISPLAYSURF.fill(BLACK)
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

    # TODO: text issue when inventory display a number over 10

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            elif (event.key == K_LEFT) and playerPos[0] > 0:
                playerPos[0] -= 1
            elif (event.key == K_UP) and playerPos[1] > 0:
                playerPos[1] -= 1
            elif (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            elif event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
                print(inventory)
            # place dirt
            elif (event.key == K_1):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1
            # place grass
            elif (event.key == K_2):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[GRASS] > 0:
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    inventory[currentTile] += 1
            elif (event.key == K_3):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[WATER] > 0:
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    inventory[currentTile] += 1
            elif (event.key == K_4):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[COAL] > 0:
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    inventory[currentTile] += 1
        # else:
            #print(event)

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE,row*TILESIZE, TILESIZE, TILESIZE))
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

    placePositionInv = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item],(placePositionInv,MAPHEIGHT*TILESIZE+20))
        placePositionInv += 45
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePositionInv,MAPHEIGHT*TILESIZE+20))
        placePositionInv += 50

    DISPLAYSURF.blit(textures[CLOUD],(cloudx,cloudy));
    cloudx += 1

    if cloudx > MAPWIDTH*TILESIZE:
        cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
        cloudx = -200



    pygame.display.update()
    fpsClock.tick(FPS)
