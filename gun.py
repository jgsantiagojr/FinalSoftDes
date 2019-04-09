import pygame

class gun(object):

    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle

    def __str__(self):
        return "Gun height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                           self.width,
                                                           self.x,
                                                           self.y)

    def shoot(self):

    def attack(self, attacking):
        if attacking :
            self.shoot()
