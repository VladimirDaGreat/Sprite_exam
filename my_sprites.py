"""
This game is to test my understanding of sprites and python
By: Vladimir Ramoi

27/05/2018
"""

import pygame
import random

# --- Global Constants ---

WHITE = (255, 255, 255)
RED   = (255,   0,   0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

# --- Classes ---

class Block(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()

class Player(pygame.sprite.Sprite):
    """ This class represents the player. """

    def __init__(self, x, y):
        super().__init__()

        # Set height, width
        
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        # Make our top-left corner the passed-in location.
        self.rect.x = x
        self.rect.y = y

        # set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        # Change the speed of the player.
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player location. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to creat a new instance of this
        class. """

    def __init__(self):
        """ Constructor. Create all our attributes and initaialize
            the game. """

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()

        # Create the player
        self.player = Player(5, 5)
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_f:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_e:
                   self. player.changespeed(0, -3)
                elif event.key == pygame.K_d:
                    self.player.changespeed(0, 3)
     
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_f:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_e:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_d:
                    self.player.changespeed(0, -3)
                
        return False

    def run_logic(self):
        """
        This method is run each time throught the fraem. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

    def display_frame(self, screen):
        """ Display everything to the screen for the game."""
        screen.fill(WHITE)

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()
    
def main():
    """ Main program function. """
    # Initailize Pygame and set up the window
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Sprite Examination")
    pygame.mouse.set_visible(False)

    # Create our objects and set the date
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()
    
