import pygame
from entity import Entity, DynamicEntity

class Projectile(DynamicEntity):
	def __init__(self,x, y, trajectory, images):
		super().__init__(x,y,images)
		self.x = x
		self.y = y
		self.trajectory = trajectory
		self.speed = 1

	def __str__(self):
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Radius: " + str(self.radius) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		angle = "Angle: " + str(self.angle) + "\n"
		lifetime = "Lifeline :" + str(self.lifetime) + "\n"
		return location + size + speed + angle + lifetime ##Printing important information

	def update(self, dt):
		self.x += self.trajectory[0] * self.speed * dt
		self.y += self.trajectory[1] * self.speed * dt


class Bullet(Projectile):
	def __init__(self, x, y, trajectory, images):
		super().__init__(x, y, trajectory, images)
		self.speed = self.speed*5


class Shuriken(Projectile):
	def __init__(self, x, y, trajectory, images):
		super().__init__(x, y, trajectory, images)
