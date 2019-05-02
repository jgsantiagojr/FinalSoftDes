import pygame, math

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load(i) for i in images]
        self.masks = [pygame.mask.from_surface(i) for i in self.images]

        self.frame = 0

        self.image = self.images[self.frame]
        self.mask = self.masks[self.frame]

        self.x = x
        self.y = y

    def draw(self, viewtopleft, screen):
        screen.blit(self.image, (self.x-viewtopleft[0], self.y-viewtopleft[1]))

class DynamicEntity(Entity):
    def __init__(self, x, y, images ):
        super().__init__(x, y, images)

        self.xnew = x
        self.ynew = y
        self.vx = 0.0
        self.vy = 0.0
