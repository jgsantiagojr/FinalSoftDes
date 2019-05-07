class Stage(object):
    def __init__(self, size, platforms, enemies = [], spawnpoint = [], backgrounds = [], exitpoint = []):
        '''Generates a Stage object from a list of platforms'''
        self.size = size
        self.platforms = platforms
        self.exitpoint = exitpoint
        self.spawnpoint = spawnpoint
        self.enemies = enemies
        self.backgrounds = backgrounds
        self.width = size[0]
        self.height = size[1]
        self.died = False
        self.completed = False

    def contains_point(self, point):
        if 0 < point[0] and point[0] < self.width:
            if 0 < point[1] and point[1] < self.height:
                return True
        return False
