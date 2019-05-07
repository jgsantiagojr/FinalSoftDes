from entity import Entity, DynamicEntity
import pygame


class Platform(Entity):
    """ Encodes the state of a platform in the game """
    def __init__(self, height, width, x, y):
        super().__init__(int(x+width/2), int(y+height/2), ['blatform.png'], resize = (int(width), int(height)))
