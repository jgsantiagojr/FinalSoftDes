from entity import Entity, DynamicEntity
import pygame


class Platform(object):
    """ Encodes the state of a platform in the game """
    def __init__(self,height,width,x,y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.mask = pygame.mask.Mask((int(width),int(height)))

    def __str__(self):
        return "Platform height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                          self.width,
                                                          self.x,
                                                          self.y)
'''
class Platform(Entity):
    """ Encodes the state of a platform in the game """
    def __init__(self, x, y, width, height, images):
        super().__init__(x, y, images, platforms)

        self.height = height
        self.width = width
'''
