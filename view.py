"""
platformer view code
"""

import pygame
from random import randint


class PyGameWindowView(object):
    """ A view of platformer rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        # Make display at resolution size in full screen
        self.screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

    def draw(self):
        """ Draw the current game objects to the screen """
        # Black background
        self.screen.fill(pygame.Color(0,0,0))

        # Draw white platforms in model
        for platform in self.model.stages[self.model.level].platforms:
            
            pygame.draw.rect(self.screen,
                             pygame.Color(255, 255, 255),
                             pygame.Rect(platform.x-                           self.model.topleft[0],
                                         platform.y- self.model.topleft[1],
                                         platform.width,
                                         platform.height))

            #platform.draw(self.model.topleft, self.screen)
        # Draw avatar as red square
        '''
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 0, 0),
                         pygame.Rect(self.model.avatar.x-                           self.model.topleft[0],
                                     self.model.avatar.y- self.model.topleft[1],
                                     self.model.avatar.width,
                                     self.model.avatar.height))
        '''
        self.model.avatar.draw(self.model.topleft, self.screen)
        #model.avatar.draw(self.model.topleft, self.screen)
        #print(self.model.avatar.x)
        #print(self.model.left_edge)
        # Call update so things actually change
        pygame.display.update()
