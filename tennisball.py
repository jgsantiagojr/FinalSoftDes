import pygame
from math import cos, sin, pi, degrees, radians

pygame.init()

#game colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
turquoise = (0, 255, 255)
cottoncandy = (255, 179, 230)

# all_sprites = pygame.sprite.Group() #group to allow all sprites to be updated
# tennisballs = [] #list to enable multiple tennis balls to exist on screen


#initialize pygame and create window
width = 700
height = 700
fps = 20

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tennis Ball Machine")
pygame.mixer.init() #handles sound effects/music

clock = pygame.time.Clock()

class Machine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill(turquoise)

        self.rect = self.image.get_rect()

        self.rect.center = (width / 2, height /2)

# win.blit(win, (255, 0, 0), (self.x, self.y))

    def update(self, win):
        #restricted game bounds

        # win.blit(self.image, self.rect.center)
        win.blit(self.image, ((width / 2) - 20, (height / 2) - 25))

        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = width
        if self.rect.bottom > 0:
            self.rect.top = height
        if self.rect.top > height:
            self.rect.bottom = 0

class Shooterthing(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 100), pygame.SRCALPHA, 32)
        self.orig_image = self.image
        self.image.convert_alpha(self.image)

        self.image.fill(blue)

        self.rect = self.image.get_rect()

        self.rect.center = ((width / 2 + 5), (height / 2) + 50)
        # self.image.set_alpha(0)
        # self.image.fill(turquoise, self.rect)
        # self.image.set_colorkey(turquoise)


        self.pos = pygame.math.Vector2(self.rect.centerx, self.rect.top)
        self.angle = 0
        # self.rot_vel = radians(30)

        self.offset = pygame.math.Vector2(0, 50)
        self.trajectory = pygame.math.Vector2(cos(self.angle), sin(self.angle))

    def rotate(self):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, -self.angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        # self.rect = self.image.get_rect(center = (width / 2 + 5, height / 2 + 50))
        self.rect = self.image.get_rect(center = (self.pos + offset_rotated))

    def update(self, win):
        # self.angle += 1 * degrees(pi / 10)
        self.rotate()
        # win.blit(self.image, (width / 2, height / 2))


class Ball(object):
    def __init__(self, x, y, radius, color, trajectory):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = green
        self.trajectory = trajectory
        self.vel = trajectory * 7

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def main():
    #initialized values / runs only once when game is started

    all_sprites = pygame.sprite.Group() #group to allow all sprites to be updated
    tennisballs = [] #list to enable multiple tennis balls to exist on screen

    shooter = Shooterthing()
    machine = Machine()
    all_sprites.add(machine)
    all_sprites.add(shooter)
    shootloop = 0


    #game loop / no looping happens before here
    running = True

    while running:
        #process input (events)
        clock.tick(fps)

        if shootloop > 0:
            shootloop += 1
        if shootloop > 3:
            shootloop = 0

        trajectory = pygame.math.Vector2(cos(shooter.angle), sin(shooter.angle))

        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                running = False

        for ball in tennisballs:
            #if the bullet is within the x bounds of the screen, move it
            #otherwise, remove it from gameplay (pop)

            if ball.x < width and ball.x > 0:
                ball.x += ball.vel
            else:
                tennisballs.pop(tennisballs.index(ball))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]: #to be shot automatically
            if len(tennisballs) < 2:
                tennisballs.append(Ball(shooter.rect.top, shooter.rect.centery, 3, green, trajectory))
            shootloop += 1

        if keys[pygame.K_z]:
            # shooter.image, shooter.rect = rot_center(shooter.image, shooter.rect, shooter.angle)
            shooter.angle += 5

        if keys[pygame.K_c]:
            # shooter.image, shooter.rect = rot_center(shooter.image, shooter.rect, shooter.angle)
            shooter.angle -= 5

        #update
        win.fill(cottoncandy)
        all_sprites.update(win)
        shooter.update(win)

        #draw / render
        all_sprites.draw(win)


        for ball in tennisballs:
            ball.draw(win)

        # after drawing everything, flip (update) the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
