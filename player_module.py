import pygame
import images

class Player(object):

	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 5
		self.jumping = False
		self.jump_count = 10
		self.left = False
		self.right = True
		self.walk_count = 0
		self.standing = True
		self.hitbox = (self.x+18,self.y+12,28,50)

	def draw(self,display):

		if self.walk_count + 1 >= 27:
			self.walk_count = 0

		if not self.standing:

			if self.left:
				display.blit(images.walk_left[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			elif self.right:
				display.blit(images.walk_right[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

		else: 

			if self.right:
				display.blit(images.walk_right[0], (self.x,self.y) )
			else:
				display.blit(images.walk_left[0], (self.x,self.y) )

		#Set the position as the character walks
		self.hitbox = (self.x+18,self.y+12,28,50)
		
	def hit(self):
		pass