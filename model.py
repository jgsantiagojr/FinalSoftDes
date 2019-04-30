from platform import Platform
from avatar import Avatar
from stage import Stage

size = (1920, 1080)
screenbottom = 980

bigboi = Stage((10000,10000),
               [Platform(40, 10000, 0, 9960),
                Platform(40, 1000, 500, 9800),
                Platform(40, 1000, 1000, 9600),
                Platform(40, 1000, 1500, 9400),
                Platform(40, 1000, 2000, 9200),
                Platform(40, 1000, 2500, 9000),
                Platform(40, 1000, 3000, 8800),
                Platform(40, 1000, 3500, 8600),
                Platform(40, 1000, 4000, 8400),
                Platform(40, 1000, 4500, 8200),
                Platform(40, 1000, 5000, 8000)])

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

AvatarImages = ['run/run_l1.png', 'run/run_l2.png',
                'run/run_l3.png', 'run/run_l4.png',
                'run/run_l5.png', 'run/run_l6.png',
                'run/run_l7.png', 'run/run_l8.png',
                'run/run_r1.png', 'run/run_r2.png',
                'run/run_r3.png', 'run/run_r4.png',
                'run/run_r5.png', 'run/run_r6.png',
                'run/run_r7.png', 'run/run_r8.png', ]
'''
class PlatformerModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size, clock):
        self.view_width = size[0]
        self.view_height = size[1]
        self.level = 0
        self.stages = [bigboi, ceiling2, pit1, pit3, ceiling1, pit2];

        self.avatar = Avatar(20, 20, 400, self.stages[0].size[1]-100, size)

        self.topleft = [self.avatar.x + self.avatar.width/2 - self.view_width/2, self.avatar.y + self.avatar.width/2 -self.view_width/2]

        self.clock = clock

    def update(self):
        """ Update the game state (currently only tracking the avatar) """

        #Update clock to allow for time-based physics calculations
        self.clock.tick()
        self.dt = self.clock.get_time()

        if len(self.avatar.inputs)<1:
            self.dt = self.dt*0.1

        #Update Avatar
        self.avatar.update(self.dt, self.stages[self.level])
        if 'QUIT' in self.avatar.inputs:
            return True

        if self.stages[self.level].completed:
            level += 1

        self.topleft = [self.avatar.x + self.avatar.width/2 - self.view_width/2, self.avatar.y + self.avatar.height/2 -self.view_height/2]

        if self.avatar.x+self.avatar.width/2-self.view_width/2<0:
            self.topleft[0] = 0
        elif self.avatar.x+self.avatar.width/2-self.view_width > self.stages[self.level].size[0]:
            self.topleft[0] = self.self.stages[self.level].size[0]-self.view_width

        if self.avatar.y + self.avatar.height/2 - self.view_height/2 < 0:
            self.topleft[1] = 0
        elif self.avatar.y+self.avatar.height/2-self.view_height > self.stages[self.level].height:
            self.topleft[1] = self.self.stages[self.level].height-self.view_height


    def __str__(self):
        output_lines = []
        # convert each platform to a string for outputting
        for platform in self.stages[self.level].platforms:
            output_lines.append(str(platform))
        output_lines.append(str(self.avatar))
        # print one item per line
        return "\n".join(output_lines)


'''
class PlatformerModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size, clock):
        self.view_width = size[0]
        self.view_height = size[1]
        self.level = 0
        self.stages = [bigboi, ceiling2, pit1, pit3, ceiling1, pit2];

        self.avatar = Avatar(400, 9000, AvatarImages, size)

        """
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemyprojectiles = pygame.sprite.Group()
        self.friendlyprojectiles = pygame.sprite.Group()

        for p in self.stages[0].platforms:
            self.platforms.add(p)

        for e in self.stages[0].enemies:
            self.enemies.add(e)
        """

        self.topleft = [self.avatar.x + self.avatar.width/2 - self.view_width/2, self.avatar.y + self.avatar.width/2 -self.view_width/2]

        self.clock = clock

    def update(self):
        """ Update the game state (currently only tracking the avatar) """

        #Update clock to allow for time-based physics calculations
        self.clock.tick()
        self.dt = self.clock.get_time()

        if len(self.avatar.inputs)<1:
            self.dt = self.dt*0.1

        #Update Avatar
        self.avatar.update(self.dt, self.stages[self.level])
        if 'QUIT' in self.avatar.inputs:
            return True

        if self.stages[self.level].completed:
            level += 1

            """
            for p in self.platforms:
                p.kill()
            for e in self.enemies:
                e.kill()
            for e in self.enemyprojectiles:
                e.kill()
            for f in self.friendlyprojectiles:
                f.kill()
            for p in self.stages[level].platforms:
                self.platforms.add(p)
            for e in self.stages[level].enemies:
                self.enemies.add(e)
            """


        self.topleft = [self.avatar.x + self.avatar.width/2 - self.view_width/2, self.avatar.y + self.avatar.height/2 -self.view_height/2]

        if self.avatar.x+self.avatar.width/2-self.view_width/2<0:
            self.topleft[0] = 0
        elif self.avatar.x+self.avatar.width/2-self.view_width > self.stages[self.level].width:
            self.topleft[0] = self.self.stages[self.level].width-self.view_width

        if self.avatar.y + self.avatar.height/2 - self.view_height/2 < 0:
            self.topleft[1] = 0
        elif self.avatar.y+self.avatar.height/2-self.view_height > self.stages[self.level].height:
            self.topleft[1] = self.self.stages[self.level].height-self.view_height

    #def draw(self):
        #self.stages[level].draw(self.topleft)
