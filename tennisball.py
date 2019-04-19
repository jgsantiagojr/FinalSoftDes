import pygame
from math import cos, sin
pygame.init()

#game colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
turquoise = (0, 255, 255)
cottoncandy = (255, 179, 230)


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

        self.image = pygame.Surface(10, 100))
        self.image.fill(cottoncandy)

        self.rect = self.image.get_rect()

        self.rect.bottom = (width / 2, height / 2)

        self.angle = -1 * (math.pi / 2)
        self.angle.speed = 5

    def update(self, win):


class ball(object):
    def __init__(self,x,y,radius,color, trajectory):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = green
        self.trajectory = trajectory
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redraw_game_window():
    """Redraws the game window"""

    win.fill(black)
    all_sprites.draw(win)

    for ball in tennisball:
        ball.draw(win)
    #after drawing everything, flip (update) the display
    pygame.display.flip()

def main():

    #initialized values / runs only once when game is started
    all_sprites = pygame.sprite.Group()
    machine = Machine()
    shooter = Shooterthing()
    all_sprites.add(machine)
    tennisballs = []

    #game loop / no looping happens before here
    running = True

    while running:
        #process input (events)
        clock.tick(fps)

        if shootloop > 0:
            shootloop += 1
        if shootloop > 3:
            shootloop = 0

        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                running = False

        for ball in tennisball:
            #if the bullet is within the x bounds of the screen, move it
            #otherwise, remove it from gameplay (pop)
            if ball.x < width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]: #to be shot automatically
            trajectory = pygame.Vector2(cos(shooter.rect.top), sin(shooter.rect.top))
            if len(tennisball) < 2:
                tennisballs.append(ball(shooter.rect.top, 3, green, trajectory))

        if keys[pygame.K_z]:
            pygame.transform.rotate(shooter.image, shooter.angle.speed, 1)

        if keys[pygame.K_c]:
            pygame.transform.rotate(shooter.image, -1 * shooter.angle.speeed, 1)

        #update
        all_sprites.update()

        #draw / render
        redraw_game_window()

    pygame.quit()

if __name__ == "__main__":
