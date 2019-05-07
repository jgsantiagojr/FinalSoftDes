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
        self.screen = pygame.display.set_mode(size,pygame.RESIZABLE)

    def draw(self):
        """ Draw the current game objects to the screen """
        # Black background
        self.screen.fill(pygame.Color(255,255,255))

        for p in self.model.stage().platforms:
            p.draw(self.model.camera, self.screen)

        for e in self.model.enemies:
            e.draw(self.model.camera,self.screen)

        for p in self.model.enemy_projectiles:
            p.draw(self.model.camera,self.screen)

        for p in self.model.friendly_projectiles:
            p.draw(self.model.camera,self.screen)

        self.model.avatar.draw(self.model.camera, self.screen)

        # Call update so things actually change
        pygame.display.update()
