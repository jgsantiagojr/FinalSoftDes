import pygame, math

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, images, resize = False):
        """Generates an Entity object

        x: x coordinate of center of Sprite
        y: y coordinate of center of sprite
        images: list of strings corresponding to bitmapped images to be loaded

        returns: Entity Object
        """

        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load(i) for i in images]
        if resize:
            for i in range(len(self.images)):
                self.images[i] = pygame.transform.smoothscale(self.images[i],resize)
        self.masks = [pygame.mask.from_surface(i) for i in self.images]
        self.rects = [pygame.Surface.get_bounding_rect(i) for i in self.images]
        for r in self.rects:
            r.center = (x,y)

        self.frame = 0

        self.x = x
        self.y = y

    def contains_point(self, point):
        if self.x - self.width()/2 < point[0] and point[0] < self.x + self.width()/2:
            if self.y - self.height()/2 < point[1] and point[1] < self.y + self.height()/2:
                return True
        return False

    def image(self):
        return self.images[self.frame]

    def mask(self):
        return self.masks[self.frame]

    def rect(self):
        self.rects[self.frame].center = (self.x, self.y)
        return self.rects[self.frame]

    def height(self):
        return self.rects[self.frame].height

    def width(self):
        return self.rects[self.frame].width

    def left(self):
        return self.x - self.rects[self.frame].width/2

    def right(self):
        return self.x + self.rects[self.frame].width/2

    def top(self):
        return self.y - self.rects[self.frame].height/2

    def bottom(self):
        return self.y + self.rects[self.frame].height/2

    def draw(self, camera, screen):
        """
        Draws an entity relative to the camera's center,
        trusting that the camera will be positioned properly
        """



        screen.blit(self.image(), (self.left()-camera.left, self.top()-camera.top))

class DynamicEntity(Entity):
    def __init__(self, x, y, images ):
        super().__init__(x, y, images)

        self.xnew = x
        self.ynew = y
        self.vx = 0.0
        self.vy = 0.0
