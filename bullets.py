import pygame

pygame.init()

class projectile(Fynanmic):
	def __init__(self,x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle
	def __str__(self):
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Radius: " + str(self.radius) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		angle = "Angle: " + str(self.angle) + "\n"
		lifetime = "Lifeline :" + str(self.lifetime) + "\n"
		return location + size + speed + angle + lifetime ##Printing important information

	def update_projectile(self):
		self.coverdraw()
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel


class bullet(projectile):
	def __init__(self, x, y, angle):
		super(bullet, self).__init__(x, y, angle)

	def update_projectile(self):
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel

class shurikens(projectile):
	def __init__(self, x, y, angle):
		super(bullet,self).__init__(x, y, angle)

	def update_projectile(self):
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel
