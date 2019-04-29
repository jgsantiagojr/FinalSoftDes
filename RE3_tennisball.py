import pygame
from math import cos, sin, pi, degrees, radians
from RagnarokEngine3 import RE3 as R
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
fps = 40

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

        # self.x = x
        # self.y = y
        #
        # self.width = width
        # self.height = height
        #
        # self.vel = 10
        #
        # self.isJump = False
        # self.left = False
        # self.right = False

# win.blit(win, (255, 0, 0), (self.x, self.y))

    def update(self, win):
        #restricted game bounds

        # win.blit(self.image, self.rect.center)
        win.blit(self.image, (width / 2 - 20, height / 2 - 25))

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

        self.image = pygame.Surface((10, 100))
        self.image.fill(blue)

        self.rect = self.image.get_rect()

        self.rect.center = (width, height + 50)

        self.angle = 1 * radians(pi / 20)
        self.rot_vel = radians(30)

    def update(self, win):
        win.blit(self.image, (width / 2, height / 2))

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

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# def redraw_game_window():
#     """Redraws the game window"""
#
#     win.fill(red)
#
#     all_sprites.draw(win)
#
#     for ball in tennisballs:
#         Ball.draw(win)
#     #after drawing everything, flip (update) the display
#     pygame.display.update()

def main():

    #initialized values / runs only once when game is started

    all_sprites = pygame.sprite.Group() #group to allow all sprites to be updated
    tennisballs = [] #list to enable multiple tennis balls to exist on screen

    machine = Machine()
    shooter = Shooterthing()
    all_sprites.add(shooter)
    all_sprites.add(machine)
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

        trajectory = (cos(shooter.angle), sin(shooter.angle))
        print(trajectory)

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
            # shooter.angle += shooter.rot_vel #exclusively for trajectory, not a visual
            # rotated_surface = shooter.image = pygame.transform.rotate(shooter.image, shooter.angle)
            # rect = rotated_surface.get_rect()
            # # rect.center = shooter.rect.center
            # win.blit(rotated_surface, (rect.center))
            # shooter.image = rot_center(shooter.image, shooter.angle)


        if keys[pygame.K_c]:
            # shooter.angle -= shooter.rot_vel #exclusively for trajectory, not a visual
            # rotated_surface = pygame.transform.rotate(shooter.image, -1 * shooter.angle)
            # rect = rotated_surface.get_rect()
            # # rect.center = shooter.rect.center
            # win.blit(rotated_surface, (rect.center))
            # shooter.image = rot_center(shooter.image, shooter.angle)


        #update
        win.fill(black)
        all_sprites.update(win)

        #draw / render
        all_sprites.draw(win)

        for ball in tennisballs:
            ball.draw(win)
            # win.blit(ball.image, (ball.x, ball.y))

        # after drawing everything, flip (update) the display
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()