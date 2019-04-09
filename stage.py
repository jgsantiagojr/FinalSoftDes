class Stage(object):
    def __init__(self, size, platforms):
        '''Generates a Stage object from a list of platforms'''
        self.platforms = platforms
        self.width = size[0]
        self.height = size[1]
