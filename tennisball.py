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

        self.image = pygame.Surface((10, 100))
        self.image.fill(blue)

        self.rect = self.image.get_rect()

        self.rect.center = ((width / 2 + 5), (height / 2) + 50)

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


offset = pygame.math.Vector2(50, 0)

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

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

    shooter = Shooterthing()
    machine = Machine()
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

        trajectory = pygame.math.Vector2(cos(shooter.angle), sin(shooter.angle))
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

        print(type(shooter.image))
        if keys[pygame.K_x]: #to be shot automatically
            if len(tennisballs) < 2:
                tennisballs.append(Ball(shooter.rect.top, shooter.rect.centery, 3, green, trajectory))
            shootloop += 1

        if keys[pygame.K_z]:
            shooter.image = rotate(shooter.image, 5, shooter.rect.center, trajectory)

        if keys[pygame.K_c]:
            shooter.image = rotate(shooter.image, 5, shooter.rect.center, trajectory)

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
