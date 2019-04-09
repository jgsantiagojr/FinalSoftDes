import pygame

pygame.init()

class projectile(object):
	def __init__(self,x, y,radius,color, angle, window,winL, winH, lifetime = 0):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.angle = angle
		self.vel = .5
		self.window = window
		self.winL = winL
		self.winH = winH
		self.lifetime = lifetime
	def __str__(self):
		location = "Coordinates: (" + str(self.x) + "," + str(self.y) + ") \n"
		size = "Radius: " + str(self.radius) + "\n"
		speed = "Speed: " +  str(self.vel) + "\n"
		angle = "Angle: " + str(self.angle) + "\n"
		lifetime = "Lifeline :" + str(self.lifetime) + "\n"
		return location + size + speed + angle + lifetime ##Printing important information
	def coverdraw(self):
		pygame.draw.circle(self.window, (0,0,0), (round(self.x), round(self.y)), round(self.radius))

	def draw(self):
		pygame.draw.circle(self.window, self.color, (round(self.x), round(self.y)), round(self.radius))

	def update_projectile(self):
		self.coverdraw()
		self.x += math.degrees(math.cos(self.angle)) * self.vel
		self.y += math.degrees(math.sin(self.angle)) * self.vel
		if self.x > self.winL :
			self.x = 0
		if self.x < 0 :
			self.x = self.winL
		if self.y > self.winH :
			self.y = 0
		if self.y < 0 :
			self.y = self.winH
		# self.update_hitbox()
		self.draw()
		self.lifetime += 1
