import pygame

class Avatar(object):
    """ Encodes the state of the player's Avatar in the game """
    def __init__(self, height, width, x, y, screensize):
        """ Initialize an Avatar with the specified height, width,
            and position (x,y) """
        self.height = height
        self.width = width
        self.x = x
        self.y = y

        #xnew and ynew are a simple way of keeping track of
        #Avatar's future position to avoid overlap with obstacles
        self.xnew = x
        self.ynew = y
        self.vx = 0.0
        self.vy = 0.0

        #Sensitivity defines maximim speed for user controls
        self.sensitivity = 0.33
        self.inputs = []
        self.collisions = []
        self.screensize = screensize

    def addinput(self, input):
        '''Takes an input from the controller and adds it to the
        Avatar's list of inputs to handle'''
        if not input in self.inputs:
            self.inputs.append(input)

    def removeinput(self, input):
        '''Removes an input that has been handled from the Avatar's input stream'''
        if input in self.inputs:
            self.inputs.remove(input)

    def controls(self):
        '''Handles inputs from the aavatar's list for input controls, accounting for collisions'''
        if 'LEFT' in self.inputs and 'RIGHT' in self.inputs:
            self.vx = 0
        elif 'LEFT' in self.inputs:
            if not 'LEFT' in self.collisions:
                self.vx = -self.sensitivity
            else:
                self.vy = self.vy * 0.75
        elif 'RIGHT' in self.inputs:
            if not 'RIGHT' in self.collisions:
                self.vx = self.sensitivity
            else:
                self.vy = self.vy * 0.75
        else:
            self.vx = 0
        if 'JUMP' in self.inputs:
            #Normal Jumping
            if 'BOTTOM' in self.collisions:
                self.collisions.remove('BOTTOM')
                self.vy = -1.25
            #Wall Jumping
            elif 'LEFT' in self.collisions:
                self.collisions.remove('LEFT')
                self.vy = -1.25
                self.vx = self.sensitivity * 2
            elif 'RIGHT' in self.collisions:
                self.collisions.remove('RIGHT')
                self.vy = -1.25
                self.vx = -self.sensitivity * 2
            #Dropping down from ceiling
            elif 'TOP' in self.collisions:
                self.collisions.remove('TOP')
                self.vy+=.002

    def check_collisions(self, dt, platforms):
        '''Checks for collisions between the avatar and the platforms, and attempts to resolve them'''

        #Update xnew and ynew to predict collisions
        self.xnew = self.x + self.vx*dt
        self.ynew = self.y + self.vy*dt

        #Sweep through all platforms
        for p in platforms:
            #Check lateral overlap with platforms
            if p.x <= self.xnew+self.width and self.width+self.xnew <= p.x+p.width:
                #Check intersection between platform and avatar
                if self.ynew+self.height >= p.y and p.y >= self.ynew:
                    #Update Collisions
                    self.collisions.append('BOTTOM')
                    #Correct ynew to avoid overlap
                    self.ynew = p.y-self.height
                    #Stop Motion
                    self.vx = 0
                    self.vy = 0
                elif self.ynew <= p.y+p.height and p.y+p.height <= self.ynew+self.height:
                    self.collisions.append('TOP')
                    self.ynew = p.y+p.height
                    self.vx = 0
                    self.vy = 0
            #Check longitudinal overlap with platforms
            if p.y < self.ynew+self.height+self.vy*dt and self.ynew+self.vy*dt < p.y+p.height:
                if self.x+self.vx*dt <= p.x+p.width and p.x+p.width <= self.x+self.width+self.vx*dt:
                    self.collisions.append('LEFT')
                    self.xnew = p.x+p.width
                    self.vx = 0
                    self.vy = 0
                elif self.x+self.width+self.vx*dt >= p.x and p.x >= self.x+self.vx*dt:
                    self.collisions.append('RIGHT')
                    self.xnew = p.x-self.width
                    self.vx = 0
                    self.vy = 0

    def resolve_collisions(self):
        '''Resolves collisions between Avatar and platforms'''
        if 'LEFT' in self.collisions or 'RIGHT' in self.collisions:
            self.x = self.xnew
        if 'TOP' in self.collisions or 'BOTTOM' in self.collisions:
            self.y = self.ynew


    def update(self, dt, platforms):
        """ update the position of the Avatar while taking physics, collisions, and controls into account"""
        self.collisions = []
        self.check_collisions(dt, platforms)

        #prevents avatar from leaving bottom of the stage
        if self.y+self.vy*dt > 1080-self.height:
            self.collisions.append('BOTTOM')
            self.ynew = 1080-self.height
            self.vy = 0

        #update avatar position
        self.x = self.xnew
        self.y = self.ynew

        self.controls()
        self.resolve_collisions()

        #Gravity (Slower when haning on wall)
        if ('LEFT' in self.collisions and 'LEFT' in self.inputs) or ('RIGHT' in self.collisions and 'RIGHT' in self.inputs):
            self.vy += 0.0002 * dt
        elif not ('TOP' in self.collisions or 'BOTTOM' in self.collisions):
            self.vy += 0.002 * dt

        #Prevent avatar from leaving the display area
        if self.x < 0:
            self.x = 0
        if self.x > self.screensize[0]-self.width:
            self.x = self.screensize[0]-self.width



    def __str__(self):
        return "Avatar height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                           self.width,
                                                           self.x,
                                                           self.y)
