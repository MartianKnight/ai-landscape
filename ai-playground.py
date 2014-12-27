
import pygame
import random
"""
Global constants
"""
# constants representing colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BROWN = ( 153, 76, 0)
GREY = ( 255, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Classes

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
    # Set speed vector
    change_x = 0
    change_y = 0
    walls = None
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
        # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
            # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            # Move up/down
        self.rect.y += self.change_y
            # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
        # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# Set the title of the window
pygame.display.set_caption('Test')
# List to hold all the sprites
all_sprites_lists = pygame.sprite.Group()


# --- Sprite lists

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites

for i in range(50):
    # This represents a block
    block = Block(BLUE)

    # Set a random location for the block
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(350)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_lists.add(block)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0


# Make the walls. (x_pos, y_pos, width, height)
# Walls are now unlocked 
wall_list = pygame.sprite.Group()
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprites_lists.add(wall)
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprites_lists.add(wall)
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprites_lists.add(wall)
wall = Wall(150, 400, 100, 10)
wall_list.add(wall)
all_sprites_lists.add(wall)

# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
all_sprites_lists.add(player)
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_lists.add(bullet)
            bullet_list.add(bullet)

    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_lists.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_lists.remove(bullet)
            score += 1
            print(score)

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_lists.remove(bullet)

    screen.fill(WHITE)
    all_sprites_lists.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
