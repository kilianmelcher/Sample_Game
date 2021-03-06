import pygame
import colors


class Projectile(object):
	
	def __init__(self,x,y,radius,color,direction):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.direction = direction
		self.speed = 10 * direction
		self.hitbox = pygame.Rect(self.x,self.y,5,5)

	def draw(self,display):	
		pygame.draw.circle(display,self.color, (self.x,self.y) ,self.radius)

		#Set the position as the bullet moves
		self.hitbox = pygame.Rect(self.x,self.y,5,5)

