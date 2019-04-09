from platform import Platform
from avatar import Avatar
from stage import Stage

size = (1920, 1080)
screenbottom = 980
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

class PlatformerModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size, clock):
        self.platforms = []
        self.view_width = size[0]
        self.view_height = size[1]
        self.level = 0
        self.stages = [ceiling2, pit1, pit3, ceiling1, pit2];
        self.update_platforms()

        self.avatar = Avatar(20, 20, 400, self.view_height - 650, size)
        self.clock = clock

    def update_platforms(self):
        #Generates platformer area from stages
        self.platforms = self.stages[self.level].platforms

    def update(self):
        """ Update the game state (currently only tracking the avatar) """

        #Update clock to allow for time-based physics calculations
        self.clock.tick()
        self.dt = self.clock.get_time()

        #Update Avatar
        self.avatar.update(self.dt, self.platforms)
        if 'QUIT' in self.avatar.inputs:
            return True

    def __str__(self):
        output_lines = []
        # convert each platform to a string for outputting
        for platform in self.platforms:
            output_lines.append(str(platform))
        output_lines.append(str(self.avatar))
        # print one item per line
        return "\n".join(output_lines)
