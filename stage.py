class Stage(object):
    def __init__(self, size, platforms, enemies = [], spawnpoint = [], backgrounds = []):
        '''Generates a Stage object from a list of platforms'''
        self.size = size
        self.platforms = platforms
        self.enemies = enemies
        self.backgrounds = backgrounds
        self.width = size[0]
        self.height = size[1]
        self.died = False
        self.completed = False
