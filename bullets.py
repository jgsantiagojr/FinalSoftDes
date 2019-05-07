import pygame
from entity import Entity, DynamicEntity

class Projectile(DynamicEntity):
	def __init__(self,x, y, trajectory, images):
		super().__init__(x,y,images)
		self.x = x
		self.y = y
		self.trajectory = trajectory
		self.speed = 1

		self.frame_time = 0
		self.cycle_time = 500

	def __str__(self):
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Radius: " + str(self.radius) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		angle = "Angle: " + str(self.angle) + "\n"
		lifetime = "Lifeline :" + str(self.lifetime) + "\n"
		return location + size + speed + angle + lifetime ##Printing important information

	def update(self, dt, stage):
		super().update()
		self.x += self.trajectory[0] * self.speed * dt
		self.y += self.trajectory[1] * self.speed * dt
		if not stage.contains_point((self.x,self.y)):
			self.kill()
		if len(self.images)>1:
			self.frame_time += dt
			self.frame_time = self.frame_time % self.cycle_time
			self.frame = int((self.frame_time*len(self.images))//self.cycle_time)


class Bullet(Projectile):
	def __init__(self, x, y, trajectory, images):
		super().__init__(x, y, trajectory, images)
		self.speed = self.speed*2


class Shuriken(Projectile):
	def __init__(self, x, y, trajectory, images):
		super().__init__(x, y, trajectory, images)
		self.speed = self.speed
