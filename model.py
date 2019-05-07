from platform import Platform
from avatar import Avatar
from stage import Stage
from enemy import StaticEnemy
from entity import Entity, DynamicEntity
import pygame

size = (1920, 1080)
screenbottom = 980


AvatarImages = ['Sprites/jump_l/jump_l1.png', 'Sprites/jump_l/jump_l2.png',
                'Sprites/jump_l/jump_l3.png', 'Sprites/jump_l/jump_l4.png',
                'Sprites/jump_l/jump_l5.png', 'Sprites/jump_r/jump_r1.png',
                'Sprites/jump_r/jump_r2.png', 'Sprites/jump_r/jump_r3.png',
                'Sprites/jump_r/jump_r4.png', 'Sprites/jump_r/jump_r5.png',
                'Sprites/run_l/run_l1.png', 'Sprites/run_l/run_l2.png',
                'Sprites/run_l/run_l3.png', 'Sprites/run_l/run_l4.png',
                'Sprites/run_l/run_l5.png', 'Sprites/run_l/run_l6.png',
                'Sprites/run_l/run_l7.png', 'Sprites/run_l/run_l8.png',
                'Sprites/run_l/run_l9.png', 'Sprites/run_l/run_l10.png',
                'Sprites/run_r/run_r1.png', 'Sprites/run_r/run_r2.png',
                'Sprites/run_r/run_r3.png', 'Sprites/run_r/run_r4.png',
                'Sprites/run_r/run_r5.png', 'Sprites/run_r/run_r6.png',
                'Sprites/run_r/run_r7.png', 'Sprites/run_r/run_r8.png',
                'Sprites/run_r/run_r9.png', 'Sprites/run_r/run_r10.png',
                'Sprites/standing_l/standing_l.png',
                'Sprites/standing_r/standing_r.png',
                'Sprites/run_l/run_l1t1.png', 'Sprites/run_l/run_l2t1.png',
                'Sprites/run_l/run_l3t1.png', 'Sprites/run_l/run_l4t1.png',
                'Sprites/run_l/run_l5t1.png', 'Sprites/run_l/run_l6t1.png',
                'Sprites/run_l/run_l7t1.png', 'Sprites/run_l/run_l8t1.png',
                'Sprites/run_l/run_l9t1.png', 'Sprites/run_l/run_l10t1.png',
                'Sprites/run_r/run_r1t1.png', 'Sprites/run_r/run_r2t1.png',
                'Sprites/run_r/run_r3t1.png', 'Sprites/run_r/run_r4t1.png',
                'Sprites/run_r/run_r5t1.png', 'Sprites/run_r/run_r6t1.png',
                'Sprites/run_r/run_r7t1.png', 'Sprites/run_r/run_r8t1.png',
                'Sprites/run_r/run_r9t1.png', 'Sprites/run_r/run_r10t1.png',
                'Sprites/standing_l/standing_lt1.png',
                'Sprites/standing_r/standing_rt1.png',
                'Sprites/run_l/run_l1t2.png', 'Sprites/run_l/run_l2t2.png',
                'Sprites/run_l/run_l3t2.png', 'Sprites/run_l/run_l4t2.png',
                'Sprites/run_l/run_l5t2.png', 'Sprites/run_l/run_l6t2.png',
                'Sprites/run_l/run_l7t2.png', 'Sprites/run_l/run_l8t2.png',
                'Sprites/run_l/run_l9t2.png', 'Sprites/run_l/run_l10t2.png',
                'Sprites/run_r/run_r1t2.png', 'Sprites/run_r/run_r2t2.png',
                'Sprites/run_r/run_r3t2.png', 'Sprites/run_r/run_r4t2.png',
                'Sprites/run_r/run_r5t2.png', 'Sprites/run_r/run_r6t2.png',
                'Sprites/run_r/run_r7t2.png', 'Sprites/run_r/run_r8t2.png',
                'Sprites/run_r/run_r9t2.png', 'Sprites/run_r/run_r10t2.png',
                'Sprites/standing_l/standing_lt2.png',
                'Sprites/standing_r/standing_rt2.png',
                'Sprites/run_l/run_l1t3.png', 'Sprites/run_l/run_l2.png',
                'Sprites/run_l/run_l3t3.png', 'Sprites/run_l/run_l4.png',
                'Sprites/run_l/run_l5t3.png', 'Sprites/run_l/run_l6.png',
                'Sprites/run_l/run_l7t3.png', 'Sprites/run_l/run_l8.png',
                'Sprites/run_l/run_l9t3.png', 'Sprites/run_l/run_l10.png',
                'Sprites/run_r/run_r1t3.png', 'Sprites/run_r/run_r2.png',
                'Sprites/run_r/run_r3t3.png', 'Sprites/run_r/run_r4.png',
                'Sprites/run_r/run_r5t3.png', 'Sprites/run_r/run_r6.png',
                'Sprites/run_r/run_r7t3.png', 'Sprites/run_r/run_r8.png',
                'Sprites/run_r/run_r9t3.png', 'Sprites/run_r/run_r10.png',
                'Sprites/standing_l/standing_lt3.png',
                'Sprites/standing_r/standing_rt3.png']

StaticEnemyImages = ['Sprites/standing_l/redstanding_l.png',
               'Sprites/standing_r/redstanding_r.png',
               'Sprites/standing_l/redstanding_lt1.png',
               'Sprites/standing_r/redstanding_rt1.png',
               'Sprites/standing_l/redstanding_lt2.png',
               'Sprites/standing_r/redstanding_rt2.png',
               'Sprites/standing_l/redstanding_lt3.png',
               'Sprites/standing_r/redstanding_rt3.png']

BulletImages = ['bullet.png']

ShurikenImages = ['Sprites/shruiken/shruiken_1.png',
                  'Sprites/shruiken/shruiken_2.png',
                  'Sprites/shruiken/shruiken_3.png',
                  'Sprites/shruiken/shruiken_4.png',
                  'Sprites/shruiken/shruiken_5.png',
                  'Sprites/shruiken/shruiken_6.png',
                  'Sprites/shruiken/shruiken_7.png',
                  'Sprites/shruiken/shruiken_8.png']

TitleImages = ['title-screen.png']

bigboi = Stage((10000,10200),
               [Platform(200, 10000, 0, 9960),
                Platform(200, 1000, 500, 9800),
                Platform(200, 1000, 1000, 9600),
                Platform(200, 1000, 1500, 9400),
                Platform(200, 1000, 2000, 9200),
                Platform(200, 1000, 2500, 9000),
                Platform(200, 1000, 3000, 8800),
                Platform(200, 1000, 3500, 8600),
                Platform(200, 1000, 4000, 8400),
                Platform(200, 1000, 4500, 8200),
                Platform(200, 1000, 5000, 8000),
                Platform(9900, 1000, 5000, 200)],
                [StaticEnemy(550, 9500,StaticEnemyImages, BulletImages),
                 StaticEnemy(650, 9500,StaticEnemyImages, BulletImages),
                 StaticEnemy(750, 9500,StaticEnemyImages, BulletImages),
                 StaticEnemy(850, 9500,StaticEnemyImages, BulletImages),
                 StaticEnemy(950, 9500,StaticEnemyImages, BulletImages)])

pit1 = Stage(size,
[Platform(40,size[0]/2,0,screenbottom),
Platform(40,size[0]/2,1200,screenbottom)]
)

pit2 = Stage(size,
[Platform(40,200,200,screenbottom),
Platform(40,200,400,screenbottom),
Platform(40,200,800,screenbottom)]
)

pit3 = Stage(size,
[Platform(40,200,0,screenbottom),
Platform(40,200,400,screenbottom-300),
Platform(300,40,600,screenbottom-700),
Platform(40,200,1000,screenbottom-700),
Platform(100,40,600,screenbottom-900),
Platform(600,40,1200,screenbottom-700),
Platform(40,300,1200,screenbottom-200)]
)

ceiling1 = Stage(size,
[Platform(40,200,0,screenbottom),
Platform(800,1600,0,0),
Platform(40,200,1600,screenbottom)]
)

ceiling2 = Stage(size,
[Platform(40,200,0,screenbottom),
Platform(400,1600,0,0),
Platform(240,40,200,screenbottom-200),
Platform(200,40,0,screenbottom-600),
Platform(40,200,1600,screenbottom)]
)

class Camera(object):
    def __init__(self, centerx, centery, size):
        self.x = centerx
        self.y = centery
        self.width = size[0]
        self.height = size[1]
        self.left = centerx-size[0]/2
        self.right = centerx+size[0]/2
        self.top = centery-size[1]/2
        self.bottom = centery-size[1]/2

    def update(self, centerx, centery, stage):
        #corrects view window for camera tracking
        self.x = centerx
        self.y = centery
        self.left = centerx-self.width/2
        self.right = centerx+self.width/2
        self.top = centery-self.height/2
        self.bottom = centery+self.height/2

        if centerx - self.width/2 < 0:
            self.left = 0
            self.x = self.width/2
            self.right = self.x+self.width/2
        elif centerx + self.width/2 > stage.width:
            self.right = stage.width
            self.x = stage.width-self.width/2
            self.left = self.x-self.width/2

        if centery - self.height/2 < 0:
            self.top = 0
            self.y = self.height/2
            self.bottom = self.height
        elif centery + self.height/2 > stage.height:
            self.bottom = stage.height
            self.y = stage.height - self.height/2
            self.top = stage.height-self.height

    def rect(self):

        return pygame.Rect((self.left,self.top), (self.width, self.height))

class PlatformerModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size, clock):
        self.view_width = size[0]
        self.view_height = size[1]
        self.level = 0
        self.stages = [bigboi, ceiling2, pit1, pit3, ceiling1, pit2];
        self.pictures = []

        self.dead = False
        self.avatar = Avatar(400, 9000, AvatarImages, ShurikenImages, size)
        self.avatar_group = pygame.sprite.GroupSingle(self.avatar)

        self.enemies = pygame.sprite.Group()
        for e in self.stages[self.level].enemies:
            self.enemies.add(e)

        self.platforms = pygame.sprite.Group()
        for p in self.stages[self.level].platforms:
            self.platforms.add(p)

        self.enemy_projectiles = pygame.sprite.Group()

        self.friendly_projectiles = pygame.sprite.Group()

        self.camera = Camera(self.avatar.x,self.avatar.y, size)

        self.clock = clock

    def reset(self):
        self.dead = False
        self.avatar = Avatar(400, 9000, AvatarImages, ShurikenImages, size)
        self.avatar_group = pygame.sprite.GroupSingle(self.avatar)

        self.enemies = pygame.sprite.Group()
        for e in self.stages[self.level].enemies:
            self.enemies.add(e)

        self.platforms = pygame.sprite.Group()
        for p in self.stages[self.level].platforms:
            self.platforms.add(p)

        self.enemy_projectiles = pygame.sprite.Group()

        self.friendly_projectiles = pygame.sprite.Group()

    def contains_point(self, point):
        if 0 < point[0] and point[0] < self.width():
            if 0 < point[1] and point[1] < self.height():
                return True
        return False

    def stage(self):
        return self.stages[self.level]

    def width(self):
        return self.stages[self.level].width

    def height(self):
        return self.stages[self.level].height

    def update(self):
        """ Update the game state (currently only tracking the avatar) """

        #Update clock to allow for time-based physics calculations
        self.clock.tick()
        self.dt = self.clock.get_time()

        if len(self.avatar.inputs)<1:
            self.dt = self.dt*0.1

        #Update Avatar
        self.avatar.update(self.dt, self.stage(), self.friendly_projectiles)
        if 'QUIT' in self.avatar.inputs:
            return True

        self.enemies.update(self.avatar, self.stage(), self.enemy_projectiles, self.dt)

        self.enemy_projectiles.update(self.dt, self.stage())
        self.friendly_projectiles.update(self.dt, self.stage())

        pygame.sprite.groupcollide(self.platforms, self.friendly_projectiles, False, True, collided = pygame.sprite.collide_rect_ratio(1))

        pygame.sprite.groupcollide(self.enemies, self.friendly_projectiles, True, True, collided = pygame.sprite.collide_rect_ratio(.95))

        if pygame.sprite.groupcollide(self.avatar_group, self.enemy_projectiles, False, True, collided = pygame.sprite.collide_rect_ratio(.75)):
            self.dead = True

        pygame.sprite.groupcollide(self.platforms, self.enemy_projectiles, False, True, collided = pygame.sprite.collide_rect_ratio(1))



        if self.stages[self.level].completed:
            level += 1


        self.camera.update(self.avatar.x, self.avatar.y, self.stage())



    #def draw(self):
        #self.stages[level].draw(self.topleft)
