from entity import Entity, DynamicEntity
import pygame

'''
class Platform(object):
    """ Encodes the state of a platform in the game """
    def __init__(self,height,width,x,y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.left = x
        self.right = x+width
        self.top = y
        self.bottom = y + height
        self.mask = pygame.mask.Mask((int(width),int(height)))


    def contains_point(self, point):
        if self.x < point[0] and point[0] < self.x + self.width:
            if self.x < point[0] and point[0] < self.x + self.width:
                return True
        return False

    def draw(self, camera, screen):
        self.rect = pygame.Rect(self.x-camera.left,self.y-camera.top,self.width,self.height)
        pygame.draw.rect(screen, (255,255,255), self.rect)


    def __str__(self):
        return "Platform height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                          self.width,
                                                          self.x,
                                                          self.y)
'''
class Platform(Entity):
    """ Encodes the state of a platform in the game """
    def __init__(self, height, width, x, y):
        super().__init__(int(x+width/2), int(y+height/2), ['blatform.png'], resize = (int(width), int(height)))
