import pygame
from entity import Entity, DynamicEntity
"""
class Avatar(object):
    ''' Encodes the state of the player's Avatar in the game '''
    def __init__(self, height, width, x, y, screensize):
        ''' Initialize an Avatar with the specified height, width,
            and position (x,y) '''
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


    def update(self, dt, stage):
        ''' update the position of the Avatar while taking physics, collisions, and controls into account'''
        self.collisions = []

        self.check_collisions(dt, stage.platforms)

        #prevents avatar from leaving bottom of the stage
        if self.y+self.vy*dt > stage.height-self.height:
            self.collisions.append('BOTTOM')
            self.ynew = stage.height-self.height
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
        if self.x > stage.width-self.width:
            self.x = stage.width-self.width



    def __str__(self):
        return "Avatar height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                           self.width,
                                                           self.x,
                                                           self.y)

"""
class Avatar(DynamicEntity):
    def __init__(self, x, y, images, screensize):
        ''' Initialize an Avatar with the specified height, width,
            and position (x,y) '''

        super().__init__(x, y, images)

        #Sensitivity defines maximim speed for user controls
        self.sensitivity = 1
        self.inputs = []
        self.collisions = []
        self.movement = 'RUN'
        self.screensize = screensize

        #A dictionary in which the image indicies containing the first frame of different movement cycles are stored
        self.move_frames = {'RUN LEFT': (0,8,1000),
                            'RUN RIGHT': (8,8,1000)}

        self.frame = 8
        self.frame_time = 0

        self.width = self.images[self.frame].get_bounding_rect().width
        self.height = self.images[self.frame].get_bounding_rect().height

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

    '''
    def check_collisions(self, dt, platforms):
        #Update xnew and ynew to predict collisions
        self.xnew = self.x + self.vx*dt
        self.ynew = self.y + self.vy*dt

        #Sweep through all platforms
        for p in platforms:
            ox = int(p.x-self.xnew)
            oy = int(p.y-self.ynew)
            print(self.mask.overlap_area(p.mask, (ox, oy)))
            if self.mask.overlap_area(p.mask, (ox, oy))>0:
                #Stop Motion
                self.vx = 0
                self.vy = 0

                dx = self.mask.overlap_area(p.mask,(ox+1,oy)) - self.mask.overlap_area(p.mask,(ox-1,oy))
                dy = self.mask.overlap_area(p.mask,(ox,oy+1)) - self.mask.overlap_area(p.mask,(ox,oy-1))
                if dx == 0:
                    if dy<0:
                        #Update Collisions
                        self.collisions.append('BOTTOM')
                        #Correct ynew to avoid overlap
                        self.ynew = p.y-self.height
                    else:
                        self.collisions.append('TOP')
                        self.ynew = p.y+p.height
                elif dy == 0:
                    if dx<0:
                        self.collisions.append('RIGHT')
                        self.xnew = p.x-self.width
                    else:
                        self.collisions.append('LEFT')
                        self.xnew = p.x+p.width
                else:
                    if self.y + self.height > p.y and self.vy < 0 or self.y < p.y+p.height and self.vy > 0:
                        if dx<0:
                            self.collisions.append('RIGHT')
                            self.xnew = p.x-self.width
                        else:
                            self.collisions.append('LEFT')
                            self.xnew = p.x+p.width
                    elif self.x+self.width > p.x and self.vx < 0 or self.x < p.x+p.width and self.vx > 0:
                        if dy<0:
                            #Update Collisions
                            self.collisions.append('BOTTOM')
                            #Correct ynew to avoid overlap
                            self.ynew = p.y-self.height
                        else:
                            self.collisions.append('TOP')
                            self.ynew = p.y+p.height
    '''

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

    def cycle_frames(self, dt):
        cycle_index = self.move_frames[self.movement + ' ' + self.inputs[0]][0]
        cycle_length = self.move_frames[self.movement + ' ' + self.inputs[0]][1]
        cycle_time = self.move_frames[self.movement + ' ' + self.inputs[0]][2]
        self.frame_time += dt
        self.frame_time = self.frame_time % cycle_time
        self.frame = cycle_index + (self.frame_time*cycle_length)//cycle_time

    def update(self, dt, stage):
        ''' update the position of the Avatar while taking physics, collisions, and controls into account'''
        self.image = self.images[self.frame]
        self.mask = self.masks[self.frame]

        self.width = self.images[self.frame].get_bounding_rect().width
        self.height = self.images[self.frame].get_bounding_rect().height

        self.collisions = []

        self.check_collisions(dt, stage.platforms)

        #prevents avatar from leaving bottom of the stage
        if self.y+self.vy*dt > stage.height-self.height:
            self.collisions.append('BOTTOM')
            self.ynew = stage.height-self.height
            self.vy = 0

        #update avatar position
        self.x = self.xnew
        self.y = self.ynew

        if len(self.inputs)>0:
            if self.inputs[0]=='LEFT' or self.inputs[0]=='RIGHT':
                self.cycle_frames(dt)
            else:
                self.frame_time = 0
                self.frame = self.frame - self.frame%8

            self.controls()
        else:
            self.vx = 0

        #Gravity (Slower when haning on wall)
        if ('LEFT' in self.collisions and 'LEFT' in self.inputs) or ('RIGHT' in self.collisions and 'RIGHT' in self.inputs):
            self.vy += 0.002 * dt
        elif not ('TOP' in self.collisions or 'BOTTOM' in self.collisions):
            self.vy += 0.005 * dt

        #Prevent avatar from leaving the display area
        if self.x < 0:
            self.x = 0
        if self.x > stage.width-self.width:
            self.x = stage.width-self.width
