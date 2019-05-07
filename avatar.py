import pygame
from entity import Entity, DynamicEntity
from pygame import Vector2
from bullets import Projectile, Shuriken

class Avatar(DynamicEntity):
    def __init__(self, x, y, images, weaponimages, screensize):
        ''' Initialize an Avatar with the specified height, width,
            and position (x,y) '''

        super().__init__(x, y, images)

        #Sensitivity defines maximim speed for user controls
        self.sensitivity = 1
        self.inputs = []
        self.collisions = []
        self.movement = 'RUN'
        self.facing = 'RIGHT'
        self.screensize = screensize

        self.weaponimages = weaponimages
        self.cooldown = 100
        self.shot_clock = 0
        self.attacking = False
        self.shoot = False
        self.trajectory = Vector2(1,0)

        #A dictionary in which the image indicies containing the first frame of different movement cycles are stored
        self.move_frames = {'JUMP LEFT': (0,5,200),
                            'JUMP RIGHT': (5,5,200),
                            'RUN LEFT': (10,10,1000),
                            'RUN RIGHT': (20,10,1000),
                            'STANDING LEFT': (30,1,1),
                            'STANDING RIGHT': (31,1,1)}

        self.frame = 30
        self.frame_time = 0

        self.handpos = Vector2(self.x,self.y)



    def addinput(self, input):
        '''Takes an input from the controller and adds it to the
        Avatar's list of inputs to handle'''
        if not input in self.inputs:
            self.inputs.append(input)

    def removeinput(self, input):
        '''Removes an input that has been handled from the Avatar's input stream'''
        if input in self.inputs:
            self.inputs.remove(input)

    def controls(self, dt):
        '''Handles inputs from the aavatar's list for input controls, accounting for collisions'''
        if 'LEFT' in self.inputs and 'RIGHT' in self.inputs:
            self.vx = 0
            if 'BOTTOM' in self.collisions:
                if not (self.movement == 'JUMP' or self.movement == 'RUN'):
                    self.movement = 'STANDING'
                    self.frame_time = 0
        elif 'LEFT' in self.inputs:
            self.facing = 'LEFT'
            self.trajectory = Vector2(-1,0)
            if 'BOTTOM' in self.collisions:
                if not (self.movement == 'JUMP' or self.movement == 'RUN'):
                    self.movement = 'RUN'
                    self.frame_time = 0
            if not 'LEFT' in self.collisions:
                self.vx = -self.sensitivity
            else:
                self.vy = self.vy * 0.75
        elif 'RIGHT' in self.inputs:
            self.facing = 'RIGHT'
            self.trajectory = Vector2(1,0)
            if 'BOTTOM' in self.collisions:
                if not (self.movement == 'JUMP' or self.movement == 'RUN'):
                    self.movement = 'RUN'
                    self.frame_time = 0
            if not 'RIGHT' in self.collisions:
                self.vx = self.sensitivity
            else:
                self.vy = self.vy * 0.75
        else:
            self.vx = 0
            if 'BOTTOM' in self.collisions:
                if not (self.movement == 'JUMP' or self.movement == 'RUN'):
                    self.movement = 'STANDING'
                    self.frame_time = 0
        if 'JUMP' in self.inputs:
            #Normal Jumping
            if 'BOTTOM' in self.collisions:
                self.movement = 'JUMP'
                self.frame_time = 0
                self.shot_clock = self.cooldown + 1
                self.collisions.remove('BOTTOM')
                self.vy = -3
            #Wall Jumping
            elif 'LEFT' in self.collisions:
                self.movement = 'JUMP'
                self.frame_time = 0
                self.shot_clock = self.cooldown + 1
                self.facing = 'RIGHT'
                self.trajectory = Vector2(1,0)
                print(self.movement + ' ' + self.facing)
                self.collisions.remove('LEFT')
                self.vy = -1.25
                self.vx = self.sensitivity * 2
            elif 'RIGHT' in self.collisions:
                self.movement = 'JUMP'
                self.frame_time = 0
                self.shot_clock = self.cooldown + 1
                self.facing = 'LEFT'
                self.trajectory = Vector2(-1,0)
                self.collisions.remove('RIGHT')
                self.vy = -1.25
                self.vx = -self.sensitivity * 2
            #Dropping down from ceiling
            elif 'TOP' in self.collisions:
                self.collisions.remove('TOP')
                self.vy+=.002
        #Gravity (Slower when haning on wall)
        if ('LEFT' in self.collisions and 'LEFT' in self.inputs) or ('RIGHT' in self.collisions and 'RIGHT' in self.inputs):
            self.vy += 0.0005 * dt
        elif not ('TOP' in self.collisions or 'BOTTOM' in self.collisions):
            self.vy += 0.005 * dt
        if 'ATTACK' in self.inputs:
            self.movement = 'STANDING'

            if self.shot_clock > self.cooldown:
                self.shot_clock = 0
                self.attacking = True
                self.shoot = True
            else:
                self.shoot = False


    def check_collisions(self, dt, stage):
        '''Checks for collisions between the avatar and the platforms, and attempts to resolve them'''

        #Update xnew and ynew to predict collisions
        newcenter = (self.x + self.vx*dt, self.y + self.vy*dt)
        self.xnew = newcenter[0]
        self.ynew = newcenter[1]
        leftnew = self.left() + self.vx*dt
        rightnew = self.right() + self.vx*dt
        topnew = self.top() + self.vy*dt
        bottomnew = self.bottom() + self.vy*dt

        #Sweep through all platforms
        for p in stage.platforms:
            #Check lateral overlap with platforms
            if p.contains_point((leftnew,bottomnew)) and p.contains_point((rightnew,bottomnew)):
                if self.movement == 'JUMP' and self.frame%5 == 2:
                    self.frame += 1
                    self.frame_time += 1+self.move_frames['JUMP '+self.facing][2]//self.move_frames['JUMP '+self.facing][1]
                if not 'BOTTOM' in self.collisions:
                    self.collisions.append('BOTTOM')
                #Correct ynew to avoid overlap
                bottomnew = p.top()
                self.ynew = p.top() - self.height()/2
                topnew = p.top() - self.height()
                #Stop Motion
                self.vy = 0
            elif p.contains_point((leftnew,topnew)) and p.contains_point((rightnew,topnew)):
                if not 'TOP' in self.collisions:
                    self.collisions.append('TOP')
                topnew = p.bottom() + 0.01
                self.ynew = p.bottom() + 0.01 + self.height()/2
                bottomnew = p.bottom() + 0.01 + self.height()
                self.vy = 0
            #Check longitudinal overlap with platforms
            elif p.contains_point((rightnew,topnew)) and p.contains_point((rightnew,bottomnew)):
                if not 'RIGHT' in self.collisions:
                    self.collisions.append('RIGHT')
                rightnew = p.left()
                self.xnew = p.left() - self.width()/2
                leftnew = p.left() - self.width()
                self.vx = 0
            elif p.contains_point((leftnew,topnew)) and p.contains_point((leftnew,bottomnew)):
                if not 'LEFT' in self.collisions:
                    self.collisions.append('LEFT')
                leftnew = p.right()
                self.xnew = p.right() + self.width()/2
                rightnew = p.right() + self.width()
                self.vx = 0
            if p.contains_point(((rightnew,topnew))):
                if not 'RIGHT' in self.collisions:
                    self.collisions.append('RIGHT')
                rightnew = p.left()
                self.xnew = p.left() - self.width()/2
                leftnew = p.left() - self.width()
                self.vx = 0
            elif p.contains_point((leftnew,topnew)):
                if not 'LEFT' in self.collisions:
                    self.collisions.append('LEFT')
                leftnew = p.right()
                self.xnew = p.right() + self.width()/2
                rightnew = p.right() + self.width()
                self.vx = 0
            elif p.contains_point((leftnew,bottomnew)) or p.contains_point((rightnew,bottomnew)):
                if self.movement == 'JUMP' and self.frame%5 == 2:
                    self.frame += 1
                if not 'BOTTOM' in self.collisions:
                    self.collisions.append('BOTTOM')
                #Correct ynew to avoid overlap
                bottomnew = p.top()
                self.ynew = p.top() - self.height()/2
                topnew = p.top() - self.height()
                #Stop Motion
                self.vy = 0

        #prevents avatar from leaving bottom of the stage
        if bottomnew > stage.height:
            if not 'BOTTOM' in self.collisions:
                self.collisions.append('BOTTOM')
            self.ynew = stage.height-self.height()/2
            self.vy = 0

    def cycle_frames(self, dt):
        cycle_index = self.move_frames[self.movement + ' ' + self.facing][0]
        cycle_length = self.move_frames[self.movement + ' ' + self.facing][1]
        cycle_time = self.move_frames[self.movement + ' ' + self.facing][2]
        if self.movement == 'RUN':
            self.frame_time += dt
            if self.frame_time > cycle_time:
                self.movement = 'STANDING'
                self.frame_time = 0
                cycle_index = self.move_frames[self.movement + ' ' + self.facing][0]
                cycle_length = self.move_frames[self.movement + ' ' + self.facing][1]
                cycle_time = self.move_frames[self.movement + ' ' + self.facing][2]
            self.frame_time = self.frame_time % cycle_time
            self.frame = int(cycle_index + (self.frame_time*cycle_length)//cycle_time)
        elif self.movement == 'JUMP':
            self.attacking = False
            if self.frame%cycle_length < 2 or 2 < self.frame%cycle_length:
                self.frame_time += dt
                if self.frame_time > cycle_time:
                    self.movement = 'STANDING'
                    self.frame_time = 0
                    cycle_index = self.move_frames[self.movement + ' ' + self.facing][0]
                    cycle_length = self.move_frames[self.movement + ' ' + self.facing][1]
                    cycle_time = self.move_frames[self.movement + ' ' + self.facing][2]
                self.frame_time = self.frame_time % cycle_time
                self.frame = int(cycle_index + (self.frame_time*cycle_length)//cycle_time)
        elif self.movement == 'STANDING':
            self.frame = int(cycle_index)
        if self.attacking:
            if self.shot_clock > self.cooldown:
                self.attacking = False
                self.shot_clock = self.shot_clock % self.cooldown
            else:
                self.shot_clock = self.shot_clock % self.cooldown
                self.frame = int((self.frame-10)%22 + 32 + (22*((self.shot_clock*3)//self.cooldown)))
        if not self.frame in range(len(self.images)):
            self.frame = int(cycle_index)




    def update(self, dt, stage, friendly_projectiles: pygame.sprite.Group):
        ''' update the position of the Avatar while taking physics, collisions, and controls into account'''

        super().update()
        self.collisions = []

        self.shot_clock += dt


        self.cycle_frames(dt)

        self.check_collisions(dt, stage)

        self.controls(dt)

        if self.facing == 'LEFT':
            if not 'LEFT' in self.inputs:
                if 'RIGHT' in self.inputs:
                    self.facing = 'RIGHT'
        elif self.facing == 'RIGHT':
            if not 'RIGHT' in self.inputs:
                if 'LEFT' in self.inputs:
                    self.facing = 'LEFT'

        if self.movement == 'RUN' and len(self.inputs) == 0:
            self.movement = 'STANDING'


        self.handpos = Vector2(self.xnew, self.ynew)

        if self.shoot:
            self.shoot = False
            friendly_projectiles.add(Shuriken(self.handpos.x, self.handpos.y, self.trajectory, self.weaponimages))

        #update avatar position
        self.x = self.xnew
        self.y = self.ynew

        #Prevent avatar from leaving the display area
        if self.x < 0:
            self.x = 0
        if self.x > stage.width-self.width():
            self.x = stage.width-self.width()
