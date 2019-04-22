import Pygame, math

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, images, group):
        pygame.sprite.Sprite.__init__(self, group)

        self.images = [pygame.image.load(i) for i in images]
        self.masks = [pygame.mask.from_surface(i) for i in self.images]

        for i in images):
            i.rect = i.get_bounding_rect

        self.frame = 0

        self.image = self.images[frame]
        self.mask = self.masks[frame]

        self.x = x
        self.y = y

    def update(self, dt):
        self.image = self.images[frame]
        self.mask = self.masks[frame]

        if frame < len(images):
            frame += 1
        else:
            frame = 0

    def draw(self, viewtopleft, screen):
        screen.blit(self.image, (self.x-viewtopleft[0], self.y-viewtopleft[1]))

class DynamicEntity(Entity):
    def __init__(self, x, y, images, group):
        super().__init__(x, y, images, group)

        self.xnew = x
        self.ynew = y
        self.vx = 0.0
        self.vy = 0.0
